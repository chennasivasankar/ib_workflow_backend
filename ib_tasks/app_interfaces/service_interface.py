from typing import List

from ib_tasks.interactors.get_task_fields_and_actions import \
    GetTaskFieldsAndActionsInteractor
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
from ib_tasks.storages.tasks_storage_implementation import \
    TasksStorageImplementation


class TaskDetailsServiceInterface:

    @staticmethod
    def get_task_details(task_dtos: List[GetTaskDetailsDTO]):
        storage = TasksStorageImplementation()
        interactor = GetTaskFieldsAndActionsInteractor(storage)
        result = interactor.get_task_fields_and_action(task_dtos)
        return result


from typing import List

from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO


class ServiceInterface:

    @staticmethod
    def get_task_ids_for_the_stages(
            task_config_dtos: List[TaskDetailsConfigDTO]):
        from ib_tasks.interactors.get_task_ids_interactor import \
            GetTaskIdsInteractor
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        interactor = GetTaskIdsInteractor(
            task_storage=TasksStorageImplementation(),
            stage_storage=StagesStorageImplementation()
        )

        task_ids_dtos = interactor.get_task_ids(
            task_details_configs=task_config_dtos
        )
        return task_ids_dtos

    @staticmethod
    def get_task_details(task_dtos: List[GetTaskDetailsDTO]):
        storage = TasksStorageImplementation()
        interactor = GetTaskFieldsAndActionsInteractor(storage)
        result = interactor.get_task_fields_and_action(task_dtos)
        return result

