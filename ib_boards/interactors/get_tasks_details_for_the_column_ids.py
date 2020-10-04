"""
Created on: 10/08/20
Author: Pavankumar Pamuru

"""
from dataclasses import dataclass
from typing import List, Tuple, Optional

from ib_boards.constants.enum import ViewType
from ib_boards.interactors.dtos import ColumnTaskIdsDTO, FieldDTO, ActionDTO, \
    TaskStageDTO, StageAssigneesDTO, TaskCommonDetailsDTO, \
    TaskCompleteDetailsDTO, TaskBaseAndCompleteDetailsDTO
from ib_boards.interactors.storage_interfaces.dtos import ColumnStageIdsDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskBaseDetailsDTO


@dataclass
class ColumnsTasksParametersDTO:
    column_ids: List[str]
    user_id: str
    limit: int
    offset: int
    project_id: str
    view_type: ViewType
    search_query: Optional[str]


class GetColumnsTasksDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_column_tasks_with_column_ids(
            self, column_tasks_parameters: ColumnsTasksParametersDTO) \
            -> TaskBaseAndCompleteDetailsDTO:
        limit = column_tasks_parameters.limit
        offset = column_tasks_parameters.offset
        user_id = column_tasks_parameters.user_id
        column_ids = column_tasks_parameters.column_ids
        view_type = column_tasks_parameters.view_type
        project_id = column_tasks_parameters.project_id
        search_query = column_tasks_parameters.search_query
        self._validate_offset_value(offset=offset)
        self._validate_limit_value(limit=limit)
        column_stage_dtos = self.get_column_stage_dtos(column_ids)
        task_ids_stages_dtos = self._get_task_ids_for_given_stages(
            column_stage_dtos=column_stage_dtos,
            limit=limit,
            offset=offset,
            user_id=user_id,
            project_id=project_id,
            search_query=search_query
        )
        tasks_complete_details = \
            self._get_tasks_complete_details(
                task_ids_stages_dtos=task_ids_stages_dtos,
                user_id=user_id,
                view_type=view_type,
                project_id=project_id
            )

        return tasks_complete_details

    def get_column_stage_dtos(self, column_ids: List[str]):
        column_stage_dtos = self.storage.get_columns_stage_ids(
            column_ids=column_ids
        )
        return column_stage_dtos

    @staticmethod
    def _validate_offset_value(offset: int):
        if offset < 0:
            from ib_boards.exceptions.custom_exceptions import \
                InvalidOffsetValue
            raise InvalidOffsetValue
        return

    @staticmethod
    def _validate_limit_value(limit: int):
        if limit <= 0:
            from ib_boards.exceptions.custom_exceptions import InvalidLimitValue
            raise InvalidLimitValue

    @staticmethod
    def _get_tasks_complete_details(
            task_ids_stages_dtos: List[ColumnTaskIdsDTO],
            user_id: str, view_type: ViewType, project_id: str
    ) -> TaskBaseAndCompleteDetailsDTO:
        task_details_dtos = []
        for task_ids_stages_dto in task_ids_stages_dtos:
            for stage_id_dto in task_ids_stages_dto.task_stage_ids:
                from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
                task_details_dtos.append(
                    GetTaskDetailsDTO(
                        task_id=stage_id_dto.task_id,
                        stage_id=stage_id_dto.stage_id
                    )
                )
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        assignees_dtos = service_adapter.task_service.get_tasks_assignees_details(
            task_stage_ids=task_details_dtos, project_id=project_id
        )
        task_field_dtos, task_action_dtos, task_stage_color_dtos = \
            service_adapter.task_service.get_task_complete_details(
                task_details_dtos, user_id=user_id, view_type=view_type
            )
        task_ids = sorted(list({
            task_details_dto.task_id
            for task_details_dto in task_details_dtos
        }))
        task_base_details_dtos = service_adapter.task_service.get_task_base_details(
            task_ids=task_ids
        )
        return TaskBaseAndCompleteDetailsDTO(
            task_field_dtos=task_field_dtos,
            task_action_dtos=task_action_dtos,
            task_stage_color_dtos=task_stage_color_dtos,
            column_task_ids=task_ids_stages_dtos,
            assignees_dtos=assignees_dtos,
            task_base_details_dtos=task_base_details_dtos
        )

    @staticmethod
    def _get_task_ids_for_given_stages(
            column_stage_dtos: List[ColumnStageIdsDTO],
            limit: int, offset: int, user_id: str, search_query: str,
            project_id: str) -> List[ColumnTaskIdsDTO]:
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO
        task_config_dto = [
            TaskDetailsConfigDTO(
                unique_key=column_stage_dto.column_id,
                stage_ids=column_stage_dto.stage_ids,
                limit=limit,
                offset=offset,
                user_id=user_id,
                project_id=project_id,
                search_query=search_query
            )
            for column_stage_dto in column_stage_dtos
        ]
        task_ids_details = service_adapter.task_service.get_task_ids_for_stage_ids(
            task_config_dtos=task_config_dto
        )
        return task_ids_details
