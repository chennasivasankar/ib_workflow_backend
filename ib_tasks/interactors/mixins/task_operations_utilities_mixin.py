from typing import List, Optional

from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
    TaskGoFFieldDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskGoFWithTaskIdDTO, TaskGoFDetailsDTO
from ib_tasks.interactors.task_dtos import GoFFieldsDTO


class TaskOperationsUtilitiesMixin:

    @staticmethod
    def _prepare_task_gof_dtos(
            task_id: int, gof_field_dtos: List[GoFFieldsDTO]
    ) -> List[TaskGoFWithTaskIdDTO]:
        task_gof_dtos = [
            TaskGoFWithTaskIdDTO(
                task_id=task_id, gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order)
            for gof_fields_dto in gof_field_dtos
        ]
        return task_gof_dtos

    def _prepare_task_gof_fields_dtos(
            self, gof_fields_dtos: List[GoFFieldsDTO],
            task_gof_details_dtos: List[TaskGoFDetailsDTO]
    ) -> List[TaskGoFFieldDTO]:
        task_gof_field_dtos = []
        for gof_fields_dto in gof_fields_dtos:
            task_gof_id = self._get_task_gof_id_for_field_in_task_gof_details(
                gof_fields_dto.gof_id, gof_fields_dto.same_gof_order,
                task_gof_details_dtos
            )
            task_gof_field_dtos += [
                TaskGoFFieldDTO(
                    field_id=field_values_dto.field_id,
                    field_response=field_values_dto.field_response,
                    task_gof_id=task_gof_id
                )
                for field_values_dto in gof_fields_dto.field_values_dtos
            ]
        return task_gof_field_dtos

    @staticmethod
    def _get_task_gof_id_for_field_in_task_gof_details(
            gof_id: str, same_gof_order: int,
            task_gof_details_dtos: List[TaskGoFDetailsDTO]
    ) -> Optional[int]:
        for task_gof_details_dto in task_gof_details_dtos:
            gof_matched = (
                    task_gof_details_dto.gof_id == gof_id and
                    task_gof_details_dto.same_gof_order == same_gof_order
            )
            if gof_matched:
                return task_gof_details_dto.task_gof_id
        return
