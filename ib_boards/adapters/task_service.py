"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.adapters.dtos import TaskStatusDTO


class TaskService:

    @property
    def app_interface(self):
        # from ib_tasks.app_interfaces.service_interface import ServiceInterface
        # return ServiceInterface()
        pass

    def validate_task_template_ids(self, task_template_ids: List[str]):
        pass

    def validate_task_ids(self, task_ids: List[str]):
        pass

    def validate_task_template_stages_with_id(
            self, task_template_stages: List):
        pass

    def validate_task_task_summary_fields_with_id(
            self, task_summary_fields: List):
        pass

    def get_stage_display_logics(self, stage_ids: List[str]) -> List[str]:
        pass

    def get_task_ids_and_number_total_tasks(
            self, task_status_dtos: List[TaskStatusDTO]) -> (List[str], int):
        pass
