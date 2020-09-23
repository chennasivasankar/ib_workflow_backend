from typing import List

from ib_tasks.interactors.storage_interfaces.task_dtos import TaskProjectDTO, \
    TaskDisplayIdDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class GetTaskDetailsInteractor:
    def __init__(self, task_storage: TaskStorageInterface):
        self.task_storage = task_storage

    def get_task_project_ids(self, task_ids: List[int]) -> List[
        TaskProjectDTO]:
        self._validate_task_ids(task_ids)
        task_project_dtos = self.task_storage.get_task_project_ids(task_ids)
        return task_project_dtos

    def _validate_task_ids(self, task_ids: List[int]):
        valid_task_ids = self.task_storage.get_valid_task_ids(task_ids)
        invalid_task_ids = [task_id for task_id in task_ids if task_id not
                            in valid_task_ids]
        if invalid_task_ids:
            from ib_tasks.exceptions.task_custom_exceptions import \
                InvalidTaskIds
            raise InvalidTaskIds(task_ids)

    def get_task_ids_for_given_task_display_ids(self, task_display_ids:
    List[str]) -> List[TaskDisplayIdDTO]:
        self._validate_task_display_ids(task_display_ids)
        task_display_ids_dtos = \
            self.task_storage.get_task_ids_given_task_display_ids(
                task_display_ids)
        return task_display_ids_dtos

    def _validate_task_display_ids(self, task_display_ids: List[str]):
        valid_task_display_ids = self.task_storage.get_valid_task_display_ids(
            task_display_ids)
        invalid_task_display_ids = [task_display_id for task_display_id in
                                    task_display_ids if task_display_id not
                                    in valid_task_display_ids]
        if invalid_task_display_ids:
            from ib_tasks.exceptions.task_custom_exceptions import \
                InvalidTaskDisplayIds
            raise InvalidTaskDisplayIds(invalid_task_display_ids)
