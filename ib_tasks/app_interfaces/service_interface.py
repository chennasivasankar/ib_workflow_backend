from typing import List

from ib_tasks.interactors.get_task_fields_and_actions import GetTaskFieldsAndActionsInteractor
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
from ib_tasks.storages.tasks_storage_implementation import TasksStorageImplementation


class TaskDetailsServiceInterface:

    @staticmethod
    def get_task_details(task_dtos: List[GetTaskDetailsDTO]):
        storage = TasksStorageImplementation()
        interactor = GetTaskFieldsAndActionsInteractor(storage)
        result = interactor.get_task_fields_and_action(task_dtos)
        return result
