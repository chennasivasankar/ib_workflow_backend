from typing import List

from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskStageAssigneeDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface
from ib_tasks.models import TaskStage


class TaskStageStorageImplementation(TaskStageStorageInterface):

    def get_valid_stage_ids_of_task(self, task_id: int,
                                    stage_ids: List[int]) -> List[int]:
        valid_stage_ids = list(
            TaskStage.objects.filter(
                task_id=task_id, stage_id__in=stage_ids
            ).values_list('stage_id', flat=True)
        )
        return valid_stage_ids

    def get_stage_assignee_dtos(
            self, task_id: int, stage_ids: List[int]
    ) -> List[TaskStageAssigneeDTO]:

        task_stage_objs = TaskStage.objects.filter(
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
