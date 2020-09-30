"""
Created on: 30/09/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_tasks.interactors.storage_interfaces.get_task_dtos \
    import TaskBaseDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class GetTasksBaseDetailsInteractor:

    def __init__(
            self, task_storage: TaskStorageInterface,
    ):
        self.task_storage = task_storage

    def get_tasks_base_details(
            self, task_ids: List[int]) -> List[TaskBaseDetailsDTO]:
        valid_task_ids = self.task_storage.get_valid_task_ids(
            task_ids=task_ids
        )
        invalid_task_ids = [
            task_id
            for task_id in task_ids
            if task_id not in valid_task_ids
        ]
        if invalid_task_ids:
            from ib_tasks.exceptions.task_custom_exceptions import \
                InvalidTaskIds
            raise InvalidTaskIds(invalid_task_ids)
        task_base_details_dtos = self.task_storage.get_base_details_to_task_ids(
            task_ids=task_ids
        )
        return task_base_details_dtos
