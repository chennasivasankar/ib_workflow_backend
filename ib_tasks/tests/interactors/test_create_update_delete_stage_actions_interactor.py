import json
from unittest.mock import create_autospec

import pytest

from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidTransitionTemplateIds
from ib_tasks.interactors.create_or_update_or_delete_stage_actions import (
    EmptyStageDisplayLogic, DuplicateStageButtonsException,
    DuplicateStageActionNamesException, EmptyStageButtonText,
    CreateOrUpdateOrDeleteStageActions
)
from ib_tasks.interactors.storage_interfaces.action_storage_interface \
    import ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface \
    import TaskTemplateStorageInterface
from ib_tasks.tests.factories.interactor_dtos import StageActionDTOFactory


class TestCreateUpdateDeleteStageActionsInteractor:

    @staticmethod
    def test_given_invalid_stage_ids_raises_exception():
        # Arrange
        expected_stage_ids = ["stage_id_2"]
        expected_stage_ids_dict = json.dumps(
            {"invalid_stage_ids": expected_stage_ids}
        )
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        stage_ids = ["stage_id_1", "stage_id_2"]
        storage = create_autospec(ActionStorageInterface)
        template_storage = create_autospec(TaskTemplateStorageInterface)
        storage.get_valid_stage_ids.return_value = ["stage_id_1"]
        interactor = CreateOrUpdateOrDeleteStageActions(
            storage=storage,
            template_storage=template_storage
        )
        from ib_tasks.exceptions.stage_custom_exceptions \
            import InvalidStageIdsException

        # Act
        with pytest.raises(InvalidStageIdsException) as err:
            interactor.create_or_update_or_delete_stage_actions(
                action_dtos=actions_dto
            )

        # Assert
        assert err.value.stage_ids_dict == expected_stage_ids_dict
        storage.get_valid_stage_ids\
            .assert_called_once_with(stage_ids=stage_ids)

    @staticmethod
    def test_given_invalid_transition_template_ids_raises_exception():
        # Arrange
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        stage_ids = ["stage_id_1", "stage_id_2"]
        transition_ids = ["template_1", "template_2"]
        storage = create_autospec(ActionStorageInterface)
        template_storage = create_autospec(TaskTemplateStorageInterface)
        storage.get_valid_stage_ids.return_value = ["stage_id_1", "stage_id_2"]
        template_storage.get_valid_transition_template_ids.return_value = []
        interactor = CreateOrUpdateOrDeleteStageActions(
            storage=storage,
            template_storage=template_storage
        )

        # Act
        with pytest.raises(InvalidTransitionTemplateIds) as err:
            interactor.create_or_update_or_delete_stage_actions(
                action_dtos=actions_dto
            )
        # Assert

        storage.get_valid_stage_ids \
            .assert_called_once_with(stage_ids=stage_ids)
        template_storage.get_valid_transition_template_ids.\
            assert_called_once_with(transition_ids)

    @staticmethod
    def test_given_invalid_roles_raises_exception(mocker):

        # Arrange
        expected_stage_roles = {
            "stage_id_1": ["ROLE_1", "ROLE_2"],
            "stage_id_2": ["ROLE_2"],
            "stage_id_3": ["ROLE_4"]
        }
        expected_stage_role_dict = json.dumps(expected_stage_roles)
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=3)
        storage = create_autospec(ActionStorageInterface)
        template_storage = create_autospec(TaskTemplateStorageInterface)
        template_storage.get_valid_transition_template_ids.return_value =\
        ["template_1", "template_2", "template_3"]
        stage_ids = ["stage_id_1", "stage_id_2", "stage_id_3"]
        storage.get_valid_stage_ids.return_value = stage_ids
        interactor = CreateOrUpdateOrDeleteStageActions(
            storage=storage,
            template_storage=template_storage
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_invalid_mock
        mocker_obj = prepare_get_roles_for_invalid_mock(mocker)

        from ib_tasks.exceptions.roles_custom_exceptions import InvalidRolesException

        # Act
        with pytest.raises(InvalidRolesException) as err:
            interactor.create_or_update_or_delete_stage_actions(
                action_dtos=actions_dto
            )

        # Assert
        assert err.value.stage_roles_dict == expected_stage_role_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_empty_stage_display_logic_raises_exception(mocker):

        # Arrange
        project_id = "FINMAN"
        expected_stage_ids = {"stage_ids": ["stage_id_3"]}
        expected_stage_ids_dict = json.dumps(expected_stage_ids)
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        action_dto = StageActionDTOFactory(logic="")
        actions_dto.append(action_dto)
        storage = create_autospec(ActionStorageInterface)
        stage_ids = ["stage_id_1", "stage_id_2", "stage_id_3"]
        template_storage = create_autospec(TaskTemplateStorageInterface)
        template_storage.get_valid_transition_template_ids.return_value = \
            ["template_1", "template_2", "template_3"]
        storage.get_valid_stage_ids.return_value = stage_ids
        interactor = CreateOrUpdateOrDeleteStageActions(
            storage=storage,
            template_storage=template_storage
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(EmptyStageDisplayLogic) as err:
            interactor.create_or_update_or_delete_stage_actions(
                action_dtos=actions_dto
            )

        assert err.value.stage_ids_dict == expected_stage_ids_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_empty_stage_button_text_raises_exception(mocker):

        # Arrange
        expected_stage_ids = {"stage_ids": ["stage_id_3"]}
        expected_stage_ids_dict = json.dumps(expected_stage_ids)
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        action_dto = StageActionDTOFactory(button_text="")
        actions_dto.append(action_dto)
        template_storage = create_autospec(TaskTemplateStorageInterface)
        template_storage.get_valid_transition_template_ids.return_value = \
            ["template_1", "template_2",
             "template_3"
             ]
        storage = create_autospec(ActionStorageInterface)
        stage_ids = ["stage_id_1", "stage_id_2", "stage_id_3"]
        storage.get_valid_stage_ids.return_value = stage_ids
        interactor = CreateOrUpdateOrDeleteStageActions(
            storage=storage,
            template_storage=template_storage
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(EmptyStageButtonText) as err:
            interactor.create_or_update_or_delete_stage_actions(
                action_dtos=actions_dto
            )

        assert err.value.stage_ids_dict == expected_stage_ids_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_duplicate_stage_buttons_raises_exception(mocker):

        # Arrange
        expected_stage_buttons = {
            "stage_id_1": ["add"]
        }
        expected_stage_buttons_dict = json.dumps(expected_stage_buttons)
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(
            size=2, stage_id="stage_id_1", button_text="add"
        )
        action_dto = StageActionDTOFactory(stage_id="stage_id_2", button_text="pay")
        actions_dto.append(action_dto)
        storage = create_autospec(ActionStorageInterface)
        template_storage = create_autospec(TaskTemplateStorageInterface)
        template_storage.get_valid_transition_template_ids.return_value = \
            ["template_1", "template_2",
             "template_3"
             ]
        stage_ids = ["stage_id_1", "stage_id_2"]
        storage.get_valid_stage_ids.return_value = stage_ids
        interactor = CreateOrUpdateOrDeleteStageActions(
            storage=storage,
            template_storage=template_storage
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(DuplicateStageButtonsException) as err:
            interactor.create_or_update_or_delete_stage_actions(
                action_dtos=actions_dto
            )

        assert err.value.stage_buttons_dict == expected_stage_buttons_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_duplicate_stage_action_names_raises_exception(mocker):

        # Arrange
        expected_stage_actions = {
            "stage_id_1": ["action_name_1"]
        }
        expected_stage_actions_dict = json.dumps(expected_stage_actions)
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(
            size=2, stage_id="stage_id_1", action_name="action_name_1"
        )
        action_dto = StageActionDTOFactory(stage_id="stage_id_2")
        actions_dto.append(action_dto)
        storage = create_autospec(ActionStorageInterface)
        template_storage = create_autospec(TaskTemplateStorageInterface)
        template_storage.get_valid_transition_template_ids.return_value = \
            ["template_1", "template_2",
             "template_3"
             ]
        storage.get_valid_stage_ids.return_value = ["stage_id_1", "stage_id_2"]
        interactor = CreateOrUpdateOrDeleteStageActions(
            storage=storage,
            template_storage=template_storage
        )

        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(DuplicateStageActionNamesException) as err:
            interactor.create_or_update_or_delete_stage_actions(
                action_dtos=actions_dto
            )

        assert err.value.stage_actions == expected_stage_actions_dict
        mocker_obj.assert_called_once()

    @pytest.fixture()
    def create_update_mock(self, mocker):

        path = 'ib_tasks.interactors.create_or_update_stage_actions_interactor.CreateOrUpdateStageActions' \
               '.create_or_update_stage_actions'
        mock_obj = mocker.patch(path)
        return mock_obj

    @pytest.fixture()
    def delete_stage_action_mock(self, mocker):
        path = 'ib_tasks.interactors.delete_stage_actions_interactor.DeleteStageActionsInteractor' \
               '.delete_stage_actions_wrapper'
        mock_obj = mocker.patch(path)
        return mock_obj

    @staticmethod
    def test_given_create_stage_actions_creates_actions(
            mocker, create_update_mock, delete_stage_action_mock):

        # Arrange
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        stage_actions_dto = []
        create_stage_actions_dto = actions_dto
        stage_ids = ["stage_id_1", "stage_id_2"]
        storage = create_autospec(ActionStorageInterface)
        template_storage = create_autospec(TaskTemplateStorageInterface)
        template_storage.get_valid_transition_template_ids.return_value = \
            ["template_1", "template_2",
             "template_3"
             ]
        storage.get_valid_stage_ids.return_value = stage_ids
        storage.get_stage_action_names.return_value = stage_actions_dto
        interactor = CreateOrUpdateOrDeleteStageActions(
            storage=storage,
            template_storage=template_storage
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        interactor.create_or_update_or_delete_stage_actions(
            action_dtos=actions_dto
        )

        # Assert
        storage.get_stage_action_names\
            .assert_called_once_with(stage_ids=stage_ids)
        create_update_mock.assert_called_once_with(
            db_stage_action_name_dtos=stage_actions_dto,
            action_dtos=create_stage_actions_dto
        )
        delete_stage_action_mock.ssert_called_once_with(
            db_stage_action_name_dtos=stage_actions_dto,
            action_dtos=create_stage_actions_dto
        )
        mocker_obj.assert_called_once()
