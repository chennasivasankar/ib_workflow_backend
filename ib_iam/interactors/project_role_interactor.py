from typing import List

from ib_iam.interactors.storage_interfaces.dtos import ProjectRolesDTO
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface


class UserNotAMemberOfAProject(Exception):
    pass


class UserNotAMemeberOfProjectsException(Exception):
    def __init__(self, project_ids: List[str]):
        self.project_ids = project_ids

    def __str__(self):
        return f"user is not a member of projects:{self.project_ids}"


class ProjectRoleInteractor:

    def __init__(self, project_storage: ProjectStorageInterface):
        self.project_storage = project_storage

    def get_user_role_ids_based_on_project(self, user_id: str,
                                           project_id: str):
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        is_not_valid_project_id = not self.project_storage.is_valid_project_id(
            project_id=project_id
        )
        if is_not_valid_project_id:
            raise InvalidProjectId

        is_user_not_in_a_project = not \
            self.project_storage.is_user_in_a_project(
                user_id=user_id, project_id=project_id
            )
        if is_user_not_in_a_project:
            raise UserNotAMemberOfAProject()

        role_ids = self.project_storage.get_user_role_ids(
            user_id=user_id, project_id=project_id
        )
        return role_ids

    def get_user_role_ids_for_given_project_ids(self, user_id: str,
                                                project_ids: List[str]) -> \
            List[ProjectRolesDTO]:
        self._validate_project_ids(project_ids)
        self._validate_if_user_is_in_projects(user_id, project_ids)
        user_project_roles_dtos = \
            self.project_storage.get_user_roles_for_projects(user_id,
                                                             project_ids)
        return user_project_roles_dtos

    def _validate_project_ids(self, project_ids):
        valid_project_ids = self.project_storage.get_valid_project_ids(
            project_ids)
        invalid_project_ids = [project_id for project_id in project_ids if
                               project_id not in valid_project_ids]
        if invalid_project_ids:
            from ib_iam.exceptions.custom_exceptions import InvalidProjectIds
            raise InvalidProjectIds(invalid_project_ids)

    def _validate_if_user_is_in_projects(self, user_id: str, project_ids:
    List[str]):
        user_status_dtos = self.project_storage \
            .get_user_status_for_given_projects(
            user_id, project_ids)
        user_is_not_in_projects = [user_status_dto.project_id for
                                   user_status_dto in user_status_dtos if
                                   user_status_dto.is_exist is False]
        if user_is_not_in_projects:
            raise UserNotAMemeberOfProjectsException(user_is_not_in_projects)
