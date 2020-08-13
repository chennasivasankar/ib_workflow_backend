"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
from typing import List, Tuple

from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface
from ib_tasks.interactors.storage_interfaces.filter_storage_interface import \
    FilterStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStageIdsDTO
from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO


class GetTaskIdsBasedOnUserFiltersInColumns:

    def __init__(self, filter_storage: FilterStorageInterface,
                 elasticsearch_storage: ElasticSearchStorageInterface):
        self.elasticsearch_storage = elasticsearch_storage
        self.filter_storage = filter_storage

    def get_task_ids_by_applying_filters(
            self, task_details_config: TaskDetailsConfigDTO) -> Tuple[List[TaskStageIdsDTO], int]:
        user_id = task_details_config.user_id
        filter_dtos = self.filter_storage.get_enabled_filters_dto_to_user(
            user_id=user_id
        )
        filtered_task_ids, total_tasks = self.elasticsearch_storage.filter_tasks_with_stage_ids(
            filter_dtos=filter_dtos, task_details_config=task_details_config
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