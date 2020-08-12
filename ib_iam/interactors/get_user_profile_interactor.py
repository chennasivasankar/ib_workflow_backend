from typing import List

from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    GetUserProfilePresenterInterface, \
    UserProfileWithTeamsAndCompanyAndTheirUsersDTO
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
            user_profile_response_dto = self.get_user_profile(
                user_id=user_id)
            response = presenter.prepare_response_for_get_user_profile(
                user_profile_response_dto=user_profile_response_dto)
        except InvalidUserId:
            response = presenter.raise_exception_for_invalid_user_id()
        except UserAccountDoesNotExist:
            response \
                = presenter.raise_exception_for_user_account_does_not_exist()
        return response

    def get_user_profile(self, user_id: str):
        from ib_iam.adapters.service_adapter import get_service_adapter
        user_service = get_service_adapter().user_service
        user_profile_dto = user_service.get_user_profile_dto(user_id=user_id)
        is_admin = self.user_storage.is_user_admin(user_id=user_id)
        user_profile_dto.is_admin = is_admin

        team_dtos = self.user_storage.get_user_related_team_dtos(
            user_id=user_id)
        team_ids = self._get_team_ids_from_team_dtos(
            team_dtos=team_dtos)
        team_user_ids_dtos = self.user_storage.get_team_user_ids_dtos(
            team_ids=team_ids)

        company_dto = self.user_storage.get_user_related_company_dto(
            user_id=user_id)
        if company_dto is not None:
            company_id = company_dto.company_id
            company_id_with_employee_ids_dtos = self.user_storage \
                .get_company_employee_ids_dtos(company_ids=[company_id])
            company_id_with_employee_ids_dto = \
                company_id_with_employee_ids_dtos[0]
        else:
            company_id_with_employee_ids_dto = None

        user_ids = self._get_all_user_ids_from_teams_and_companies(
            team_user_ids_dtos=team_user_ids_dtos,
            company_id_with_employee_ids_dto=company_id_with_employee_ids_dto)
        user_dtos = self._get_user_dtos_from_service(user_ids=user_ids)
        user_profile_response_dto = \
            UserProfileWithTeamsAndCompanyAndTheirUsersDTO(
                user_profile_dto=user_profile_dto,
                company_dto=company_dto,
                team_dtos=team_dtos,
                team_user_ids_dto=team_user_ids_dtos,
                user_dtos=user_dtos,
                company_id_with_employee_ids_dto=
                company_id_with_employee_ids_dto,
            )

        return user_profile_response_dto

    @staticmethod
    def _get_team_ids_from_team_dtos(team_dtos: List[TeamDTO]) -> List[str]:
        team_ids = [team_dto.team_id for team_dto in team_dtos]
        return team_ids

    def _get_all_user_ids_from_teams_and_companies(
            self,
            team_user_ids_dtos: List[TeamUserIdsDTO],
            company_id_with_employee_ids_dto: CompanyIdWithEmployeeIdsDTO):
        user_ids = []
        user_ids.extend(
            self._get_user_ids_from_teams(
                team_user_ids_dtos=team_user_ids_dtos))
        user_ids.extend(company_id_with_employee_ids_dto.employee_ids)
        unique_user_ids = list(set(user_ids))
        return unique_user_ids

    @staticmethod
    def _get_user_ids_from_teams(team_user_ids_dtos: List[TeamUserIdsDTO]):
        user_ids = []
        for team_user_ids_dto in team_user_ids_dtos:
            user_ids.extend(team_user_ids_dto.user_ids)
        unique_user_ids = list(set(user_ids))
        return unique_user_ids

    @staticmethod
    def _get_user_dtos_from_service(user_ids: List[str]):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        user_dtos = service.user_service.get_basic_user_dtos(user_ids=user_ids)
        return user_dtos
