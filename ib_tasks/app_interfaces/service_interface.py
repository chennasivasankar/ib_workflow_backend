from typing import List

from ib_tasks.constants.enum import ViewType
from ib_tasks.interactors.get_task_fields_and_actions import \
    GetTaskFieldsAndActionsInteractor
from ib_tasks.interactors.storage_interfaces.stage_dtos import GetTaskStageCompleteDetailsDTO
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
from ib_tasks.storages.tasks_storage_implementation import TasksStorageImplementation


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
        from ib_tasks.storages.elasticsearch_storage_implementation import \
            ElasticSearchStorageImplementation
        elasticsearch_storage = ElasticSearchStorageImplementation()
        from ib_tasks.storages.filter_storage_implementation import \
            FilterStorageImplementation
        filter_storage = FilterStorageImplementation()
        interactor = GetTaskIdsInteractor(
            task_storage=TasksStorageImplementation(),
            stage_storage=StagesStorageImplementation(),
            filter_storage=filter_storage,
            elasticsearch_storage=elasticsearch_storage
        )

        task_ids_dtos = interactor.get_task_ids(
            task_details_configs=task_config_dtos
        )
        return task_ids_dtos

    @staticmethod
    def get_task_details(task_dtos: List[GetTaskDetailsDTO], user_id: str,
                         view_type: ViewType) -> \
            List[GetTaskStageCompleteDetailsDTO]:
        from ib_tasks.storages.fields_storage_implementation import \
            FieldsStorageImplementation
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        field_storage = FieldsStorageImplementation()
        stage_storage = StagesStorageImplementation()
        action_storage = ActionsStorageImplementation()
        task_storage = TasksStorageImplementation()

        interactor = GetTaskFieldsAndActionsInteractor(
            field_storage=field_storage,
            stage_storage=stage_storage,
            action_storage=action_storage,
            task_storage=task_storage,
        )
        result = interactor.get_task_fields_and_action(task_dtos, user_id, view_type)
        return result

    def get_assignees_for_task_stages(self, task_stage_dtos: List[GetTaskDetailsDTO]):
        pass

