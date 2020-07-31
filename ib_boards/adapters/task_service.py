"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.interactors.dtos import TaskTemplateStagesDTO, \
    TaskSummaryFieldsDTO, TaskStatusDTO, TaskDTO, ColumnTaskIdsDTO
from ib_boards.tests.factories.storage_dtos import TaskActionsDTOFactory, \
    TaskFieldsDTOFactory
from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO, \
    GetTaskDetailsDTO


class TaskService:

    @property
    def interface(self):
        from ib_tasks.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    @staticmethod
    def get_valid_task_template_ids(
            task_template_ids: List[str]) -> List[str]:
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

    def get_task_ids_for_stage_ids(
            self, task_config_dtos: List[TaskDetailsConfigDTO]) \
            -> List[ColumnTaskIdsDTO]:
        task_ids_dtos = self.interface.get_task_ids_for_the_stages(
            task_config_dtos=task_config_dtos
        )
        column_task_ids_dtos = [
            ColumnTaskIdsDTO(
                unique_key=task_ids_dto.unique_key,
                task_stage_ids=task_ids_dto.task_stage_ids,
                total_tasks=task_ids_dto.total_tasks
            )
            for task_ids_dto in task_ids_dtos
        ]
        return column_task_ids_dtos

    def get_task_complete_details(self,
                                  task_stage_ids: List[GetTaskDetailsDTO]):
        tasks_complete_details_dtos = self.interface.get_task_details(
            task_dtos=task_stage_ids
        )
        from ib_boards.interactors.presenter_interfaces.presenter_interface import \
            TaskCompleteDetailsDTO
        tasks_details_dtos = []
        for tasks_complete_details_dto in tasks_complete_details_dtos:
            tasks_details_dtos.append(
                TaskCompleteDetailsDTO(
                    task_id=tasks_complete_details_dto.task_id,
                    stage_id=tasks_complete_details_dto.stage_id,
                    field_dtos=tasks_complete_details_dto.field_dtos,
                    action_dtos=tasks_complete_details_dto.action_dtos
                )
            )

        return tasks_details_dtos