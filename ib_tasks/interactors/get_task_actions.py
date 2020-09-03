from typing import List

from ib_tasks.interactors.storage_interfaces.action_storage_interface \
    import ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.task_dtos import TaskProjectDTO
from ib_tasks.interactors.user_role_validation_interactor import \
    UserRoleValidationInteractor


class GetTaskActionsInteractor:
    def __init__(self, action_storage: ActionStorageInterface):
        self.action_storage = action_storage

    def get_task_actions(self, stage_ids: List[str],
                         user_id: str,
                         task_project_dtos: List[TaskProjectDTO]):
        user_roles_interactor = UserRoleValidationInteractor()
        permitted_action_ids = user_roles_interactor. \
            get_permitted_action_ids_for_given_user_in_projects(
            task_project_dtos=task_project_dtos,
            action_storage=self.action_storage, user_id=user_id, stage_ids=stage_ids)

        action_dtos = self.action_storage.get_actions_details(permitted_action_ids)
        return action_dtos
