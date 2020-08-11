from typing import List

from ib_tasks.interactors.stages_dtos import TaskStageHistoryDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskStageAssigneeDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface
from ib_tasks.models import CurrentTaskStage
from ib_tasks.models.task_stage_history import TaskStageHistory


class TaskStageStorageImplementation(TaskStageStorageInterface):

    def get_task_stage_dtos(self, task_id: int) -> List[TaskStageHistoryDTO]:
        task_stage_history_objs = \
            TaskStageHistory.objects.filter(task_id=task_id)

        return [
            TaskStageHistoryDTO(
                log_id=task_stage_obj.id,
                task_id=task_stage_obj.task_id,
                stage_id=task_stage_obj.stage_id,
                started_at=task_stage_obj.joined_at,
                left_at=task_stage_obj.left_at,
                assignee_id=task_stage_obj.task_stage_assignee_id,
                stage_duration=None
            )
            for task_stage_obj in task_stage_history_objs
        ]

    def get_valid_stage_ids_of_task(self, task_id: int,
                                    stage_ids: List[int]) -> List[int]:
        valid_stage_ids = list(
            CurrentTaskStage.objects.filter(
                task_id=task_id, stage_id__in=stage_ids
            ).values_list('stage_id', flat=True)
        )
        return valid_stage_ids

    def get_stage_assignee_dtos(
            self, task_id: int, stage_ids: List[int]
    ) -> List[TaskStageAssigneeDTO]:

        task_stage_objs = CurrentTaskStage.objects.filter(
            task_id=task_id, stage_id__in=stage_ids
        )
        task_stage_assignee_dtos = [
            TaskStageAssigneeDTO(
                task_stage_id=task_stage_obj.id,
                stage_id=task_stage_obj.stage_id,
                assignee_id=task_stage_obj.assignee_id
            )
            for task_stage_obj in task_stage_objs
        ]
        return task_stage_assignee_dtos
