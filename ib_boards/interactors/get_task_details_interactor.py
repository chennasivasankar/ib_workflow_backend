from typing import List

from ib_boards.adapters.service_adapter import get_service_adapter
from ib_boards.interactors.dtos import (
    TaskColumnDTO, TaskDTO, TaskDetailsDTO, FieldsDTO, TaskStageDTO)
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface


class GetTaskDetailsInteractor:
    def __init__(self):
        pass

    def get_task_details_wrapper(self, presenter: PresenterInterface,
                                 fields_dto: List[FieldsDTO],
                                 tasks_dtos: List[TaskDetailsDTO], user_id: str):
        task_fields_dtos, task_actions_dtos, task_column_details = self. \
            get_task_details(tasks_dtos, fields_dto, user_id)
        return presenter.get_response_for_task_details(
            task_actions_dtos, task_fields_dtos, task_column_details)

    def get_task_details(self, tasks_dtos: List[TaskDetailsDTO],
                         fields_dto: List[FieldsDTO], user_id: str):

        task_column_details = self._get_task_and_column_ids(tasks_dtos)
        fields_ids = self._get_field_ids(fields_dto)
        task_stages_dto = self._get_task_stages_dto(tasks_dtos)
        task_service = get_service_adapter().tasks_service
        task_fields_dtos = task_service[0]
        task_actions_dtos = task_service[1]
        # task_fields_dtos, task_actions_dtos = task_service.\
        #     get_task_details_dtos(tasks_dtos=task_stages_dto, user_id=user_id)

        return task_fields_dtos, task_actions_dtos, task_column_details

    @staticmethod
    def _get_field_ids(fields_dto):
        field_ids = [field.field_id for field in fields_dto]
        return field_ids

    @staticmethod
    def _get_task_stages_dto(tasks_details_dto: List[TaskDetailsDTO]):
        tasks_dto = [TaskStageDTO(
            task_id=task.task_id,
            stage_id=task.stage_id
        ) for task in tasks_details_dto]
        return  tasks_dto

    @staticmethod
    def _get_task_and_column_ids(tasks_dtos):
        task_details = [TaskColumnDTO(
            task_id=task_dto.task_id,
            column_id=task_dto.column_id)
            for task_dto in tasks_dtos]

        return task_details
