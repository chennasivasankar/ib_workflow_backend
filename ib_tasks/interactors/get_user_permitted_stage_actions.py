from typing import List

from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface


class InvalidTaskTemplateIdsException(Exception):
    def __init__(self, task_template_ids_dict: str):
        self.task_template_ids_dict = task_template_ids_dict


class GetUserPermittedStageActions:

    def __init__(self, storage: StorageInterface,
                 user_id: str, stage_ids: List[str]
                 ):
        self.storage = storage
        self.user_id = user_id
        self.stage_ids = stage_ids

    def get_user_permitted_stage_actions(self):

        actions_roles_dto = self.storage.get_action_roles_to_stages(
            stage_ids=self.stage_ids)

        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_roles = service_adapter.roles_service\
            .get_user_roles(user_id=self.user_id)

        action_ids = self._get_user_permitted_action_ids(
            actions_roles_dto, user_roles)
        actions_dto = self.storage.get_actions_dto(action_ids=action_ids)
        return actions_dto

    @staticmethod
    def _get_user_permitted_action_ids(actions_roles_dto, user_roles):

        action_ids = []
        for role in user_roles:
            for action_role in actions_roles_dto:
                if role in action_role.roles:
                    action_ids.append(action_role.action_id)
        return sorted(list(set(action_ids)))

