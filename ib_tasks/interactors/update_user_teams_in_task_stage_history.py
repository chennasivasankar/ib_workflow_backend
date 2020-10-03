from typing import List

from ib_tasks.interactors.dtos.dtos import TeamUserIdsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface


class UpdateUserTeamsInTaskStageHistory:

    def __init__(self, stage_storage: StageStorageInterface):
        self.stage_storage = stage_storage

    def update_user_teams_in_task_stage_history(
            self, team_user_id_dtos: List[TeamUserIdsDTO], old_team_id: str
    ):
        self.stage_storage.update_user_teams_in_task_stage_history(
            team_user_id_dtos=team_user_id_dtos, old_team_id=old_team_id
        )
