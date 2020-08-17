"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List, Tuple

from ib_boards.constants.enum import ViewType
from ib_boards.interactors.dtos import TaskTemplateStagesDTO, \
    TaskSummaryFieldsDTO, TaskStatusDTO, FieldDTO, ColumnTaskIdsDTO, ActionDTO, \
    TaskStageDTO, StageAssigneesDTO, AssigneesDTO
from ib_boards.tests.factories.storage_dtos import TaskActionsDTOFactory, \
    TaskFieldsDTOFactory
from ib_tasks.adapters.dtos import AssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStagesDTO
from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO, \
    GetTaskDetailsDTO


class InvalidStagesForTemplate(Exception):
    def __init__(self, invalid_stages_task_template_ids: List[TaskStagesDTO]):
        self.invalid_stages_task_template_ids = \
            invalid_stages_task_template_ids

    def __str__(self):
        return self.invalid_stages_task_template_ids


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

        template_stages = []
        for task_template_stage in task_template_stages:
            for stage_id in task_template_stage.stages:
                from ib_tasks.interactors.storage_interfaces.stage_dtos import \
                    TaskStagesDTO
                template_stages.append(TaskStagesDTO(
                    task_template_id=task_template_stage.task_template_id,
                    stage_id=stage_id
                ))
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidStagesTaskTemplateId
        try:
            self.interface.validate_stage_ids_with_template_id(
                template_stages=template_stages
            )
        except InvalidStagesTaskTemplateId as error:
            raise InvalidStagesForTemplate(
                invalid_stages_task_template_ids=error.invalid_stages_task_template_ids
            )

    def validate_task_task_summary_fields_with_id(
            self, task_summary_fields: List[TaskSummaryFieldsDTO]):
        pass

    def get_stage_display_logics(self, stage_ids: List[str]) -> List[str]:
        pass

    def get_task_ids_with_respective_stages(
            self, task_status_dtos: List[TaskStatusDTO]) -> List[str]:
        pass

    @staticmethod
    def get_task_details_dtos(task_dtos: List[FieldDTO],
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

    def get_task_complete_details(
            self, task_stage_ids: List[GetTaskDetailsDTO],
            user_id: str, view_type: ViewType) \
            -> Tuple[List[FieldDTO], List[ActionDTO], List[TaskStageDTO]]:
        tasks_complete_details_dtos = self.interface.get_task_details(
            task_dtos=task_stage_ids, user_id=user_id, view_type=view_type
        )
        tasks_dtos = []
        action_dtos = []
        task_stage_color_dtos = []
        for tasks_complete_details_dto in tasks_complete_details_dtos:
            tasks_dtos += self._convert_task_fields_to_field_dtos(
                task_id=tasks_complete_details_dto.task_id,
                stage_id=tasks_complete_details_dto.stage_id,
                field_dtos=tasks_complete_details_dto.field_dtos
            )
            action_dtos += self._convert_task_action_to_action_dtos(
                task_id=tasks_complete_details_dto.task_id,
                stage_id=tasks_complete_details_dto.stage_id,
                action_dtos=tasks_complete_details_dto.action_dtos
            )
            task_stage_color_dtos.append(
                TaskStageDTO(
                    task_id=tasks_complete_details_dto.task_id,
                    stage_id=tasks_complete_details_dto.stage_id,
                    db_stage_id=tasks_complete_details_dto.db_stage_id,
                    display_name=tasks_complete_details_dto.display_name,
                    stage_color=tasks_complete_details_dto.stage_color)
            )

        return tasks_dtos, action_dtos, task_stage_color_dtos

    @staticmethod
    def _convert_task_fields_to_field_dtos(
            task_id: int, stage_id: str, field_dtos: List) -> List[FieldDTO]:
        return [
            FieldDTO(
                task_id=task_id,
                field_id=field_dto.field_id,
                field_type=field_dto.field_type,
                key=field_dto.key,
                value=field_dto.value,
                stage_id=stage_id
            )
            for field_dto in field_dtos
        ]

    @staticmethod
    def _convert_task_action_to_action_dtos(
            task_id: int, stage_id: str, action_dtos: List) -> List[ActionDTO]:
        return [
            ActionDTO(
                action_id=action_dto.action_id,
                name=action_dto.name,
                button_text=action_dto.button_text,
                button_color=action_dto.button_color,
                task_id=task_id,
                stage_id=stage_id,
                action_type=action_dto.action_type,
                transition_template_id=action_dto.transition_template_id
            )
            for action_dto in action_dtos
        ]

    def get_tasks_assignees_details(
            self, task_stage_ids: List[GetTaskDetailsDTO]) -> List[StageAssigneesDTO]:

        stage_assignees_dtos = self.interface.get_assignees_for_task_stages(
            task_stage_dtos=task_stage_ids
        )
        return [
            StageAssigneesDTO(
                task_id=stage_assignees_dto.task_id,
                stage_id=stage_assignees_dto.stage_id,
                assignees_details=self._get_assignee_details_dto(
                    stage_assignees_dto.assignee_details
                )
            )
            for stage_assignees_dto in stage_assignees_dtos
        ]

    @staticmethod
    def _get_assignee_details_dto(assignee_details: AssigneeDetailsDTO) -> AssigneesDTO:
        return AssigneesDTO(
            assignee_id=assignee_details.assignee_id,
            name=assignee_details.name,
            profile_pic_url=assignee_details.profile_pic_url
        )
