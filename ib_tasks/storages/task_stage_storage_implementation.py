from typing import List

from ib_tasks.interactors.stages_dtos import TaskStageHistoryDTO, StageMinimalDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskStageAssigneeDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface, TaskStageAssigneeIdDTO
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
from ib_tasks.models import CurrentTaskStage, Stage
from ib_tasks.models.task_stage_history import TaskStageHistory
from django.db.models import Q


class TaskStageStorageImplementation(TaskStageStorageInterface):

    def get_stage_details(self, stage_ids: List[int]) -> List[StageMinimalDTO]:

        stage_objs = Stage.objects.filter(id__in=stage_ids)

        return [
            StageMinimalDTO(
                stage_id=stage_obj.id,
                name=stage_obj.display_name,
                color=stage_obj.stage_color
            )
            for stage_obj in stage_objs
        ]

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

    def get_stage_assignee_id_dtos(
            self, task_stage_dtos: List[GetTaskDetailsDTO]) -> List[TaskStageAssigneeIdDTO]:
        q = None
        for counter, item in enumerate(task_stage_dtos):
            current_queue = Q(
                task_id=item.task_id, stage__stage_id=item.stage_id
            )
            if counter == 0:
                q = current_queue
            q = q | current_queue
        if q is None:
            return []
        task_stage_objects = CurrentTaskStage.objects.filter(q).values(
            'task_id', 'stage__stage_id', 'assignee_id'
        )
        return [
            TaskStageAssigneeIdDTO(
                task_id=task_stage_object['task_id'],
                stage_id=task_stage_object['stage_id'],
                assignee_id=task_stage_object['assignee_id']
            )
            for task_stage_object in task_stage_objects
        ]
