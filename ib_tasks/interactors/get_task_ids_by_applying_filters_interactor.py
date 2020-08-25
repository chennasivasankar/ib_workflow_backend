"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
from dataclasses import dataclass
from typing import List, Tuple

from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface
from ib_tasks.interactors.storage_interfaces.filter_storage_interface import \
    FilterStorageInterface


@dataclass
class FilterTasksParameter:
    project_id: str
    user_id: str
    limit: int
    offset: int
    stage_ids: List[str]


class GetTaskIdsBasedOnUserFilters:

    def __init__(self, filter_storage: FilterStorageInterface,
                 elasticsearch_storage: ElasticSearchStorageInterface):
        self.elasticsearch_storage = elasticsearch_storage
        self.filter_storage = filter_storage

    def get_task_ids_by_applying_filters(
            self, filter_tasks_parameter: FilterTasksParameter) -> Tuple[List[int], int]:
        self._validations_of_limit_and_offset(
            offset=filter_tasks_parameter.offset,
            limit=filter_tasks_parameter.limit
        )
        filter_dtos = self.filter_storage.get_enabled_filters_dto_to_user(
            user_id=filter_tasks_parameter.user_id,
            project_id=filter_tasks_parameter.project_id
        )
        filtered_task_ids, total_tasks = self.elasticsearch_storage.filter_tasks(
            filter_dtos=filter_dtos,
            offset=filter_tasks_parameter.offset,
            limit=filter_tasks_parameter.limit,
            stage_ids=filter_tasks_parameter.stage_ids
        )
        return filtered_task_ids, total_tasks

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
