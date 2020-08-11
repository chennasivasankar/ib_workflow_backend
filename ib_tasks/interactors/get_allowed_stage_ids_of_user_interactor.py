from typing import List

from ib_tasks.interactors.stages_dtos import StageRolesDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface


class GetAllowedStageIdsOfUserInteractor:
    def __init__(self, storage: StageStorageInterface):
        self.storage = storage

    def get_allowed_stage_ids_of_user(self, user_id: str) -> List[str]:

        user_role_ids = self._get_user_role_ids(user_id=user_id)

        stage_roles_dtos = self.storage.get_stages_roles()

        return [
            stage_roles_dto.stage_id
            for stage_roles_dto in stage_roles_dtos
            if self._check_for_roles_match(stage_roles_dto, user_role_ids)
        ]

    @staticmethod
    def _check_for_roles_match(stage_roles_dto: StageRolesDTO,
                               user_role_ids: List[str]) -> bool:

        from ib_tasks.constants.constants import ALL_ROLES_ID
        if ALL_ROLES_ID in stage_roles_dto.role_ids:
            return True

        is_common_roles_present = \
            set(stage_roles_dto.role_ids).intersection(set(user_role_ids))
        if is_common_roles_present:
            return True
        return False

    @staticmethod
    def _get_user_role_ids(user_id: str) -> List[str]:
        from ib_tasks.adapters.roles_service_adapter import \
            get_roles_service_adapter
        roles_service_adapter = get_roles_service_adapter()
        roles_service = roles_service_adapter.roles_service
        user_role_ids = \
            roles_service.get_user_role_ids(user_id=user_id)
        return user_role_ids