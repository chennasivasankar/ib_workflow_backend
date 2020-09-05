from typing import List

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds
from ib_tasks.interactors.storage_interfaces.action_storage_interface \
    import ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskProjectDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.user_role_validation_interactor import \
    UserRoleValidationInteractor


class GetTaskActionsInteractor:
    def __init__(self, action_storage: ActionStorageInterface,
                 task_storage: TaskStorageInterface,
                 stage_storage: StageStorageInterface
                 ):
        self.action_storage = action_storage
        self.task_storage = task_storage
        self.stage_storage = stage_storage

    def get_task_actions(self, stage_ids: List[str],
                         user_id: str,
                         task_ids: List[int]):
        task_ids = self._validate_task_ids(task_ids)
        self._validate_stage_ids(stage_ids)
        task_project_dtos = self.task_storage.get_task_project_ids(task_ids)
        user_roles_interactor = UserRoleValidationInteractor()
        permitted_action_ids = user_roles_interactor. \
            get_permitted_action_ids_for_given_user_in_projects(
            task_project_dtos=task_project_dtos,
            action_storage=self.action_storage, user_id=user_id, stage_ids=stage_ids)

        action_dtos = self.action_storage.get_actions_details(permitted_action_ids)
        return action_dtos

    def _validate_stage_ids(self, stage_ids: List[str]):
        valid_stage_ids = self.stage_storage.get_existing_stage_ids(
                stage_ids)
        invalid_stage_ids = [
                stage_id for stage_id in stage_ids
                if stage_id not in valid_stage_ids
        ]
        if invalid_stage_ids:
            from ib_tasks.exceptions.stage_custom_exceptions import \
                InvalidStageIdsListException
            raise InvalidStageIdsListException(invalid_stage_ids)

    def _validate_task_ids(self, task_ids: List[int]):
        valid_task_ids = self.task_storage.get_valid_task_ids(task_ids)
        invalid_task_ids = [
            task_id for task_id in task_ids if task_id not in valid_task_ids
        ]
        if invalid_task_ids:
            raise InvalidTaskIds(invalid_task_ids)
        return task_ids
