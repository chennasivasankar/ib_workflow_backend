"""
Created on: 24/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface
from ib_tasks.interactors.storage_interfaces.filter_storage_interface import \
    FilterStorageInterface
from ib_tasks.models import Stage

from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO, TaskIdsDTO


class InvalidOffsetValue(Exception):
    pass


class InvalidLimitValue(Exception):
    pass


class GetTaskIdsInteractor:
    def __init__(
            self, stage_storage: StageStorageInterface,
            task_storage: TaskStorageInterface,
            filter_storage: FilterStorageInterface,
            elasticsearch_storage: ElasticSearchStorageInterface):
        self.elasticsearch_storage = elasticsearch_storage
        self.filter_storage = filter_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage

    def get_task_ids(self, task_details_configs: List[TaskDetailsConfigDTO]):
        self._validate_given_data(task_details_configs=task_details_configs)

        total_task_ids_dtos = []
        # TODO need optimize db hits
        for task_details_config in task_details_configs:
            task_ids_dto = self._get_task_ids_dto(
                task_details_config
            )
            total_task_ids_dtos.append(task_ids_dto)
        return total_task_ids_dtos

    def _validate_given_data(self, task_details_configs: List[TaskDetailsConfigDTO]):
        for task_details_config in task_details_configs:
            if task_details_config.offset < 0:
                raise InvalidOffsetValue
            if task_details_config.limit < 1:
                raise InvalidLimitValue
        total_stage_ids = []
        for task_details_config in task_details_configs:
            total_stage_ids += task_details_config.stage_ids
        valid_stage_ids = self.stage_storage.get_existing_stage_ids(
            stage_ids=total_stage_ids
        )
        invalid_stage_ids = [
            stage_id for stage_id in total_stage_ids
            if stage_id not in valid_stage_ids
        ]
        if invalid_stage_ids:
            from ib_tasks.exceptions.stage_custom_exceptions import \
                InvalidStageIdsListException
            raise InvalidStageIdsListException(
                invalid_stage_ids=invalid_stage_ids)

    def _get_task_ids_dto(self, task_details_config: TaskDetailsConfigDTO):

        from ib_tasks.interactors.get_task_ids_by_applying_filters_with_stage_ids import \
            GetTaskIdsBasedOnUserFiltersInColumns
        filtered_task_ids_interactor = GetTaskIdsBasedOnUserFiltersInColumns(
            filter_storage=self.filter_storage,
            elasticsearch_storage=self.elasticsearch_storage
        )

        task_stage_dtos, total_count = filtered_task_ids_interactor.get_task_ids_by_applying_filters(
            user_id=task_details_config.user_id, limit=task_details_config.limit,
            offset=task_details_config.offset, stage_ids=task_details_config.stage_ids
        )

        return TaskIdsDTO(
            unique_key=task_details_config.unique_key,
            task_stage_ids=task_stage_dtos,
            total_tasks=total_count
        )
