"""
Created on: 24/07/20
Author: Pavankumar Pamuru

"""
from typing import List
from ib_tasks.models import Stage

from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO, TaskIdsDTO


class GetTaskIdsInteractor:
    def __init__(
            self, stage_storage: StageStorageInterface,
            task_storage: TaskStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage

    def get_task_ids(self, task_details_configs: List[TaskDetailsConfigDTO]):

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
                InvalidStageIds
            raise InvalidStageIds(stage_ids=invalid_stage_ids)

        total_task_ids_dtos = []
        # TODO need optimize db hits
        for task_details_config in task_details_configs:
            task_ids_dto = self._get_task_ids_dto(
                task_details_config
            )
            total_task_ids_dtos.append(task_ids_dto)
        return total_task_ids_dtos

    def _get_task_ids_dto(self, task_details_config: TaskDetailsConfigDTO):
        task_ids_dtos, total_count = self.task_storage.get_task_ids_for_the_stage_ids(
            stage_ids=task_details_config.stage_ids,
            offset=task_details_config.offset,
            limit=task_details_config.limit
        )
        return TaskIdsDTO(
            unique_key=task_details_config.unique_key,
            task_stage_ids=task_ids_dtos,
            total_tasks=total_count
        )
