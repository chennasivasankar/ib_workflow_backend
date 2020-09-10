from typing import List
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface


class GetAllowedStageIdsOfUserInteractor:
    def __init__(self, storage: StageStorageInterface):
        self.storage = storage

    def get_allowed_stage_ids_of_user(self, user_id: str) -> List[str]:

        user_role_ids = self._get_user_role_ids(user_id=user_id)

        stage_ids = \
            self.storage.get_permitted_stage_ids(user_role_ids=user_role_ids)

        return stage_ids

    @staticmethod
    def _get_user_role_ids(user_id: str) -> List[str]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        user_role_ids = \
            roles_service.get_user_role_ids(user_id=user_id)
        return user_role_ids
