from typing import List

from ib_boards.adapters.service_adapter import get_service_adapter
from ib_boards.interactors.dtos import TaskColumnDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.storage_interfaces.dtos import TaskDTO


class GetTaskDetailsInteractor:
    def __init__(self):
        pass

    def get_task_details_wrapper(self, presenter: PresenterInterface,
                                 tasks_dtos: List[TaskDTO], user_id: str):
        task_fields_dtos, task_actions_dtos, task_details = self.get_task_details(
            tasks_dtos, user_id)
        return presenter.get_response_for_task_details(
            task_actions_dtos, task_fields_dtos, task_details)

    def get_task_details(self, tasks_dtos: List[TaskDTO], user_id: str):
        task_details = self._get_task_and_column_ids(tasks_dtos)
        task_service = get_service_adapter().task_service
        task_fields_dtos, task_actions_dtos = task_service. \
            get_task_details_dtos(task_dtos=tasks_dtos, user_id=user_id)

        return task_fields_dtos, task_actions_dtos, task_details

    @staticmethod
    def _get_task_and_column_ids(tasks_dtos):
        task_details = [TaskColumnDTO(
            task_id=task_dto.task_id,
            column_id=task_dto.column_id)
            for task_dto in tasks_dtos]
        return task_details
