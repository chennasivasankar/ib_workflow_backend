from typing import List

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    GetUserProfilePresenterInterface, \
    CompleteUserProfileDTO
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamDTO, TeamUserIdsDTO, CompanyIdWithEmployeeIdsDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetUserProfileInteractor:
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def get_user_profile_wrapper(self, user_id: str,
                                 presenter: GetUserProfilePresenterInterface):
        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        from ib_iam.adapters.user_service import UserAccountDoesNotExist
        try:
            complete_user_profile_dto = self.get_user_profile(
                user_id=user_id)
            response = presenter.prepare_response_for_get_user_profile(
                complete_user_profile_dto=complete_user_profile_dto)
        except InvalidUserId:
            response = presenter.raise_exception_for_invalid_user_id()
        except UserAccountDoesNotExist:
            response \
                = presenter.raise_exception_for_user_account_does_not_exist()
        return response

    def get_user_profile(self, user_id: str) -> CompleteUserProfileDTO:
        user_profile_dto = self._get_user_profile_dto(user_id=user_id)
        team_dtos = self.user_storage.get_user_related_team_dtos(user_id)
        team_ids = self._get_team_ids_from_team_dtos(team_dtos=team_dtos)
        team_user_ids_dtos = self.user_storage.get_team_user_ids_dtos(team_ids)
        role_dtos = self.user_storage.get_role_details_of_users_bulk(
            user_ids=[user_id])
        company_dto = self.user_storage.get_user_related_company_dto(user_id)
        company_id_with_employee_ids_dto = \
            self._get_company_id_with_employee_ids_dto(company_dto)
        user_dtos = self._get_all_user_dtos(
            team_user_ids_dtos=team_user_ids_dtos,
            company_id_with_employee_ids_dto=company_id_with_employee_ids_dto)
        complete_user_profile_dto = self._prepare_complete_user_profile_dto(
            company_dto=company_dto, role_dtos=role_dtos,
            team_dtos=team_dtos, team_user_ids_dtos=team_user_ids_dtos,
            user_dtos=user_dtos, user_profile_dto=user_profile_dto,
            company_id_with_employee_ids_dto=company_id_with_employee_ids_dto)
        return complete_user_profile_dto

    def _get_all_user_dtos(self, company_id_with_employee_ids_dto,
                           team_user_ids_dtos) -> List[UserProfileDTO]:
        user_ids = self._get_all_user_ids_from_teams_and_companies(
            team_user_ids_dtos=team_user_ids_dtos,
            company_id_with_employee_ids_dto=company_id_with_employee_ids_dto)
        user_dtos = self._get_user_dtos_from_service(user_ids=user_ids)
        return user_dtos

    @staticmethod
    def _prepare_complete_user_profile_dto(
            company_dto, role_dtos, team_dtos, team_user_ids_dtos,
            user_dtos, user_profile_dto, company_id_with_employee_ids_dto) \
            -> CompleteUserProfileDTO:
        complete_user_profile_dto = CompleteUserProfileDTO(
            user_profile_dto=user_profile_dto,
            role_dtos=role_dtos,
            company_dto=company_dto,
            team_dtos=team_dtos,
            team_user_ids_dto=team_user_ids_dtos,
            user_dtos=user_dtos,
            company_id_with_employee_ids_dto=
            company_id_with_employee_ids_dto,
        )
        return complete_user_profile_dto

    def _get_company_id_with_employee_ids_dto(self, company_dto) -> \
            CompanyIdWithEmployeeIdsDTO:
        company_id_with_employee_ids_dto = None
        if company_dto is not None:
            company_id = company_dto.company_id
            company_id_with_employee_ids_dto = self.user_storage \
                .get_company_employee_ids_dto(company_id=company_id)
        return company_id_with_employee_ids_dto

    def _get_user_profile_dto(self, user_id) -> UserProfileDTO:
        from ib_iam.adapters.service_adapter import get_service_adapter
        user_service = get_service_adapter().user_service
        user_profile_dto = user_service.get_user_profile_dto(user_id=user_id)
        user_details_dto = self.user_storage.get_user_details(user_id=user_id)
        user_profile_dto.is_admin = user_details_dto.is_admin
        user_profile_dto.cover_page_url = user_details_dto.cover_page_url
        return user_profile_dto

    @staticmethod
    def _get_team_ids_from_team_dtos(team_dtos: List[TeamDTO]) -> List[str]:
        team_ids = [team_dto.team_id for team_dto in team_dtos]
        return team_ids

    def _get_all_user_ids_from_teams_and_companies(
            self, team_user_ids_dtos: List[TeamUserIdsDTO],
            company_id_with_employee_ids_dto: CompanyIdWithEmployeeIdsDTO
    ) -> List[str]:
        user_ids = self._get_user_ids_from_teams(
            team_user_ids_dtos=team_user_ids_dtos)
        if company_id_with_employee_ids_dto is not None:
            user_ids.extend(company_id_with_employee_ids_dto.employee_ids)
        unique_user_ids = list(set(user_ids))
        return unique_user_ids

    @staticmethod
    def _get_user_ids_from_teams(team_user_ids_dtos: List[TeamUserIdsDTO]) -> \
            List[str]:
        user_ids = []
        for team_user_ids_dto in team_user_ids_dtos:
            user_ids.extend(team_user_ids_dto.user_ids)
        unique_user_ids = list(set(user_ids))
        return unique_user_ids

    @staticmethod
    def _get_user_dtos_from_service(user_ids: List[str]) -> \
            List[UserProfileDTO]:
        from ib_iam.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        user_dtos = service.user_service.get_basic_user_dtos(user_ids=user_ids)
        return user_dtos
