from typing import List

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

    def get_project_dtos_bulk(
            self, project_ids: List[str]) -> List[ProjectDTO]:
        project_dtos = self.project_storage.get_project_dtos_for_given_project_ids(
            project_ids=project_ids)
        if len(project_ids) != len(project_dtos):
            from ib_iam.exceptions.custom_exceptions import InvalidProjectIds
            raise InvalidProjectIds
        return project_dtos
