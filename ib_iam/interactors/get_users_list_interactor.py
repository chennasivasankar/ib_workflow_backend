from typing import List

from ib_iam.adapters.dtos import UserProfileDTO, SearchQueryWithPaginationDTO
from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin, \
    InvalidOffsetValue, InvalidLimitValue, InvalidUserId, RoleIdsAreInvalid
from ib_iam.interactors.dtos.dtos import SearchQueryAndTypeDTO
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.dtos \
    import ListOfCompleteUsersDTO
from ib_iam.interactors.presenter_interfaces.get_users_list_presenter_interface \
    import GetUsersListPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface \
    import UserStorageInterface


class GetUsersDetailsInteractor(ValidationMixin):
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def get_users_details_wrapper(
            self, user_id: str, pagination_dto: PaginationDTO,
            presenter: GetUsersListPresenterInterface,
            search_query_and_type_dto: SearchQueryAndTypeDTO
    ):
        try:
            complete_user_details_dtos = self.get_users_details(
                user_id=user_id, offset=pagination_dto.offset,
                limit=pagination_dto.limit,
                search_query_and_type_dto=search_query_and_type_dto)
            response = presenter.response_for_get_users(
                complete_user_details_dtos)
        except UserIsNotAdmin:
            response = presenter.raise_user_is_not_admin_exception()
        except InvalidOffsetValue:
            response = presenter.raise_invalid_offset_value_exception()
        except InvalidLimitValue:
            response = presenter.raise_invalid_limit_value_exception()
        except InvalidUserId:
            response = presenter.raise_invalid_user()
        return response

    def get_users_details(
            self, user_id: str, offset: int, limit: int,
            search_query_and_type_dto: SearchQueryAndTypeDTO
    ) -> ListOfCompleteUsersDTO:
        self._validate_is_user_admin(user_id=user_id)
        self._validate_pagination_details(offset=offset, limit=limit)
        user_dtos = self.user_storage.get_users_who_are_not_admins(
            offset=offset, limit=limit,
            search_query_and_type_dto=search_query_and_type_dto
        )
        total_count = self.user_storage.get_total_count_of_users_for_query()
        user_ids = [user_dto.user_id for user_dto in user_dtos]
        return self._get_complete_user_details_dto(user_ids, total_count)

    def get_user_details_for_given_role_ids_based_on_query(
            self, role_ids: List[str],
            search_query_with_pagination_dto: SearchQueryWithPaginationDTO
    ) -> List[UserProfileDTO]:
        self._validate_pagination_details(
            offset=search_query_with_pagination_dto.offset,
            limit=search_query_with_pagination_dto.limit)

        from ib_iam.constants.config import ALL_ROLES_ID
        if ALL_ROLES_ID in role_ids:
            role_ids = self.user_storage.get_all_distinct_roles()

        user_ids = self.user_storage.get_user_ids_for_given_role_ids(
            role_ids=role_ids)

        user_ids_based_on_query = \
            self.user_storage.get_user_ids_based_on_given_query(
                user_ids=user_ids,
                search_query_with_pagination_dto=
                search_query_with_pagination_dto)
        user_profile_dtos = \
            self._get_user_profile_dtos(user_ids_based_on_query)

        return user_profile_dtos

    def _get_complete_user_details_dto(self, user_ids, total_count):
        user_team_dtos = self.user_storage.get_team_details_of_users_bulk(
            user_ids=user_ids)
        user_role_dtos = self.user_storage.get_role_details_of_users_bulk(
            user_ids=user_ids)
        user_company_dtos = self.user_storage.get_company_details_of_users_bulk(
            user_ids=user_ids)
        user_profile_dtos = self._get_user_profile_dtos(user_ids)
        return self._convert_complete_user_details_dtos(
            user_team_dtos, user_role_dtos, user_company_dtos,
            user_profile_dtos, total_count)

    @staticmethod
    def _get_user_profile_dtos(user_ids):
        from ib_iam.adapters.user_service import UserService
        user_service = UserService()
        user_profile_dtos = user_service.get_user_profile_bulk(
            user_ids=user_ids)
        return user_profile_dtos

    @staticmethod
    def get_user_dtos(user_ids):
        from ib_iam.adapters.user_service import UserService
        user_service = UserService()
        user_dtos = user_service.get_user_profile_bulk(
            user_ids=user_ids
        )
        return user_dtos

    def get_valid_user_ids(self, user_ids: List[str]):
        valid_user_ids = self.user_storage.get_valid_user_ids(
            user_ids=user_ids)
        return valid_user_ids

    @staticmethod
    def _convert_complete_user_details_dtos(
            user_team_dtos, user_role_dtos,
            user_company_dtos, user_profile_dtos, total_no_of_users):
        complete_user_details_dto = ListOfCompleteUsersDTO(
            users=user_profile_dtos,
            teams=user_team_dtos,
            roles=user_role_dtos,
            companies=user_company_dtos,
            total_no_of_users=total_no_of_users
        )
        return complete_user_details_dto

    @staticmethod
    def _get_user_team(user_team_dtos, user_id):
        teams = []
        for team_dto in user_team_dtos:
            if team_dto.user_id == user_id:
                teams.append(team_dto)
        return teams

    @staticmethod
    def _get_user_company(user_company_dtos, user_id):
        for company_dto in user_company_dtos:
            if company_dto.user_id == user_id:
                return company_dto

    @staticmethod
    def _get_profile(user_profile_dtos, user_id):
        for user_profile in user_profile_dtos:
            if user_profile.user_id == user_id:
                return user_profile

    @staticmethod
    def _get_role(user_role_dtos, user_id):
        roles = []
        for user_role_dto in user_role_dtos:
            if user_role_dto.user_id == user_id:
                roles.append(user_role_dto)
        return roles

    def get_user_dtos_based_on_limit_and_offset(
            self, limit: int, offset: int, search_query: str
    ):
        self._validate_pagination_details(offset=offset, limit=limit)
        user_details_dtos = self.user_storage.get_user_details_dtos_based_on_limit_offset_and_search_query(
            limit=limit, offset=offset, search_query=search_query
        )
        return user_details_dtos

    def get_all_user_dtos_based_on_query(self, search_query: str):
        user_details_dtos = self.user_storage.get_user_details_dtos_based_on_search_query(
            search_query=search_query
        )
        return user_details_dtos

    def get_user_details_for_given_role_ids(
            self, role_ids: List[str]) -> List[UserProfileDTO]:
        from ib_iam.constants.config import ALL_ROLES_ID
        if ALL_ROLES_ID in role_ids:
            user_ids = self.user_storage.get_user_ids_who_are_not_admin()
        else:
            self._validate_role_ids(role_ids=role_ids)
            user_ids = self.user_storage.get_user_ids(role_ids=role_ids)
        from ib_iam.adapters.service_adapter import get_service_adapter
        service = get_service_adapter()
        user_details_dtos = service.user_service.get_basic_user_dtos(
            user_ids=user_ids)
        return user_details_dtos

    def _validate_role_ids(self, role_ids: List[str]):
        valid_role_ids = self.user_storage.get_valid_role_ids(
            role_ids=role_ids)
        if len(role_ids) != len(valid_role_ids):
            raise RoleIdsAreInvalid
