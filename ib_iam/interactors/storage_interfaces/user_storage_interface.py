import abc
from typing import List, Optional

from ib_iam.adapters.dtos import SearchQueryWithPaginationDTO
from ib_iam.exceptions.custom_exceptions import InvalidUserId, InvalidUserIds, \
    InvalidUserIdsForProject, InvalidRoleIdsForProject, InvalidProjectId
from ib_iam.interactors.dtos.dtos import UserIdWithRoleIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import UserDTO, TeamWithUserIdDTO, \
    UserRoleDTO, UserCompanyDTO, CompanyIdAndNameDTO, TeamIdAndNameDTO, \
    RoleIdAndNameDTO, UserIdAndNameDTO, TeamDTO, TeamUserIdsDTO, CompanyDTO, \
    CompanyIdWithEmployeeIdsDTO, BasicUserDetailsDTO


class UserStorageInterface(abc.ABC):

    @abc.abstractmethod
    def is_user_admin(self, user_id: str) -> bool:
        pass

    @abc.abstractmethod
    def is_user_exist(self, user_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_role_objs_ids(self, role_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def check_are_valid_role_ids(self, role_ids) -> bool:
        pass

    @abc.abstractmethod
    def check_is_exists_company_id(self, company_id) -> bool:
        pass

    @abc.abstractmethod
    def check_are_valid_team_ids(self, team_ids) -> bool:
        pass

    @abc.abstractmethod
    def remove_roles_for_user(self, user_id: str):
        pass

    @abc.abstractmethod
    def remove_teams_for_user(self, user_id: str):
        pass

    @abc.abstractmethod
    def add_roles_to_the_user(self, user_id: str, role_ids: List[str]):
        pass

    @abc.abstractmethod
    def add_user_to_the_teams(self, user_id: str, team_ids: List[str]):
        pass

    @abc.abstractmethod
    def update_user_details(self, company_id: Optional[str], user_id: str,
                            name: str):
        pass

    @abc.abstractmethod
    def get_all_user_dtos(
            self, offset: int, limit: int,
            name_search_query: str) -> List[UserDTO]:
        pass

    @abc.abstractmethod
    def get_team_details_of_users_bulk(
            self, user_ids: List[str]) -> List[TeamWithUserIdDTO]:
        pass

    @abc.abstractmethod
    def get_role_details_of_users_bulk(
            self, user_ids: List[str]) -> List[UserRoleDTO]:
        pass

    @abc.abstractmethod
    def get_company_details_of_users_bulk(
            self, user_ids: List[str]) -> List[UserCompanyDTO]:
        pass

    # TODO: Typing
    @abc.abstractmethod
    def get_total_count_of_users_for_query(self, name_search_query: str):
        pass

    @abc.abstractmethod
    def get_companies(self) -> List[CompanyIdAndNameDTO]:
        pass

    @abc.abstractmethod
    def get_team_id_and_name_dtos(self) -> List[TeamIdAndNameDTO]:
        pass

    @abc.abstractmethod
    def get_roles(self) -> List[RoleIdAndNameDTO]:
        pass

    @abc.abstractmethod
    def validate_user_id(self, user_id) -> Optional[InvalidUserId]:
        pass

    @abc.abstractmethod
    def validate_user_ids(self, user_ids: List[str]) \
            -> Optional[InvalidUserIds]:
        pass

    @abc.abstractmethod
    def get_valid_user_ids(self, user_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_user_details_dtos_based_on_limit_offset_and_search_query(
            self, limit: int, offset: int, search_query: str
    ) -> List[UserIdAndNameDTO]:
        pass

    @abc.abstractmethod
    def get_user_details_dtos_based_on_search_query(
            self, search_query: str
    ) -> List[UserIdAndNameDTO]:
        pass

    @abc.abstractmethod
    def get_valid_user_ids_among_the_given_user_ids(
            self, user_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def create_user(self, is_admin: bool, user_id: str, name: str,
                    company_id: Optional[str] = None):
        pass

    @abc.abstractmethod
    def update_user_name_and_cover_page_url(
            self, name: str, cover_page_url: str, user_id: str):
        pass

    @abc.abstractmethod
    def get_user_ids(self, role_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_valid_role_ids(self, role_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_user_ids_who_are_not_admin(self) -> List[str]:
        pass

    @abc.abstractmethod
    def get_all_distinct_project_role_ids(self, project_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def get_user_ids_for_given_role_ids(
            self, role_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_user_ids_based_on_given_query(
            self, user_ids: List[str],
            search_query_with_pagination_dto: SearchQueryWithPaginationDTO
    ) -> List[str]:
        pass

    # @abc.abstractmethod
    # def get_db_role_ids(self, role_ids: List[str]) -> List[str]:
    #     pass

    @abc.abstractmethod
    def get_user_related_team_dtos(self, user_id: str) -> List[TeamDTO]:
        pass

    @abc.abstractmethod
    def get_team_user_ids_dtos(self, team_ids: List[str]) -> \
            List[TeamUserIdsDTO]:
        pass

    @abc.abstractmethod
    def get_user_related_company_dto(self, user_id: str) -> CompanyDTO:
        pass

    @abc.abstractmethod
    def get_company_employee_ids_dto(self, company_id: str) \
            -> CompanyIdWithEmployeeIdsDTO:
        pass

    @abc.abstractmethod
    def get_user_details(self, user_id: str) -> UserDTO:
        pass

    # TODO move to project storage interface
    @abc.abstractmethod
    def get_user_ids_for_given_project(self, project_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def get_basic_user_dtos_for_given_project(self, project_id: str) -> \
            List[BasicUserDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_user_role_dtos_of_a_project(
            self, user_ids: List[str], project_id: str) -> List[UserRoleDTO]:
        pass

    @abc.abstractmethod
    def assign_user_roles_for_given_project(
            self, user_id_with_role_ids_dtos: List[UserIdWithRoleIdsDTO],
            project_id: str
    ):
        pass

    @abc.abstractmethod
    def is_valid_project_id(self, project_id: str) -> bool:
        pass

    @abc.abstractmethod
    def validate_users_for_project(
            self, user_ids: List[str], project_id: str
    ) -> Optional[InvalidUserIdsForProject]:
        pass

    @abc.abstractmethod
    def validate_role_ids_for_project(
            self, role_ids: List[str], project_id: str
    ) -> Optional[InvalidRoleIdsForProject]:
        pass

    @abc.abstractmethod
    def validate_project_id(
            self, project_id: str
    ) -> Optional[InvalidProjectId]:
        pass
