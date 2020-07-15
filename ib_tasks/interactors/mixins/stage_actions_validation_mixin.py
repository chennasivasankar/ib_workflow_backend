import json
from collections import defaultdict
from typing import List
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.exceptions.custom_exceptions import (
    InvalidStageIdsException, InvalidRolesException
)
from ib_tasks.interactors.dtos import RequestDTO


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


class StageActionsAndTasksValidationMixin:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def validations_for_duplicate_stage_actions(
            self, actions_dto: List[RequestDTO]):
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
    def _get_stage_action_names(actions_dto: List[RequestDTO]):

        stage_actions = defaultdict(list)
        for action_dto in actions_dto:
            stage_actions[action_dto.stage_id].append(action_dto.action_name)
        return stage_actions

    def validations_for_button_texts(self, actions_dto: List[RequestDTO]):
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
    def _get_stage_button_texts(actions_dto: List[RequestDTO]):
        stage_button_texts = defaultdict(list)
        for action_dto in actions_dto:
            stage_id = action_dto.stage_id
            stage_button_texts[stage_id].append(action_dto.button_text)
        return stage_button_texts

    @staticmethod
    def validations_for_empty_stage_display_logic(actions_dto):

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
    def validations_for_empty_button_texts(actions_dto):

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

    def validations_for_stage_roles(self, actions_dto: List[RequestDTO]):
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

    def validations_for_stage_ids(self, stage_ids: List[str]):
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
    def _get_stage_ids(actions_dto: List[RequestDTO]):
        stage_ids = [
            action_dto.stage_id
            for action_dto in actions_dto
        ]
        return stage_ids
