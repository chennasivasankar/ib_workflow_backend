"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.interactors.dtos import TaskTemplateStagesDTO, \
    TaskSummaryFieldsDTO


class TaskService:

    @property
    def app_interface(self):
        # from ib_tasks.app_interfaces.service_interface import ServiceInterface
        # return ServiceInterface()
        pass

    def get_valid_task_template_ids(
            self, task_template_ids: List[str]) -> List[str]:
        pass

    def get_valid_task_ids(self, task_ids: List[str]) -> List[str]:
        pass

    def validate_task_template_stages_with_id(
            self, task_template_stages: List[TaskTemplateStagesDTO]):
        pass

    def validate_task_task_summary_fields_with_id(
            self, task_summary_fields: List[TaskSummaryFieldsDTO]):
        pass
