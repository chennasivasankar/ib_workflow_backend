from typing import List

from ib_iam.app_interfaces.dtos import ProjectTeamUserDTO
from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface


class ProjectInteractor:

    def __init__(self, project_storage: ProjectStorageInterface):
        self.project_storage = project_storage

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

    def get_team_details_for_given_project_team_user_details_dto(
            self, project_team_user_dto: ProjectTeamUserDTO):
        self._validate_project(project_id=project_team_user_dto.project_id)
        # todo validate given team_id exists in project
        # todo validate given user_id exists in the above team

    def _validate_project(self, project_id: str):
        print("hi")
        valid_project_ids = self.project_storage \
            .get_valid_project_ids_from_given_project_ids(
            project_ids=[project_id])
        is_not_valid_project = not (len(valid_project_ids) == 1 and
                                    valid_project_ids[0] == project_id)
        if is_not_valid_project:
            from ib_iam.exceptions.custom_exceptions import InvalidProjectId
            raise InvalidProjectId
