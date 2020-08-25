from typing import List

from ib_tasks.adapters.dtos import UserDetailsDTO, TeamDetailsDTO, \
    UserIdWIthTeamDetailsDTOs, TeamDetailsWithUserIdDTO, \
    ProjectDetailsDTO, ProjectTeamUserIdsDTO
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

    def get_permitted_user_details(self, role_ids: List[str], project_id:
    str) \
            -> List[UserDetailsDTO]:
        user_profile_details_dtos = \
            self.interface.get_user_details_for_given_role_ids(
                role_ids=role_ids, project_id=project_id)
        user_details_dtos = self._get_user_details_dtos(
            user_profile_details_dtos)
        return user_details_dtos

    def get_user_details_for_the_given_role_ids_based_on_query(
            self, role_ids: List[str],
            search_query_with_pagination_dto:
            SearchQueryWithPaginationDTO, project_id: str
    ) -> List[UserDetailsDTO]:
        user_profile_details_dtos = self.interface. \
            get_user_details_for_the_given_role_ids_based_on_query(
            role_ids=role_ids, search_query_with_pagination_dto=
            search_query_with_pagination_dto, project_id=project_id)

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
        return

    def validate_project_ids(self, project_ids: List[str]) -> \
            List[str]:
        return project_ids

    def get_team_details(self, team_ids: List[str]) -> List[TeamDetailsDTO]:
        return []

    def get_projects_info_for_given_ids(
            self, project_ids: List[str]) -> List[ProjectDetailsDTO]:
        iam_project_dtos = \
            self.interface.get_project_dtos_bulk(project_ids=project_ids)
        project_dtos = [
            ProjectDetailsDTO(
                project_id=project_dto.project_id,
                name=project_dto.project_id,
                logo_url=project_dto.logo_url
            )
            for project_dto in iam_project_dtos
        ]
        return project_dtos

    def get_team_info_for_given_user_ids(
            self, user_ids: List[str], project_id: str
    ) -> List[UserIdWIthTeamDetailsDTOs]:
        user_ids = list(sorted(set(user_ids)))
        user_team_dtos = self.interface.get_user_teams_for_each_project_user(
            user_ids=user_ids, project_id=project_id)
        user_id_with_team_details_dtos = []
        for user_team_dto in user_team_dtos:
            team_details = [
                TeamDetailsDTO(team_id=user_team.team_id,
                               name=user_team.team_name)
                for user_team in user_team_dto.user_teams
            ]
            user_id_with_team_details_dtos.append(
                UserIdWIthTeamDetailsDTOs(
                    user_id=user_team_dto.user_id, team_details=team_details))
        return user_id_with_team_details_dtos

    def get_team_details_for_given_project_team_user_ids_dto(
            self, team_project_details_dto: ProjectTeamUserIdsDTO
    ) -> List[TeamDetailsWithUserIdDTO]:
        from ib_iam.app_interfaces.dtos import ProjectTeamUserDTO
        project_id = team_project_details_dto.project_id
        team_details_with_user_id_dtos = []
        for user_team_dto in \
                team_project_details_dto.user_id_with_team_id_dtos:
            project_team_user_dto = ProjectTeamUserDTO(
                user_id=user_team_dto.user_id, team_id=user_team_dto.team_id,
                project_id=project_id)
            user_team = \
                self.interface.get_team_details_for_given_project_team_user_details_dto(
                    project_team_user_dto)
            team_details_with_user_id_dtos.append(
                TeamDetailsWithUserIdDTO(
                    user_id=user_team.user_id, team_id=user_team_dto.team_id,
                    name=user_team.name)
            )
        return team_details_with_user_id_dtos

    def validate_team_ids(self, team_ids: List[str]) -> \
            List[str]:
        raise NotImplementedError
