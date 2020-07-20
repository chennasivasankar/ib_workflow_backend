import json
from collections import defaultdict
from typing import List

from ib_tasks.exceptions.custom_exceptions \
    import InvalidStageIdsException, InvalidRolesException
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.interactors.dtos import StageActionDTO


class EmptyStageDisplayLogic(Exception):
    def __init__(self, stage_ids_dict: str):
        self.stage_ids_dict = stage_ids_dict


class EmptyStageButtonText(Exception):
    def __init__(self, stage_ids_dict: str):
        self.stage_ids_dict = stage_ids_dict


class DuplicateStageButtonsException(Exception):
    def __init__(self, stage_buttons_dict: str):
        self.stage_buttons_dict = stage_buttons_dict


class DuplicateStageActionNamesException(Exception):
    def __init__(self, stage_actions: str):
        self.stage_actions = stage_actions


class CreateUpdateDeleteStageActionsInteractor():

    def __init__(self, storage: StorageInterface,
                 actions_dto: List[StageActionDTO]):
        self.storage = storage
        self.actions_dto = actions_dto

    def create_update_delete_stage_actions(self):
        actions_dto = self.actions_dto
        stage_ids = self._get_stage_ids(actions_dto)
        self._validations_for_stage_ids(stage_ids=stage_ids)
        self._validations_for_stage_roles(actions_dto)
        self._validations_for_empty_stage_display_logic(actions_dto)
        self._validations_for_empty_button_texts(actions_dto)
        self._validations_for_button_texts(actions_dto)
        self._validations_for_duplicate_stage_actions(actions_dto)
        self._create_update_delete_stage_actions(actions_dto)
    
    def _validations_for_duplicate_stage_actions(
            self, actions_dto: List[StageActionDTO]):
        stage_actions = self._get_stage_action_names(actions_dto)
        invalid_stage_actions = defaultdict(list)
        from collections import Counter
        for key, value in stage_actions.items():
            for item, count in Counter(value).items():
                if count > 1:
                    invalid_stage_actions[key].append(item)
        is_invalid_stage_buttons_present = invalid_stage_actions
        if is_invalid_stage_buttons_present:
            stage_actions = json.dumps(invalid_stage_actions)
            raise DuplicateStageActionNamesException(
                stage_actions=stage_actions
            )

    @staticmethod
    def _get_stage_action_names(actions_dto: List[StageActionDTO]):

        stage_actions = defaultdict(list)
        for action_dto in actions_dto:
            stage_actions[action_dto.stage_id].append(action_dto.action_name)
        return stage_actions

    def _validations_for_button_texts(self, actions_dto: List[StageActionDTO]):
        stage_buttons = self._get_stage_button_texts(actions_dto)
        from collections import Counter
        invalid_stage_buttons = defaultdict(list)
        for key, value in stage_buttons.items():
            for item, count in Counter(value).items():
                if count > 1:
                    invalid_stage_buttons[key].append(item)
        is_invalid_stage_buttons_present = invalid_stage_buttons
        if is_invalid_stage_buttons_present:
            stage_buttons_dict = json.dumps(invalid_stage_buttons)
            raise DuplicateStageButtonsException(
                stage_buttons_dict=stage_buttons_dict
            )

    @staticmethod
    def _get_stage_button_texts(actions_dto: List[StageActionDTO]):
        stage_button_texts = defaultdict(list)
        for action_dto in actions_dto:
            stage_id = action_dto.stage_id
            stage_button_texts[stage_id].append(action_dto.button_text)
        return stage_button_texts

    @staticmethod
    def _validations_for_empty_stage_display_logic(actions_dto):

        empty_stage_display_logic_ids = sorted(list({
            action_dto.stage_id
            for action_dto in actions_dto if action_dto.logic == ""
        }))
        is_empty_stage_display_logic_present = empty_stage_display_logic_ids
        if is_empty_stage_display_logic_present:
            stage_ids_dict = json.dumps(
                {"stage_ids": empty_stage_display_logic_ids}
            )
            raise EmptyStageDisplayLogic(stage_ids_dict=stage_ids_dict)

    @staticmethod
    def _validations_for_empty_button_texts(actions_dto):

        empty_button_texts_stage_ids = list({
            action_dto.stage_id
            for action_dto in actions_dto if action_dto.button_text == ""
        })
        is_empty_stage_button_text_present = empty_button_texts_stage_ids
        if is_empty_stage_button_text_present:
            stage_ids_dict = json.dumps(
                {"stage_ids": empty_button_texts_stage_ids}
            )
            raise EmptyStageButtonText(stage_ids_dict=stage_ids_dict)

    def _validations_for_stage_roles(self, actions_dto: List[StageActionDTO]):
        from ib_tasks.adapters.service_adapter import get_service_adapter
        db_roles = get_service_adapter().roles_service.get_db_roles()
        invalid_stage_roles = defaultdict(list)
        for action_dto in actions_dto:
            if self._check_for_invalid_role(action_dto.role, db_roles):
                invalid_stage_roles[action_dto.stage_id].append(action_dto.role)
        is_invalid_stage_roles_present = invalid_stage_roles
        if is_invalid_stage_roles_present:
            stage_roles_dict = \
                json.dumps(invalid_stage_roles)
            raise InvalidRolesException(stage_roles_dict=stage_roles_dict)

    @staticmethod
    def _check_for_invalid_role(role: str, db_roles: List[str]):

        field = False
        if role not in db_roles:
            is_not_all_roles = not role == "ALL_ROLES"
            if is_not_all_roles:
                field = True
        return field

    def _validations_for_stage_ids(self, stage_ids: List[str]):
        db_stage_ids = self.storage.get_valid_stage_ids(stage_ids=stage_ids)
        invalid_stage_ids = self._get_invalid_stage_ids(
            stage_ids=stage_ids, db_stage_ids=db_stage_ids)
        is_invalid_stage_ids_present = invalid_stage_ids
        if is_invalid_stage_ids_present:
            stage_ids_dict = json.dumps(
                {"invalid_stage_ids": invalid_stage_ids}
            )
            raise InvalidStageIdsException(stage_ids_dict=stage_ids_dict)

    @staticmethod
    def _get_invalid_stage_ids(stage_ids: List[str], db_stage_ids: List[str]):
        invalid_stage_ids = [
            stage_id
            for stage_id in stage_ids if stage_id not in db_stage_ids
        ]
        return invalid_stage_ids

    @staticmethod
    def _get_stage_ids(actions_dto: List[StageActionDTO]):
        stage_ids = [
            action_dto.stage_id
            for action_dto in actions_dto
        ]
        return stage_ids

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


