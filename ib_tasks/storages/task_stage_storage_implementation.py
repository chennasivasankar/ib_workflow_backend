from typing import List

from django.db.models import Count

from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskStageAssigneeDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface
from ib_tasks.models import CurrentTaskStage, TaskStageHistory


class TaskStageStorageImplementation(TaskStageStorageInterface):

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
        task_stage_objs = TaskStageHistory.objects.filter(
            task_id=task_id, stage_id__in=stage_ids
        ).values('id', 'stage_id', 'assignee_id')
        task_stage_assignee_dtos = [
            TaskStageAssigneeDTO(
                task_stage_id=task_stage_obj['id'],
                stage_id=task_stage_obj['stage_id'],
                assignee_id=task_stage_obj['assignee_id']
            )
            for task_stage_obj in task_stage_objs
        ]
        return task_stage_assignee_dtos

    def get_count_of_tasks_assigned_for_each_user(
            self, db_stage_ids: List[int],
            task_ids: List[int], permitted_user_ids: List[str]):
        assignee_with_count_objs = list(TaskStageHistory.objects.filter(
            task_id=task_ids, stage_id__in=db_stage_ids,
            assignee_id__in=permitted_user_ids).values('assignee_id').annotate(
            assignees_count=Count('assignee_id')))
