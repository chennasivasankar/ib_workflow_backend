import abc
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO


class ProjectStorageInterface(abc.ABC):

    @abc.abstractmethod
    def add_projects(self, project_dtos: List[ProjectDTO]):
        pass
