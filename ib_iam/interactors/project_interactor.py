from typing import List

from ib_iam.app_interfaces.dtos import ProjectTeamUserDTO, \
    UserIdWithTeamIDAndNameDTO
from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO
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
