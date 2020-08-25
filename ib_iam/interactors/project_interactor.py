from typing import List, Tuple

from ib_iam.app_interfaces.dtos import ProjectTeamUserDTO, \
    UserIdWithTeamIDAndNameDTO, ProjectTeamsAndUsersDTO, UserTeamsDTO
from ib_iam.exceptions.custom_exceptions import InvalidUserIds
from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO, UserTeamDTO, \
    TeamIdAndNameDTO
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface
from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


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
        if len(project_ids) != len(project_dtos):
            from ib_iam.exceptions.custom_exceptions import InvalidProjectIds
            raise InvalidProjectIds
        return project_dtos

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
        user_ids, valid_team_ids = self._fetch_user_ids_and_team_ids(
            project_teams_and_users_dto=project_teams_and_users_dto)

        valid_team_ids = self.project_storage.get_valid_team_ids_for_given_project(
            project_id=project_id, team_ids=valid_team_ids)
        team_user_dtos = self.team_storage.get_team_user_dtos(
            team_ids=valid_team_ids, user_ids=user_ids)
        return team_user_dtos

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
        valid_user_ids = self.user_storage.get_valid_user_ids(
            user_ids=user_ids)
        if len(valid_user_ids) != len(user_ids):
            invalid_user_ids = set(user_ids) - set(valid_user_ids)
            raise InvalidUserIds(invalid_user_ids)
        team_ids = self.project_storage.get_valid_team_ids(
            project_id=project_id)
        user_team_dtos = self.team_storage.get_team_user_dtos(
            user_ids=user_ids, team_ids=team_ids)
        return self._fetch_user_teams_for_each_user(
            user_team_dtos=user_team_dtos)

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
