import abc
from typing import List

from ib_adhoc_tasks.adapters.dtos import TasksCompleteDetailsDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO


class GetChildGroupsInGroupPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def prepare_response_for_get_child_groups_in_group(
            self, group_details_dtos: List[GroupDetailsDTO],
            total_child_groups_count: int,
            task_details_dto: TasksCompleteDetailsDTO
    ):
        pass
