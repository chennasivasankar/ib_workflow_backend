from typing import List

from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface


class GetAllowedStageIdsOfUserInteractor:
    def __init__(self, storage: StageStorageInterface):
        self.storage = storage

    def get_allowed_stage_ids_of_user(self, user_id: str) -> List[str]:
        stage_ids = self.storage.get_allowed_stage_ids_of_user()
        return stage_ids
