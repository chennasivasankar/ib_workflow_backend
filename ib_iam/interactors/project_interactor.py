from typing import List, Tuple, Optional

from ib_iam.app_interfaces.dtos import ProjectTeamUserDTO, \
    UserIdWithTeamIDAndNameDTO, ProjectTeamsAndUsersDTO, UserTeamsDTO
from ib_iam.exceptions.custom_exceptions import InvalidUserIds
from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO, UserTeamDTO, \
    TeamIdAndNameDTO
    UserIdWithTeamIDAndNameDTO
from ib_iam.interactors.dtos.dtos import ProjectWithTeamIdsAndRolesDTO
from ib_iam.interactors.presenter_interfaces.add_project_presenter_interface import \
    AddProjectPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO, \
    ProjectWithoutIdDTO
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface
from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class UsersNotExistsForGivenProject(Exception):
    def __init__(self, user_ids):
        self.user_ids = user_ids


class TeamsNotExistForGivenProject(Exception):
    def __init__(self, team_ids: List[str]):
        self.team_ids = team_ids


class UsersNotExistsForGivenTeams(Exception):
    def __init__(self, user_ids: List[str]):
        self.user_ids = user_ids


class ProjectInteractor:

    def __init__(
            self, project_storage: ProjectStorageInterface,
            team_storage: TeamStorageInterface,
            user_storage: UserStorageInterface
    ):
        self.project_storage = project_storage
        self.team_storage = team_storage
        self.user_storage = user_storage

    def add_projects(self, project_dtos: List[ProjectDTO]):
        # todo check for duplicate project_ids in dtos
        # todo get to know if any permissions has to apply
        # todo check if name or project_id is empty in any project dto
        self.project_storage.add_projects(project_dtos=project_dtos)

    def get_valid_project_ids(self, project_ids):
        # todo check for duplicate project_ids
        valid_project_ids = \
            self.project_storage.get_valid_project_ids_from_given_project_ids(
                project_ids=project_ids)
        return valid_project_ids

    def get_project_dtos_bulk(
            self, project_ids: List[str]) -> List[ProjectDTO]:
        project_dtos = self.project_storage.get_project_dtos_for_given_project_ids(
            project_ids=project_ids)
        invalid_project_ids = self._get_invalid_project_ids(
            project_dtos=project_dtos, project_ids=project_ids)
        if invalid_project_ids:
            from ib_iam.exceptions.custom_exceptions import InvalidProjectIds
            raise InvalidProjectIds(project_ids=project_ids)
        return project_dtos

    @staticmethod
    def _get_invalid_project_ids(
            project_dtos: List[ProjectDTO], project_ids: List[str]
    ) -> List[str]:
        for project_dto in project_dtos:
            if project_dto.project_id in project_ids:
                project_ids.remove(project_dto.project_id)
        return project_ids

    def get_team_details_for_given_project_team_user_details_dto(
            self, project_team_user_dto: ProjectTeamUserDTO
    ) -> UserIdWithTeamIDAndNameDTO:
        # todo confirm and add invalid team and user exceptions
        self._validate_project(project_id=project_team_user_dto.project_id)
        self._validate_team_existence_in_project(
            project_team_user_dto=project_team_user_dto)
        self._validate_user_existence_in_given_team(
            project_team_user_dto=project_team_user_dto)
        name = self.project_storage.get_team_name(
            team_id=project_team_user_dto.team_id)
        from ib_iam.app_interfaces.dtos import UserIdWithTeamIDAndNameDTO
        user_id_with_team_id_and_name_dto = UserIdWithTeamIDAndNameDTO(
            user_id=project_team_user_dto.user_id,
            team_id=project_team_user_dto.team_id,
            name=name)
        return user_id_with_team_id_and_name_dto

    def get_user_team_dtos_for_given_project_teams_and_users_details_dto(
            self, project_teams_and_users_dto: ProjectTeamsAndUsersDTO
    ) -> List[UserTeamDTO]:
        project_id = project_teams_and_users_dto.project_id
        user_ids, team_ids = self._fetch_user_ids_and_team_ids(
            project_teams_and_users_dto=project_teams_and_users_dto)
        self._validate_project(project_id=project_id)
        valid_team_ids = self.project_storage.get_valid_team_ids_for_given_project(
            project_id=project_id, team_ids=team_ids)
        invalid_team_ids = list(set(team_ids) - set(valid_team_ids))
        if invalid_team_ids:
            raise TeamsNotExistForGivenProject(team_ids=invalid_team_ids)
        team_user_dtos = self.team_storage.get_team_user_dtos(
            team_ids=valid_team_ids, user_ids=user_ids)
        invalid_user_ids = self._get_invalid_user_ids_for_given_team_ids(
            user_ids=user_ids, team_user_dtos=team_user_dtos)
        if invalid_user_ids:
            raise UsersNotExistsForGivenTeams(user_ids=invalid_user_ids)
        return team_user_dtos

    @staticmethod
    def _get_invalid_user_ids_for_given_team_ids(
            user_ids: List[str], team_user_dtos: List[UserTeamDTO]
    ) -> List[str]:
        for team_user_dto in team_user_dtos:
            if team_user_dto.user_id in user_ids:
                user_ids.remove(team_user_dto.user_id)
        return user_ids

    @staticmethod
    def _fetch_user_ids_and_team_ids(
            project_teams_and_users_dto: ProjectTeamsAndUsersDTO
    ) -> Tuple[List[str], List[str]]:
        user_ids = []
        team_ids = []
        user_and_team_id_dtos = project_teams_and_users_dto.user_id_with_team_id_dtos
        for user_and_team_id_dto in user_and_team_id_dtos:
            user_ids.append(user_and_team_id_dto.user_id)
            team_ids.append(user_and_team_id_dto.team_id)
        return user_ids, team_ids

    def is_valid_user_id_for_given_project(
            self, user_id: str, project_id: str) -> bool:
        self._validate_user_id(user_id=user_id)
        self._validate_project(project_id=project_id)
        return self.project_storage.is_user_exist_given_project(
            user_id=user_id, project_id=project_id)

    def _validate_user_id(self, user_id: str):
        is_valid_user_id = self.user_storage.is_user_exist(user_id=user_id)
        if not is_valid_user_id:
            from ib_iam.exceptions.custom_exceptions import InvalidUserId
            raise InvalidUserId

    def _validate_project(self, project_id: str):
        valid_project_ids = self.project_storage \
            .get_valid_project_ids_from_given_project_ids(
            project_ids=[project_id])
        is_not_valid_project = not (
                len(valid_project_ids) == 1 and
                valid_project_ids[0] == project_id
        )
        if is_not_valid_project:
            from ib_iam.exceptions.custom_exceptions import InvalidProjectId
            raise InvalidProjectId

    def _validate_team_existence_in_project(
            self, project_team_user_dto: ProjectTeamUserDTO):
        is_team_exists_in_project = self.project_storage \
            .is_team_exists_in_project(
            project_id=project_team_user_dto.project_id,
            team_id=project_team_user_dto.team_id)
        is_team_not_exists_in_project = not is_team_exists_in_project
        if is_team_not_exists_in_project:
            from ib_iam.exceptions.custom_exceptions import \
                TeamNotExistsInGivenProject
            raise TeamNotExistsInGivenProject

    def _validate_user_existence_in_given_team(
            self, project_team_user_dto: ProjectTeamUserDTO):
        is_user_exists_in_team = self.project_storage \
            .is_user_exists_in_team(team_id=project_team_user_dto.team_id,
                                    user_id=project_team_user_dto.user_id)
        is_user_not_exists_in_team = not is_user_exists_in_team
        if is_user_not_exists_in_team:
            from ib_iam.exceptions.custom_exceptions import \
                UserNotExistsInGivenTeam
            raise UserNotExistsInGivenTeam

    def get_team_dtos(
            self, team_ids: List[str], project_id: str
    ) -> List[TeamIdAndNameDTO]:
        valid_team_ids = self.project_storage.get_valid_team_ids_for_given_project(
            project_id=project_id, team_ids=team_ids)
        return self.team_storage.get_team_id_and_name_dtos(
            team_ids=valid_team_ids)

    def get_user_teams_for_each_project_user(
            self, user_ids: List[str], project_id: str
    ) -> List[UserTeamsDTO]:
        self._validate_project(project_id=project_id)
        valid_user_ids = self.user_storage.get_valid_user_ids(
            user_ids=user_ids)
        if len(valid_user_ids) != len(user_ids):
            invalid_user_ids = list(set(user_ids) - set(valid_user_ids))
            raise InvalidUserIds(invalid_user_ids)
        user_team_dtos = \
            self._validate_user_ids_and_get_user_team_dtos_for_given_project(
                project_id=project_id, user_ids=valid_user_ids)
        return self._fetch_user_teams_for_each_user(
            user_team_dtos=user_team_dtos)

    def _validate_user_ids_and_get_user_team_dtos_for_given_project(
            self, project_id: str, user_ids: List[str]
    ) -> Optional[List[UserTeamDTO]]:
        team_ids = self.project_storage.get_valid_team_ids(
            project_id=project_id)
        user_team_dtos = self.team_storage.get_team_user_dtos(
            user_ids=user_ids, team_ids=team_ids)
        for user_team_dto in user_team_dtos:
            if user_team_dto.user_id in user_ids:
                user_ids.remove(user_team_dto.user_id)
        not_exists_users_in_given_project = user_ids
        if not_exists_users_in_given_project:
            raise UsersNotExistsForGivenProject(
                user_ids=not_exists_users_in_given_project)
        return user_team_dtos

    def _fetch_user_teams_for_each_user(
            self, user_team_dtos: List[UserTeamDTO]
    ) -> List[UserTeamsDTO]:
        user_teams_dict = {}
        for user_team_dto in user_team_dtos:
            try:
                user_teams_dict[
                    user_team_dto.user_id
                ].user_teams.append(
                    self._convert_to_team_id_and_name_dto(
                        user_team_dto=user_team_dto)
                )
            except KeyError:
                user_teams_dict[user_team_dto.user_id] = UserTeamsDTO(
                    user_id=user_team_dto.user_id, user_teams=[
                        self._convert_to_team_id_and_name_dto(
                            user_team_dto=user_team_dto)
                    ]
                )
        return list(user_teams_dict.values())

    @staticmethod
    def _convert_to_team_id_and_name_dto(
            user_team_dto: UserTeamDTO) -> TeamIdAndNameDTO:
        return TeamIdAndNameDTO(
            team_id=user_team_dto.team_id, team_name=user_team_dto.team_name)

    def add_project_wrapper(
            self,
            project_with_team_ids_and_roles_dto: ProjectWithTeamIdsAndRolesDTO,
            presenter: AddProjectPresenterInterface):
        self.add_project(project_with_team_ids_and_roles_dto=
                         project_with_team_ids_and_roles_dto)
        response = presenter.get_success_response_for_add_project()
        return response

    def add_project(
            self,
            project_with_team_ids_and_roles_dto: ProjectWithTeamIdsAndRolesDTO
    ):
        # todo confirm and write user permissions
        # todo validate given team_ids
        # todo validate given project_id is not exists already
        # todo validate is duplicate role_ids send
        # todo validate given role_ids is not exists already for
        #  any of the roles of any project
        project_without_id_dto = ProjectWithoutIdDTO(
            name=project_with_team_ids_and_roles_dto.name,
            description=project_with_team_ids_and_roles_dto.description,
            logo_url=project_with_team_ids_and_roles_dto.logo_url)
        project_id = self.project_storage.add_project(
            project_without_id_dto=project_without_id_dto)
        self.project_storage.assign_teams_to_projects(
            project_id=project_id,
            team_ids=project_with_team_ids_and_roles_dto.team_ids)
        self.project_storage.add_project_roles(
            project_id=project_id,
            roles=project_with_team_ids_and_roles_dto.roles)
