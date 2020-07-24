from typing import List

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds, \
    InvalidStageIds
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO


class GetTaskFieldsAndActionsInteractor:
    def __init__(self, storage: TaskStorageInterface,
                 stage_storage: StageStorageInterface):
        self.storage = storage
        self.stage_storage = stage_storage

    def get_task_fields_and_action(self, task_dtos: List[GetTaskDetailsDTO]):
        task_ids = [task.task_id for task in task_dtos]
        stage_ids = [task.stage_id for task in task_dtos]

        valid_task_ids = self.storage.get_valid_task_ids(task_ids)
        invalid_task_ids = [task_id for task_id in task_ids
                            if task_id not in valid_task_ids]
        if invalid_task_ids:
            raise InvalidTaskIds(invalid_task_ids)

        valid_stage_ids = self.stage_storage.get_existing_stage_ids(stage_ids)
        invalid_stage_ids = [stage_id for stage_id in stage_ids
                             if stage_id not in valid_stage_ids]
        if invalid_stage_ids:
            raise InvalidStageIds(invalid_stage_ids)

        task_details_dtos = self.storage.get_task_details(task_dtos)
        return task_details_dtos
