import datetime
from typing import List

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskStageAssigneeDTO, CurrentStageDetailsDTO, TaskIdWithDbStageIdsDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface
from ib_tasks.models import CurrentTaskStage, Task, TaskStageHistory, \
    StagePermittedRoles, Stage


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

    def update_task_stage_having_assignees_with_left_at_status(
            self, task_id_with_db_stage_ids_dto:
            TaskIdWithDbStageIdsDTO):
        task_id = task_id_with_db_stage_ids_dto.task_id
        stage_ids = task_id_with_db_stage_ids_dto.db_stage_ids
        task_stage_objs_having_assignees = TaskStageHistory.objects.filter(
            task_id=task_id,
            stage_id__in=stage_ids).exclude(assignee_id=None)
        for each_task_stage_obj in task_stage_objs_having_assignees:
            each_task_stage_obj.left_at = datetime.datetime.now()
        TaskStageHistory.objects.bulk_update(
            task_stage_objs_having_assignees, ['left_at']
        )
