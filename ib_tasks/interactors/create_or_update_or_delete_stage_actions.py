import json
from collections import defaultdict
from typing import List, Dict

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.exceptions.roles_custom_exceptions import InvalidRolesException
from ib_tasks.exceptions.stage_custom_exceptions import \
    InvalidStageIdsException
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTransitionTemplateIds
from ib_tasks.interactors.stages_dtos import StageActionDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageActionNamesDTO
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface\
    import TaskTemplateStorageInterface


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


class CreateOrUpdateOrDeleteStageActions:

    def __init__(self, storage: ActionStorageInterface,
                 template_storage: TaskTemplateStorageInterface):
        self.storage = storage
        self.template_storage = template_storage

    def create_or_update_or_delete_stage_actions(
            self, action_dtos: List[StageActionDTO]
    ):
        stage_ids = self._get_stage_ids(action_dtos)
        self._validations_for_stage_ids(stage_ids=stage_ids)
        transition_template_ids = \
            self._get_transition_template_ids(action_dtos)
        self._validations_for_transition_template_ids(transition_template_ids)
        self._validations_for_action_roles(action_dtos)
        self._validations_for_empty_stage_display_logic(action_dtos)
        self._validations_for_empty_button_texts(action_dtos)
        self._validations_for_button_texts(action_dtos)
        self._validations_for_duplicate_stage_actions(action_dtos)
        db_stage_action_name_dtos = \
            self.storage.get_stage_action_names(stage_ids=stage_ids)
        self._create_update_delete_stage_actions(
            db_stage_action_name_dtos, action_dtos
        )
        self._delete_stage_actions(db_stage_action_name_dtos, action_dtos)

    def _validations_for_transition_template_ids(
            self, transition_template_ids: List[str]):
        valid_transition_template_ids = self.template_storage. \
            get_valid_transition_template_ids(transition_template_ids)
        invalid_transition_ids = [
            transition_id
            for transition_id in transition_template_ids
            if transition_id.strip() and transition_id not in valid_transition_template_ids
        ]
        if invalid_transition_ids:
            raise InvalidTransitionTemplateIds(invalid_transition_ids)

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
    def _get_transition_template_ids(actions_dto: List[StageActionDTO]):
        transition_template_ids = [
            action.transition_template_id for action in actions_dto
        ]
        return transition_template_ids

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

    def _validations_for_action_roles(
            self, actions_dto: List[StageActionDTO]
    ):
        from ib_tasks.adapters.service_adapter import get_service_adapter
        adapter = get_service_adapter().roles_service
        role_ids = self._get_all_role_ids(actions_dto)
        valid_roles = adapter.get_valid_role_ids_in_given_role_ids(role_ids)
        invalid_stage_roles = defaultdict(list)
        for action_dto in actions_dto:
            if not action_dto.roles == [ALL_ROLES_ID]:
                stage_id = action_dto.stage_id
                self._validation_for_action_roles(
                    action_dto.roles, valid_roles, invalid_stage_roles, stage_id)

        is_invalid_stage_roles_present = invalid_stage_roles

        if is_invalid_stage_roles_present:
            stage_roles_dict = \
                json.dumps(invalid_stage_roles)
            raise InvalidRolesException(stage_roles_dict=stage_roles_dict)
        return

    @staticmethod
    def _get_all_role_ids(action_dtos: List[StageActionDTO]):

        role_ids = []
        for action_dto in action_dtos:
            role_ids += action_dto.roles
        return sorted(list(set(role_ids)))

    def _validation_for_action_roles(self, action_roles: List[str],
                                     valid_roles: List[str],
                                     invalid_stage_roles: Dict[str, List],
                                     stage_id: str):

        invalid_action_roles = self._get_invalid_roles_to_action(
            action_roles, valid_roles)

        is_invalid_action_roles_present = invalid_action_roles
        if is_invalid_action_roles_present:
            self._append_invalid_action_roles_to_dict(invalid_action_roles,
                                                      stage_id,
                                                      invalid_stage_roles)

    @staticmethod
    def _append_invalid_action_roles_to_dict(
            invalid_action_roles: List[str], stage_id: str,
            invalid_stage_roles_dict: Dict[str, List]):

        for role in invalid_action_roles:
            invalid_stage_roles_dict[stage_id].append(role)
        stage_roles = invalid_stage_roles_dict[stage_id]
        stage_roles = sorted(list(set(stage_roles)))
        invalid_stage_roles_dict[stage_id] = stage_roles

    @staticmethod
    def _get_invalid_roles_to_action(
            action_roles: List[str], db_roles: List[str]):

        invalid_action_roles = []
        for role in action_roles:
            if role not in db_roles:
                invalid_action_roles.append(role)
        return invalid_action_roles

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
            self, db_stage_actions_dto: List[StageActionNamesDTO],
            actions_dto: List[StageActionDTO]):

        from ib_tasks.interactors.create_or_update_stage_actions_interactor \
            import CreateOrUpdateStageActions
        interactor = CreateOrUpdateStageActions(storage=self.storage)

        interactor.create_or_update_stage_actions(
            db_stage_action_name_dtos=db_stage_actions_dto,
            action_dtos=actions_dto
        )

    def _delete_stage_actions(
            self,
            db_stage_actions_dto: List[StageActionNamesDTO],
            stage_actions: List[StageActionDTO]):

        from ib_tasks.interactors.delete_stage_actions_interactor \
            import DeleteStageActionsInteractor
        interactor = DeleteStageActionsInteractor(storage=self.storage)
        interactor.delete_stage_actions_wrapper(
            db_stage_action_name_dtos=db_stage_actions_dto,
            action_dtos=stage_actions
        )
