import abc
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO


class ProjectStorageInterface(abc.ABC):

    @abc.abstractmethod
    def add_projects(self, project_dtos: List[ProjectDTO]):
        pass

    @abc.abstractmethod
    def get_valid_project_ids_from_given_project_ids(
            self, project_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_project_dtos(self):
        pass

    @abc.abstractmethod
    def get_project_dtos_for_given_project_ids(
            self, project_ids: List[str]) -> List[ProjectDTO]:
        pass