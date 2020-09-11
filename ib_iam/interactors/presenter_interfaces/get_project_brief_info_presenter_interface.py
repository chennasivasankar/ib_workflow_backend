import abc
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import ProjectWithDisplayIdDTO


class GetProjectBriefInfoPresenterInterface(abc.ABC):

    # @abc.abstractmethod
    # def response_for_invalid_offset(self):
    #     pass
    #
    # @abc.abstractmethod
    # def response_for_invalid_limit(self):
    #     pass

    @abc.abstractmethod
    def response_for_user_does_not_exist(self):
        pass

    @abc.abstractmethod
    def success_response_for_get_project_brief_info(
            self, project_dtos: List[ProjectWithDisplayIdDTO]
    ):
        pass
