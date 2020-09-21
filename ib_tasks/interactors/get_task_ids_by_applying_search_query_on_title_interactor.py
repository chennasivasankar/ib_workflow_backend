"""
Created on: 03/09/20
Author: Pavankumar Pamuru

"""
from dataclasses import dataclass
from typing import List, Optional

from ib_tasks.documents.elastic_task import QueryTasksDTO
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface, ApplyFilterDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldTypeDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.filter_storage_interface import \
    FilterStorageInterface
from ib_tasks.interactors.task_dtos import SearchQueryDTO


@dataclass
class SearchTasksParameter:
    project_id: str
    user_id: str
    limit: int
    offset: int
    stage_ids: List[str]
    search_query: Optional[str]
    apply_filters_dto: List[ApplyFilterDTO]


class GetTaskIdsBasedOnUserSearchQuery(ValidationMixin):

    def __init__(self, filter_storage: FilterStorageInterface,
                 field_storage: FieldsStorageInterface,
                 elasticsearch_storage: ElasticSearchStorageInterface):
        self.field_storage = field_storage
        self.elasticsearch_storage = elasticsearch_storage
        self.filter_storage = filter_storage

    def get_task_ids_by_applying_search_query(
            self, search_query_dto: SearchQueryDTO, stage_ids: List[str],
            apply_filters_dto: List[ApplyFilterDTO]) -> QueryTasksDTO:
        user_id = search_query_dto.user_id
        project_id = search_query_dto.project_id
        self._validations_of_limit_and_offset(
            offset=search_query_dto.offset,
            limit=search_query_dto.limit
        )
        self._validate_project_data(project_id=project_id, user_id=user_id)
        filter_dtos = self.filter_storage.get_enabled_filters_dto_to_user(
            user_id=search_query_dto.user_id,
            project_id=search_query_dto.project_id
        )
        advanced_filter_dtos = apply_filters_dto
        apply_filters_dto = apply_filters_dto + filter_dtos
        field_ids = [filter_dto.field_id for filter_dto in apply_filters_dto]
        field_type_dtos = self.field_storage.get_field_type_dtos(
            field_ids=field_ids)
        self._validate_conditions_for_values(
            field_type_dtos=field_type_dtos,
            filter_dtos=advanced_filter_dtos
        )

        query_tasks_dto = self.elasticsearch_storage.search_tasks(
            search_query_dto=search_query_dto,
            apply_filter_dtos=apply_filters_dto,
            stage_ids=stage_ids,
            field_type_dtos=field_type_dtos
        )
        return query_tasks_dto

    @staticmethod
    def _validations_of_limit_and_offset(offset: int, limit: int):
        if limit < 1:
            from ib_tasks.exceptions.fields_custom_exceptions import \
                LimitShouldBeGreaterThanZeroException
            raise LimitShouldBeGreaterThanZeroException

        if offset < 0:
            from ib_tasks.exceptions.fields_custom_exceptions import \
                OffsetShouldBeGreaterThanZeroException
            raise OffsetShouldBeGreaterThanZeroException

    def _validate_project_data(self, project_id: str, user_id: str):

        self.validate_given_project_ids(project_ids=[project_id])
        self.validate_if_user_is_in_project(
            project_id=project_id, user_id=user_id
        )

    @staticmethod
    def _validate_conditions_for_values(
            field_type_dtos: List[FieldTypeDTO],
            filter_dtos: List[ApplyFilterDTO]):
        field_types_map = {}
        for field_type_dto in field_type_dtos:
            field_types_map[field_type_dto.field_id] = field_type_dto.field_type
        from ib_tasks.constants.constants import NUMERIC_OPERATORS, STRING_OPERATORS
        for filter_dto in filter_dtos:
            field_type = field_types_map[filter_dto.field_id]
            from ib_tasks.constants.enum import FieldTypes
            is_invalid_filter_string = field_type != FieldTypes.NUMBER.value \
                                and field_type != FieldTypes.FLOAT.value \
                                and filter_dto.operator in NUMERIC_OPERATORS
            is_invalid_filter = field_type == FieldTypes.NUMBER.value \
                                or field_type == FieldTypes.FLOAT.value \
                                and filter_dto.operator in STRING_OPERATORS
            if is_invalid_filter or is_invalid_filter_string:
                from ib_tasks.exceptions.filter_exceptions import \
                    InvalidFilterCondition
                raise InvalidFilterCondition(condition=filter_dto.operator)
