"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.interactors.dtos import TaskTemplateStagesDTO, \
    TaskSummaryFieldsDTO, TaskStatusDTO, TaskDTO
from ib_boards.tests.factories.storage_dtos import TaskActionsDTOFactory, \
    TaskFieldsDTOFactory


class TaskService:

    @property
    def app_interface(self):
        # from ib_tasks.app_interfaces.service_interface import ServiceInterface
        # return ServiceInterface()
        return

    def get_valid_task_template_ids(
            self, task_template_ids: List[str]) -> List[str]:
        return task_template_ids

    def validate_task_ids(self, task_ids: List[str]):
        pass

    def validate_stage_ids(self, stage_ids: List[str]):
        pass

    def validate_task_template_stages_with_id(
            self, task_template_stages: List[TaskTemplateStagesDTO]):
        pass

    def validate_task_task_summary_fields_with_id(
            self, task_summary_fields: List[TaskSummaryFieldsDTO]):
        pass

    def get_stage_display_logics(self, stage_ids: List[str]) -> List[str]:
        pass

    def get_task_ids_with_respective_stages(
            self, task_status_dtos: List[TaskStatusDTO]) -> List[str]:
        pass

    @staticmethod
    def get_task_details_dtos(task_dtos: List[TaskDTO],
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
