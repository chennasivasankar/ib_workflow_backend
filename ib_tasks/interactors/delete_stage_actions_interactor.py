from collections import defaultdict
from typing import List, Dict

from ib_tasks.interactors.stages_dtos import StageActionDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageActionNamesDTO


class DeleteStageActionsInteractor:

    def __init__(self, storage: ActionStorageInterface):
        self.storage = storage

    def delete_stage_actions_wrapper(
            self, db_stage_action_name_dtos: List[StageActionNamesDTO],
            action_dtos: List[StageActionDTO]):
        stage_action_name_map = self._get_stage_action_names_map(action_dtos)
        self._delete_stage_actions(
            db_stage_action_name_dtos, stage_action_name_map
        )

    @staticmethod
    def _get_stage_action_names_map(action_dtos: List[StageActionDTO]):

        stage_actions_map = defaultdict(list)
        for action_dto in action_dtos:
            stage_actions_map[action_dto.stage_id].append(
                action_dto.action_name
            )
        return stage_actions_map

    def _delete_stage_actions(
            self, db_stage_action_name_dtos: List[StageActionNamesDTO],
            stage_action_name_map: Dict[str, List[str]]):

        delete_stage_actions_map = defaultdict(list)
        for stage_action_dto in db_stage_action_name_dtos:
            self.add_delete_stage_action_name(
                stage_action_dto, stage_action_name_map,
                delete_stage_actions_map
            )

        is_delete_stage_actions_present = delete_stage_actions_map
        if is_delete_stage_actions_present:
            delete_actions = [
                StageActionNamesDTO(stage_id=key, action_names=value)
                for key, value in delete_stage_actions_map.items()
            ]
            self.storage \
                .delete_stage_actions(stage_actions=delete_actions)

    @staticmethod
    def add_delete_stage_action_name(
            stage_action_name_dto: StageActionNamesDTO,
            stage_action_name_map: Dict[str, List[str]],
            delete_stage_actions_map: Dict[str, List[str]]
    ):
        for action_name in stage_action_name_dto.action_names:
            stage_id = stage_action_name_dto.stage_id
            if action_name not in stage_action_name_map[stage_id]:
                delete_stage_actions_map[stage_id].append(action_name)
