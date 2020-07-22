from typing import List

from ib_boards.interactors.dtos import TaskDTO
from ib_boards.interactors.storage_interfaces.dtos import (TaskFieldsDTO, TaskActionsDTO)
from ib_boards.tests.factories.storage_dtos import TaskActionsDTOFactory, TaskFieldsDTOFactory


class ServiceInterface:
    pass


class TaskService:
    @property
    def interface(self):
        from ib_tasks.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def get_task_details_dtos(self, task_dtos: List[TaskDTO],
                              field_ids: List[str],
                              user_id: str):
        actions_dto = [
            TaskActionsDTOFactory.create(
                task_id=task_dto.task_id
            ) for _index, task_dto in enumerate(task_dtos)
        ]

        fields_dto = [
            TaskFieldsDTOFactory.create(
                task_id=task_dto.task_id
            ) for _index, task_dto in enumerate(task_dtos)
        ]
        return fields_dto, actions_dto
