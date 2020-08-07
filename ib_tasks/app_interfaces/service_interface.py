from typing import List

from ib_tasks.constants.enum import VIEWTYPE
from ib_tasks.interactors.get_task_fields_and_actions import \
    GetTaskFieldsAndActionsInteractor
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO, \
    TaskDetailsConfigDTO
from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation


# class TaskDetailsServiceInterface:
#
#     @staticmethod
#     def get_task_details(task_dtos: List[GetTaskDetailsDTO]):
#         storage = TasksStorageImplementation()
#         interactor = GetTaskFieldsAndActionsInteractor(storage)
#         result = interactor.get_task_fields_and_action(task_dtos)
#         return result


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
    def get_task_details(task_dtos: List[GetTaskDetailsDTO], user_id: str,
                         view_type: VIEWTYPE):
        from ib_tasks.storages.fields_storage_implementation import \
            FieldsStorageImplementation
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        field_storage = FieldsStorageImplementation()
        stage_storage = StagesStorageImplementation()
        action_storage = ActionsStorageImplementation()

        interactor = GetTaskFieldsAndActionsInteractor(
            field_storage,
            stage_storage,
            action_storage
        )
        result = interactor.get_task_fields_and_action(task_dtos, user_id, view_type)
        return result
