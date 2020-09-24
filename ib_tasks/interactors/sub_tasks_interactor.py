from typing import List

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
        return subtasks_count_dtos

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
