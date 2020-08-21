"""
Created on: 21/08/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.documents.elastic_task import ElasticFieldDTO
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.get_task_dtos import TaskDetailsDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class CreateOrUpdateDataInElasticSearchInteractor:

    def __init__(
            self, field_storage: FieldsStorageInterface,
            task_storage: TaskStorageInterface,
            elasticsearch_storage: ElasticSearchStorageInterface):

        self.elasticsearch_storage = elasticsearch_storage
        self.field_storage = field_storage
        self.task_storage = task_storage

    def create_or_update_task_in_elasticsearch(
            self, task_dto: TaskDetailsDTO, stage_ids: List[str], task_id: int):

        is_task_id_exists = \
            self.elasticsearch_storage.validate_task_id_in_elasticsearch(
                task_id=task_id
            )
        elastic_task_dto = self._get_elastic_task_dto(
            task_dto=task_dto, stage_ids=stage_ids, task_id=task_id)
        if is_task_id_exists:
            self.elasticsearch_storage.update_task(task_dto=elastic_task_dto)
        else:
            elastic_task_id = self.elasticsearch_storage.create_task(
                elastic_task_dto=elastic_task_dto
            )
            self.task_storage.create_elastic_task(
                task_id=task_id, elastic_task_id=elastic_task_id
            )

    def _get_elastic_task_dto(
            self, task_dto: TaskDetailsDTO, stage_ids: List[str], task_id: int):
        fields = self._get_field_dtos_with_exact_data_type(
            task_dto=task_dto
        )
        from ib_tasks.documents.elastic_task import ElasticTaskDTO
        return ElasticTaskDTO(
            template_id=task_dto.task_base_details_dto.template_id,
            task_id=task_id,
            title=task_dto.task_base_details_dto.title,
            fields=fields,
            stages=stage_ids
        )

    def _get_field_dtos_with_exact_data_type(self, task_dto: TaskDetailsDTO):
        field_ids = [
            field.field_id
            for field in task_dto.task_gof_field_dtos
        ]
        field_type_dtos = self.field_storage.get_field_type_dtos(
            field_ids=field_ids)

        field_types_map = {}
        for field_type_dto in field_type_dtos:
            field_types_map[field_type_dto.field_id] = field_type_dto.field_type

        elastic_field_dtos = []
        for field in task_dto.task_gof_field_dtos:
            field_response = self._get_field_response_with_exact_data_type(
                field_response=field.field_response,
                field_type=field_types_map[field.field_id]
            )
            elastic_field_dto = self._get_field_dtos(
                field_id=field.field_id, field_response=field_response
            )
            elastic_field_dtos.append(elastic_field_dto)

        return elastic_field_dtos

    @staticmethod
    def _get_field_dtos(field_id: str, field_response: str) -> ElasticFieldDTO:
        return ElasticFieldDTO(
                field_id=field_id,
                value=field_response
            )

    @staticmethod
    def _get_field_response_with_exact_data_type(
            field_response: str, field_type: FieldTypes):
        if field_type == FieldTypes.FLOAT.value:
            return float(field_response)
        elif field_type == FieldTypes.NUMBER.value:
            return int(field_response)
        return field_response
