from typing import List
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateIds, DuplicateTaskStatusVariableIds
from ib_tasks.interactors.storage_interfaces.status_dtos import TaskStatusDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class CreateTaskStatusInteractor:

    def __init__(self, status_storage: TaskStorageInterface):
        self.status_storage = status_storage

    def create_task_status(self,
                           task_status_details_dtos: List[TaskStatusDTO]):
        task_template_ids = self._get_valid_template_ids_in_given_template_ids(
            task_status_details_dtos)
        self._validate_task_template_ids(task_template_ids)

        self._check_for_duplicate_status_ids_for_tasks(
            task_status_details_dtos)
        self.status_storage.create_status_for_tasks(task_status_details_dtos)

    def _get_valid_template_ids_in_given_template_ids(self,
                               task_status_details: List[TaskStatusDTO]):
        task_template_ids = [
            task.task_template_id for task in task_status_details]

        return task_template_ids

    def _check_for_duplicate_status_ids_for_tasks(self,
            task_status_details_dtos: List[TaskStatusDTO]):

        duplicate_task_status = []
        for current_task in task_status_details_dtos:
            duplicates = self._get_duplicate_status_values(
                current_task, task_status_details_dtos)
            if duplicates:
                duplicate_task_status.append(current_task.task_template_id)

        if duplicate_task_status:
            raise DuplicateTaskStatusVariableIds(duplicate_task_status)
        return


    def _get_duplicate_status_values(self,
                                     current_task: TaskStatusDTO,
                                     task_status_details_dtos: List[TaskStatusDTO]):
        task_status_ids = []
        for other_task in task_status_details_dtos:
            if current_task.task_template_id == other_task.task_template_id:
                task_status_ids.append(other_task.status_variable_id)
        duplicates = self._check_for_duplicate_status_ids_for_task(
            task_status_ids)
        return duplicates

    def _check_for_duplicate_status_ids_for_task(self, task_status_ids):
        duplicate_task_status_ids = list(set(
            [x for x in task_status_ids if task_status_ids.count(x) > 1]))
        return duplicate_task_status_ids

    def _validate_task_template_ids(self, task_template_ids):
        invalid_task_template_ids = []
        valid_task_template_ids = self.status_storage.get_valid_template_ids_in_given_template_ids(task_template_ids)
        for task_template_id in task_template_ids:
            if task_template_id not in valid_task_template_ids:
                invalid_task_template_ids.append(task_template_id)

        if invalid_task_template_ids:
            raise InvalidTaskTemplateIds(invalid_task_template_ids)
        return
