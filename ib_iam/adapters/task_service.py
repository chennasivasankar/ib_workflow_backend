from typing import List

from ib_iam.interactors.storage_interfaces.dtos import TeamUserIdsDTO


class TaskService:

    @property
    def interface(self):
        from ib_tasks.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()
        return service_interface

    def update_users_with_their_new_teams(
            self, team_user_id_dtos: List[TeamUserIdsDTO], old_team_id: str
    ):
        self.interface.update_user_teams_in_task_stage_history(
            team_user_id_dtos=team_user_id_dtos, old_team_id=old_team_id
        )
