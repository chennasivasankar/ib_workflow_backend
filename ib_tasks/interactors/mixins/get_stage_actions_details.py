from typing import List

from ib_tasks.interactors.dtos import RequestDTO


class GetStageActionsDetailsMixin:

    @staticmethod
    def get_stage_ids(actions_dto: List[RequestDTO]):
        stage_ids = [
            action_dto.stage_id
            for action_dto in actions_dto
        ]
        return stage_ids
