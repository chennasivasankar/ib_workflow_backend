from typing import List

from ib_tasks.interactors.storage_interfaces.task_dtos import SubTasksCountDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface \
    import TaskStorageInterface


class SubTasksInteractor:

    def __init__(self,
                 task_storage: TaskStorageInterface):
        self.task_storage = task_storage

    def get_sub_tasks_count_task_ids(self, task_ids: List[int]):
        self._validate_task_ids(task_ids=task_ids)
        subtasks_count_dtos = \
            self.task_storage.get_sub_tasks_count_to_tasks(task_ids=task_ids)
        extra_sub_task_count_dtos = self._get_task_ids(subtasks_count_dtos, task_ids)
        subtasks_count_dtos += extra_sub_task_count_dtos
        return subtasks_count_dtos

    @staticmethod
    def _get_task_ids(
            subtasks_count_dtos: List[SubTasksCountDTO],
            task_ids: List[int]
    ):
        parent_task_ids = [
            subtasks_count_dto.task_id
            for subtasks_count_dto in subtasks_count_dtos
        ]
        return [
            SubTasksCountDTO(
                task_id=task_id,
                sub_tasks_count=0
            )
            for task_id in task_ids
            if task_id not in parent_task_ids
        ]

    def _validate_task_ids(self, task_ids: List[int]):
        valid_task_ids = self.task_storage.get_valid_task_ids(task_ids=task_ids)
        invalid_task_ids = [
            task_id
            for task_id in task_ids
            if task_id not in valid_task_ids
        ]
        if invalid_task_ids:
            from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds
            raise InvalidTaskIds(task_ids=invalid_task_ids)

    def get_sub_task_ids_to_task_ids(self, task_ids: List[int]):
        self._validate_task_ids(task_ids=task_ids)
        subtasks_count_dtos = \
            self.task_storage.get_sub_task_ids_to_tasks(task_ids=task_ids)
        return subtasks_count_dtos
