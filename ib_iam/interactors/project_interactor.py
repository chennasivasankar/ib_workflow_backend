from typing import List

from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface


class ProjectInteractor:

    def __init__(self, project_storage: ProjectStorageInterface):
        self.project_storage = project_storage

    def add_projects(self, project_dtos: List[ProjectDTO]):
        self.project_storage.add_projects(project_dtos=project_dtos)
