from typing import List

from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface


class GetUserPermittedStageIds:

    def __init__(self, stage_storage: StageStorageInterface):
        self.stage_storage = stage_storage

    def get_permitted_stage_ids_to_user_role_ids(
            self, user_roles: List[str]
    ) -> List[str]:
        self._validate_user_roles(user_roles)
        stage_ids = self.stage_storage.get_stage_ids_having_actions(
            user_roles=user_roles
        )
        return stage_ids

    @staticmethod
    def _validate_user_roles(user_roles: List[str]):
        from ib_tasks.adapters.service_adapter import ServiceAdapter
        adapter = ServiceAdapter().roles_service
        valid_roles = adapter.get_valid_role_ids_in_given_role_ids(
            role_ids=user_roles
        )
        invalid_roles = [
            role_id
            for role_id in user_roles
            if role_id not in valid_roles
        ]
        if invalid_roles:
            from ib_tasks.exceptions.roles_custom_exceptions import InvalidRoleIdsException
            raise InvalidRoleIdsException(role_ids=invalid_roles)
