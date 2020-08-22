import abc
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO


class GetProjectsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_projects(self, project_dtos: List[ProjectDTO]):
        pass
