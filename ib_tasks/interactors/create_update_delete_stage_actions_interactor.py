
from collections import defaultdict
from typing import List
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.interactors.dtos import StageActionDTO
from ib_tasks.interactors.mixins\
    .stage_actions_validation_mixin \
    import StageActionsAndTasksValidationMixin


class CreateUpdateDeleteStageActionsInteractor(
        StageActionsAndTasksValidationMixin):

    def __init__(self, storage: StorageInterface, actions_dto: List[StageActionDTO]):
        super().__init__(storage=storage)
        self.actions_dto = actions_dto

    def create_update_delete_stage_actions(self):
        actions_dto = self.actions_dto
        stage_ids = self._get_stage_ids(actions_dto)
        self.validations_for_stage_ids(stage_ids=stage_ids)
        self.validations_for_stage_roles(actions_dto)
        self.validations_for_empty_stage_display_logic(actions_dto)
        self.validations_for_empty_button_texts(actions_dto)
        self.validations_for_button_texts(actions_dto)
        self.validations_for_duplicate_stage_actions(actions_dto)
        self._create_update_delete_stage_actions(actions_dto)

    def _create_update_delete_stage_actions(
            self, actions_dto: List[StageActionDTO]):
        stage_ids = self._get_stage_ids(actions_dto)
        db_stage_actions_dto = self.storage \
            .get_stage_action_names(stage_ids=stage_ids)
        is_db_stage_actions_empty = not db_stage_actions_dto
        if is_db_stage_actions_empty:
            self.storage.create_stage_actions(stage_actions=actions_dto)
        stage_actions = self._get_stage_actions(actions_dto)
        self._create_update_stage_actions(db_stage_actions_dto, stage_actions)
        stage_action_names = self._get_stage_action_names(actions_dto)
        self._delete_stage_actions(db_stage_actions_dto, stage_action_names)

    def _delete_stage_actions(self, db_stage_actions_dto, stage_actions):

        delete_stage_actions = defaultdict(list)
        for stage_action_dto in db_stage_actions_dto:
            for action_name in stage_action_dto.action_names:
                stage_id = stage_action_dto.stage_id
                if action_name not in stage_actions[stage_id]:
                    delete_stage_actions[stage_id].append(action_name)

        is_delete_stage_actions_present = delete_stage_actions
        from ib_tasks.interactors.storage_interfaces.dtos \
            import StageActionNamesDTO
        if is_delete_stage_actions_present:
            delete_actions = [
                StageActionNamesDTO(stage_id=key, action_names=value)
                for key, value in delete_stage_actions.items()
            ]
            self.storage \
                .delete_stage_actions(stage_actions=delete_actions)

    @staticmethod
    def _get_stage_actions(actions_dto):
        stage_actions = defaultdict(list)
        for action_dto in actions_dto:
            stage_actions[action_dto.stage_id].append(action_dto)
        return stage_actions

    def _create_update_stage_actions(
            self, db_stage_actions_dto, stage_actions):
        create_stage_actions, update_stage_actions = [], []
        for stage_action_dto in db_stage_actions_dto:
            db_action_names = stage_action_dto.action_names
            stage_actions_dto = stage_actions[stage_action_dto.stage_id]
            self._append_create_and_update_stage_dto(
                db_action_names, stage_actions_dto,
                create_stage_actions, update_stage_actions
            )

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
            db_action_names, stage_actions_dto,
            create_stage_actions, update_stage_actions):
        for stage_action_dto in stage_actions_dto:
            if stage_action_dto.action_name not in db_action_names:
                create_stage_actions.append(stage_action_dto)
            elif stage_action_dto.action_name in db_action_names:
                update_stage_actions.append(stage_action_dto)


