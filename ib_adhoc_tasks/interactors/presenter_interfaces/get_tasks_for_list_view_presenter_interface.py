import abc
from typing import List

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO


class GetTasksForListViewPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def raise_invalid_project_id(self):
        pass

    @abc.abstractmethod
    def get_task_details_group_by_info_response(
            self,
            group_details_dtos: List[GroupDetailsDTO],
            task_details_dto: TasksCompleteDetailsDTO
    ):
        pass

    @abc.abstractmethod
    def raise_invalid_offset_value(self):
        pass

    @abc.abstractmethod
    def raise_invalid_limit_value(self):
        pass

    @abc.abstractmethod
    def raise_invalid_user_id(self):
        pass

    @abc.abstractmethod
    def raise_invalid_user_for_project(self):
        pass


