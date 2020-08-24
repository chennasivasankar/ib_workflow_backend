from typing import List

from ib_tasks.adapters.dtos import UserDetailsDTO, TeamDetailsDTO, \
    UserIdWIthTeamDetailsDTOs, TeamDetailsWithUserIdDTO, \
    ProjectDetailsDTO
from ib_tasks.interactors.field_dtos import SearchableFieldDetailDTO
from ib_tasks.interactors.get_stage_searchable_possible_assignees_interactor \
    import SearchQueryWithPaginationDTO


class InvalidProjectIdsException(Exception):
    def __init__(self, invalid_project_ids: List[str]):
        self.invalid_project_ids = invalid_project_ids


class UserIsNotInProject(Exception):
    pass




class AuthService:
    @property
    def interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_user_dtos_based_on_limit_and_offset(self, limit: int, offset: int,
                                                search_query: str) -> \
            List[SearchableFieldDetailDTO]:
        user_dtos = self.interface.get_user_dtos_based_on_limit_and_offset(
            limit=limit, offset=offset, search_query=search_query)

        searchable_value_detail_dtos = [
            SearchableFieldDetailDTO(id=user_dto.user_id, name=user_dto.name)
            for user_dto in user_dtos
        ]
        return searchable_value_detail_dtos

    def get_all_user_dtos_based_on_query(self, search_query: str) -> \
            List[SearchableFieldDetailDTO]:
        user_dtos = self.interface.get_all_user_dtos_based_on_query(
            search_query=search_query)

        searchable_value_detail_dtos = [
            SearchableFieldDetailDTO(id=user_dto.user_id, name=user_dto.name)
            for user_dto in user_dtos
        ]
        return searchable_value_detail_dtos

    def get_user_details(self, user_ids: List[str]) -> \
            List[UserDetailsDTO]:
        user_profile_details_dtos = self.interface.get_user_details_bulk(
            user_ids=user_ids)
        user_details_dtos = self._get_user_details_dtos(
            user_profile_details_dtos)

        return user_details_dtos

    def get_permitted_user_details(self, role_ids: List[str]) \
            -> List[UserDetailsDTO]:
        user_profile_details_dtos = self.interface.get_user_details_for_given_role_ids(
            role_ids=role_ids)
        user_details_dtos = self._get_user_details_dtos(
            user_profile_details_dtos)
        return user_details_dtos

    def get_user_details_for_the_given_role_ids_based_on_query(
            self, role_ids: List[str],
            search_query_with_pagination_dto:
            SearchQueryWithPaginationDTO) -> List[UserDetailsDTO]:
        user_profile_details_dtos = self.interface. \
            get_user_details_for_the_given_role_ids_based_on_query(
                role_ids=role_ids, search_query_with_pagination_dto=
                search_query_with_pagination_dto)

        user_details_dtos = self._get_user_details_dtos(
            user_profile_details_dtos)
        return user_details_dtos

    @staticmethod
    def _get_user_details_dtos(user_profile_details_dtos):
        user_details_dtos = [
            UserDetailsDTO(user_id=each_user_profile_detail_dto.user_id,
                           user_name=each_user_profile_detail_dto.name,
                           profile_pic_url=each_user_profile_detail_dto
                           .profile_pic_url)
            for each_user_profile_detail_dto in user_profile_details_dtos]
        return user_details_dtos

    def validate_if_user_is_in_project(self, user_id: str, project_id: str):
        raise NotImplementedError

    def validate_project_ids(self, project_ids: List[str]) -> \
            List[str]:
        return project_ids

    def get_team_details(self, team_ids: List[str]) -> List[TeamDetailsDTO]:
        raise NotImplementedError

    def get_projects_info_for_given_ids(self, project_ids: List[str]) -> List[
        ProjectDetailsDTO]:
        pass

    def get_team_info_for_given_user_ids(self, user_ids: List[str],
                                         project_id: str) -> List[
        UserIdWIthTeamDetailsDTOs]:
        return

    def get_team_details_for_given_team_project_details_dto(
            self, team_project_details_dto) -> \
            List[TeamDetailsWithUserIdDTO]:
        raise NotImplementedError

    def validate_team_ids(self, team_ids: List[str]) -> \
            List[str]:
        raise NotImplementedError
