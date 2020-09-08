
from collections import defaultdict
from typing import List, Dict
from ib_tasks.interactors.stages_dtos import StageActionDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageActionNamesDTO


class CreateOrUpdateStageActions:

    def __init__(self, storage: ActionStorageInterface):
        self.storage = storage

    def create_or_update_stage_actions(
            self, db_stage_action_name_dtos: List[StageActionNamesDTO],
            action_dtos: List[StageActionDTO]):
        self._create_or_update_stage_actions(
            db_stage_action_dtos=db_stage_action_name_dtos,
            action_dtos=action_dtos
        )

    def _create_or_update_stage_actions(
            self, db_stage_action_dtos: List[StageActionNamesDTO],
            action_dtos: List[StageActionDTO]):
        for action in action_dtos:
            if action.transition_template_id == '':
                action.transition_template_id = None
        is_db_stage_actions_empty = not db_stage_action_dtos
        if is_db_stage_actions_empty:
            self.storage.create_stage_actions(stage_actions=action_dtos)
            return
        stage_actions = self._get_stage_actions_map(action_dtos)
        self._create_update_stage_actions(db_stage_action_dtos, stage_actions)

    @staticmethod
    def _get_stage_actions_map(actions_dto: List[StageActionDTO]):
        stage_actions_map = defaultdict(list)
        for action_dto in actions_dto:
            stage_actions_map[action_dto.stage_id].append(action_dto)
        return stage_actions_map

    def _create_update_stage_actions(
            self, db_stage_action_dtos: List[StageActionNamesDTO],
            stage_actions_map: Dict[str, List[StageActionDTO]]):
        create_stage_actions, update_stage_actions = [], []
        stage_ids = [
            db_stage_action_dto.stage_id
            for db_stage_action_dto in db_stage_action_dtos
        ]
        for stage_id, stage_actions in stage_actions_map.items():
            if stage_id not in stage_ids:
                create_stage_actions += stage_actions

        for stage_action_dto in db_stage_action_dtos:
            db_action_names = stage_action_dto.action_names
            stage_actions_dto = stage_actions_map[stage_action_dto.stage_id]
            self._append_create_and_update_stage_dto(
                db_action_names, stage_actions_dto,
                create_stage_actions, update_stage_actions
            )

        self._create_or_update_stage_actions_in_database(
            create_stage_actions, update_stage_actions
        )

    def _create_or_update_stage_actions_in_database(
            self, create_stage_actions: List[StageActionDTO],
            update_stage_actions: List[StageActionDTO]
    ):

        is_create_actions_present = create_stage_actions
        if is_create_actions_present:
            self.storage \
                .create_stage_actions(stage_actions=create_stage_actions)
        is_update_actions_present = update_stage_actions
        if is_update_actions_present:
            self.storage \
                .update_stage_actions(stage_actions=update_stage_actions)

    @staticmethod
    def _append_create_and_update_stage_dto(
            db_action_names: List[str],
            stage_actions_dto: List[StageActionDTO],
            create_stage_actions: List[StageActionDTO],
            update_stage_actions: List[StageActionDTO]):

        for stage_action_dto in stage_actions_dto:
            if stage_action_dto.action_name not in db_action_names:
                create_stage_actions.append(stage_action_dto)
            elif stage_action_dto.action_name in db_action_names:
                update_stage_actions.append(stage_action_dto)
