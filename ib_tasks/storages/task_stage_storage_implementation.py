from typing import List

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.stages_dtos import TaskStageHistoryDTO, \
    StageMinimalDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskStageAssigneeDTO, CurrentStageDetailsDTO, AssigneeCurrentTasksCountDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface
    TaskStageStorageInterface, TaskStageAssigneeIdDTO
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
from ib_tasks.models import CurrentTaskStage, Stage
from ib_tasks.models.task_stage_history import TaskStageHistory
from ib_tasks.models import CurrentTaskStage, Task, TaskStageHistory, \
    StagePermittedRoles, Stage
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
                assignee_id=task_stage_obj.assignee_id,
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

    def validate_task_id(self, task_id: int) -> str:
        try:
            task_obj = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            raise InvalidTaskIdException(task_id=task_id)
        return task_obj.task_display_id

    def get_task_current_stage_ids(self, task_id: int) -> List[int]:
        stage_ids = CurrentTaskStage.objects.filter(
            task_id=task_id).values_list('stage_id', flat=True)
        stage_ids = list(stage_ids)
        return stage_ids

    def get_stage_details_dtos(
            self, stage_ids: List[int]
    ) -> List[CurrentStageDetailsDTO]:

        stage_details_dict = Stage.objects.filter(id__in=stage_ids).values(
            'stage_id', 'display_name')
        stage_details_dtos = [
            CurrentStageDetailsDTO(
                stage_id=stage_detail_dict['stage_id'],
                stage_display_name=stage_detail_dict['display_name']
            )
            for stage_detail_dict in stage_details_dict
        ]
        return stage_details_dtos

    def is_user_has_permission_for_at_least_one_stage(
            self, stage_ids: List[int], user_roles: List[str]
    ) -> bool:
        is_user_has_permissions = StagePermittedRoles.objects.filter(
            stage_id__in=stage_ids, role_id__in=user_roles
        ).exists()
        return is_user_has_permissions

    def get_count_of_tasks_assigned_for_each_user(
            self, db_stage_ids: List[int],
            task_ids: List[int], user_ids: List[str]) -> List[
        AssigneeCurrentTasksCountDTO]:
        from django.db.models import Count
        assignee_with_count_objs = list(TaskStageHistory.objects.filter(
            task_id__in=task_ids, stage_id__in=db_stage_ids,
            assignee_id__in=user_ids, left_at=None).values(
            'assignee_id').annotate(
            tasks_count=Count('assignee_id')).order_by('tasks_count'))
        assignee_with_current_tasks_count_dtos = [AssigneeCurrentTasksCountDTO(
            assignee_id=assignee_with_count_obj['assignee_id'],
            tasks_count=assignee_with_count_obj['tasks_count']) for
            assignee_with_count_obj in
            assignee_with_count_objs]
        return assignee_with_current_tasks_count_dtos

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
