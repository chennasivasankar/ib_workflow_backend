from typing import List

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.dtos.dtos import CompleteUserProfileDTO
from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    GetUserProfilePresenterInterface, \
    UserWithExtraDetailsDTO
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamDTO, TeamUserIdsDTO, CompanyIdWithEmployeeIdsDTO, UserDTO, CompanyDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetUserProfileInteractor:
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def get_user_profile_wrapper(
            self, user_id: str, presenter: GetUserProfilePresenterInterface
    ):
        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        from ib_iam.adapters.user_service import UserAccountDoesNotExist
        try:
            user_with_extra_details_dto = self.get_user_profile(
                user_id=user_id
            )
            response = presenter.prepare_response_for_get_user_profile(
                user_with_extra_details_dto=user_with_extra_details_dto
            )
        except InvalidUserId:
            response = presenter.response_for_invalid_user_id_exception()
        except UserAccountDoesNotExist:
            response = presenter.response_for_user_account_does_not_exist_exception()
        return response

    def get_user_profile(self, user_id: str) -> UserWithExtraDetailsDTO:
        user_profile_dto = self._get_user_profile_dto(user_id=user_id)
        team_dtos = self.user_storage.get_user_related_team_dtos(user_id)
        team_ids = self._get_team_ids_from_team_dtos(team_dtos=team_dtos)
        team_user_ids_dtos = self.user_storage.get_team_user_ids_dtos(team_ids)
        role_dtos = self.user_storage.get_role_details_of_users_bulk(
            user_ids=[user_id]
        )
        company_dto = self.user_storage.get_user_related_company_dto(user_id)
        company_id_with_employee_ids_dto = self._get_company_id_with_employee_ids_dto(
            company_dto
        )
        user_dtos = self._get_all_user_dtos(
            team_user_ids_dtos=team_user_ids_dtos,
            company_id_with_employee_ids_dto=company_id_with_employee_ids_dto
        )
        user_with_extra_details_dto = UserWithExtraDetailsDTO(
            user_profile_dto=user_profile_dto, company_dto=company_dto,
            team_dtos=team_dtos, team_user_ids_dto=team_user_ids_dtos,
            user_dtos=user_dtos, role_dtos=role_dtos,
            company_id_with_employee_ids_dto=company_id_with_employee_ids_dto
        )
        return user_with_extra_details_dto

    def _get_all_user_dtos(
            self, team_user_ids_dtos: List[TeamUserIdsDTO],
            company_id_with_employee_ids_dto: CompanyIdWithEmployeeIdsDTO
    ) -> List[UserProfileDTO]:
        user_ids = self._get_all_user_ids_from_teams_and_companies(
            team_user_ids_dtos=team_user_ids_dtos,
            company_id_with_employee_ids_dto=company_id_with_employee_ids_dto
        )
        user_dtos = self._get_user_dtos_from_service(user_ids=user_ids)
        return user_dtos

    def _get_company_id_with_employee_ids_dto(
            self, company_dto: CompanyDTO
    ) -> CompanyIdWithEmployeeIdsDTO:
        company_id_with_employee_ids_dto = None
        if company_dto is not None:
            company_id = company_dto.company_id
            company_id_with_employee_ids_dto = self.user_storage \
                .get_company_employee_ids_dto(company_id=company_id)
        return company_id_with_employee_ids_dto

    def _get_user_profile_dto(self, user_id: str) -> CompleteUserProfileDTO:
        from ib_iam.adapters.service_adapter import get_service_adapter
        user_service = get_service_adapter().user_service
        user_profile_dto_from_ib_user = user_service.get_user_profile_dto(
            user_id=user_id
        )
        user_details_dto_from_ib_iam = self.user_storage.get_user_details(
            user_id=user_id
        )
        complete_user_profile_dto = self._convert_to_complete_user_profile_dto(
            user_profile_dto_from_ib_user, user_details_dto_from_ib_iam
        )
        return complete_user_profile_dto

    @staticmethod
    def _convert_to_complete_user_profile_dto(
            ib_user_user_profile: UserProfileDTO,
            ib_iam_user_details: UserDTO
    ) -> CompleteUserProfileDTO:
        complete_user_profile_dto = CompleteUserProfileDTO(
            user_id=ib_iam_user_details.user_id,
            name=ib_user_user_profile.name,
            profile_pic_url=ib_user_user_profile.profile_pic_url,
            email=ib_user_user_profile.email,
            is_admin=ib_iam_user_details.is_admin,
            cover_page_url=ib_iam_user_details.cover_page_url
        )
        return complete_user_profile_dto

    @staticmethod
    def _get_team_ids_from_team_dtos(team_dtos: List[TeamDTO]) -> List[str]:
        team_ids = [team_dto.team_id for team_dto in team_dtos]
        return team_ids

    def _get_all_user_ids_from_teams_and_companies(
            self, team_user_ids_dtos: List[TeamUserIdsDTO],
            company_id_with_employee_ids_dto: CompanyIdWithEmployeeIdsDTO
    ) -> List[str]:
        user_ids = self._get_user_ids_from_teams(
            team_user_ids_dtos=team_user_ids_dtos
        )
        if company_id_with_employee_ids_dto is not None:
            user_ids.extend(company_id_with_employee_ids_dto.employee_ids)
        unique_user_ids = list(set(user_ids))
        return unique_user_ids

    @staticmethod
    def _get_user_ids_from_teams(
            team_user_ids_dtos: List[TeamUserIdsDTO]
    ) -> List[str]:
        user_ids = []
        for team_user_ids_dto in team_user_ids_dtos:
            user_ids.extend(team_user_ids_dto.user_ids)
        unique_user_ids = list(set(user_ids))
        return unique_user_ids

    @staticmethod
    def _get_user_dtos_from_service(
            user_ids: List[str]
    ) -> List[UserProfileDTO]:
        from ib_iam.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        user_dtos = service.user_service.get_basic_user_dtos(user_ids=user_ids)
        return user_dtos
