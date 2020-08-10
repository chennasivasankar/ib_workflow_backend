"""
Created on: 10/08/20
Author: Pavankumar Pamuru

"""
from typing import List, Tuple

from ib_boards.constants.enum import ViewType
from ib_boards.interactors.dtos import ColumnTaskIdsDTO, FieldDTO, ActionDTO, \
    TaskStageColorDTO
from ib_boards.interactors.storage_interfaces.dtos import ColumnStageIdsDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetColumnTasksInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_column_tasks_with_column_ids(
            self, column_ids: List[str], user_id, view_type: ViewType, limit: int, offset: int):
        column_stage_dtos = self.storage.get_columns_stage_ids(
            column_ids=column_ids
        )
        task_ids_stages_dtos = self._get_task_ids_for_given_stages(
            column_stage_dtos=column_stage_dtos)
        task_field_dtos, task_action_dtos, task_stage_color_dtos = \
            self._get_tasks_complete_details(
                task_ids_stages_dtos=task_ids_stages_dtos,
                user_id=user_id,
                view_type=view_type
            )

        return task_field_dtos, task_action_dtos, task_ids_stages_dtos, task_stage_color_dtos

    @staticmethod
    def _get_tasks_complete_details(
            task_ids_stages_dtos: List[ColumnTaskIdsDTO],
            user_id: str,
            view_type: ViewType) \
            -> Tuple[List[FieldDTO], List[ActionDTO], List[TaskStageColorDTO]]:
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
        return service_adapter.task_service.get_task_complete_details(
            task_details_dtos, user_id=user_id, view_type=view_type)

    def _get_task_ids_for_given_stages(
            self, column_stage_dtos: List[ColumnStageIdsDTO]) -> List[ColumnTaskIdsDTO]:
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO
        task_config_dto = [
            TaskDetailsConfigDTO(
                unique_key=column_stage_dto.column_id,
                stage_ids=column_stage_dto.stage_ids,
                limit=10,
                offset=20
            )
            for column_stage_dto in column_stage_dtos
        ]
        filtered_task_ids = self._get_filtered_task_ids(column_stage_dtos=column_stage_dtos)
        task_ids_details = service_adapter.task_service.get_task_ids_for_stage_ids(
            task_config_dtos=task_config_dto
        )
        return task_ids_details

    @staticmethod
    def _get_filtered_task_ids(column_stage_dtos):
        return 1
