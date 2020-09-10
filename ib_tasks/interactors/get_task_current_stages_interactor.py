from typing import Union, List

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface
from ib_tasks.interactors.task_dtos import TaskCurrentStageDetailsDTO


class GetTaskCurrentStagesInteractor:
    def __init__(self, task_stage_storage: TaskStageStorageInterface):
        self.task_stage_storage = task_stage_storage

    def get_task_current_stages_details(
            self, task_id: int, user_id: str
    ):
        task_display_id = self._validate_task_id(task_id)
        stage_ids = self.task_stage_storage.get_task_current_stage_ids(task_id)
        stage_details_dtos = self.task_stage_storage.get_stage_details_dtos(
            stage_ids
        )
        user_roles = self._get_user_roles(user_id)
        is_user_has_permission = \
            self.task_stage_storage\
                .is_user_has_permission_for_at_least_one_stage(
                stage_ids, user_roles)
        task_current_stage_details_dto = TaskCurrentStageDetailsDTO(
            task_display_id=task_display_id,
            stage_details_dtos=stage_details_dtos,
            user_has_permission=is_user_has_permission,
        )
        return task_current_stage_details_dto

    def _validate_task_id(
            self, task_id: int
    ) -> Union[InvalidTaskIdException, str]:
        task_display_id = self.task_stage_storage.validate_task_id(task_id)
        return task_display_id

    @staticmethod
    def _get_user_roles(user_id: str) -> List[str]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        role_service_adapter = get_roles_service_adapter()
        role_service = role_service_adapter.roles_service
        user_roles = role_service.get_user_role_ids(user_id)
        return user_roles
