"""
Created on: 24/07/20
Author: Pavankumar Pamuru

"""


from typing import List

from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStageIdsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class GetTaskIdsInteractor:
    def __init__(
            self, stage_storage: StageStorageInterface,
            task_storage: TaskStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage

    def get_task_ids(self, stage_ids: List[TaskStageIdsDTO]):
        total_stage_ids = []
        for stage_id in stage_ids:
            total_stage_ids += stage_id
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

        stage_task_ids_dtos = []
        # TODO need to optimise the db hits
        for stage_id in stage_ids:
            stage_task_ids_dto_list = self.task_storage.get_task_ids_for_the_stage_ids(
                stage_ids=stage_id
            )
            stage_task_ids_dtos.append(stage_task_ids_dto_list)
        return stage_task_ids_dtos
