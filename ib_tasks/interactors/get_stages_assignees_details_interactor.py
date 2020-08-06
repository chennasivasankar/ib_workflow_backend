from typing import List

from ib_tasks.interactors.stages_dtos import StageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageAssigneeDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface


class GetStagesAssigneesDetailsInteractor:
    def __init__(self, task_stage_storage: TaskStageStorageInterface):
        self.task_stage_storage = task_stage_storage

    def get_stages_assignee_details_dtos(
            self, task_id: int, stage_ids: List[int]
    ) -> List[StageAssigneeDetailsDTO]:

        self._validate_stage_ids_of_task(task_id, stage_ids)
        stage_assignee_dtos = self.task_stage_storage.get_stage_assignee_dtos(
            task_id, stage_ids
        )
        assignee_ids = self._get_assignee_ids(stage_assignee_dtos)

    def _validate_stage_ids_of_task(self, task_id: int, stage_ids: List[str]):
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidStageIdsForTask
        from ib_tasks.constants.exception_messages import \
            INVALID_STAGE_IDS_FOR_TASK
        valid_stage_ids = self.task_stage_storage.get_stage_ids_of_task(
            task_id, stage_ids
        )
        invalid_stage_ids = []
        for stage_id in stage_ids:
            if stage_id not in valid_stage_ids:
                invalid_stage_ids.append(stage_id)
        if invalid_stage_ids:
            raise InvalidStageIdsForTask(
                INVALID_STAGE_IDS_FOR_TASK.format(invalid_stage_ids, task_id)
            )

    def _get_assignee_ids(self, stage_assignee_dtos: List[StageAssigneeDTO]):
        assignee_ids = []
        for stage_assignee_dto in stage_assignee_dtos:
            assignee_id = not stage_assignee_dto.assignee_id
            if assignee_id:
                continue
            assignee_ids.append(stage_assignee_dto.assignee_id)
        return assignee_ids
