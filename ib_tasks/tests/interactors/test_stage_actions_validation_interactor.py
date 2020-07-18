import pytest
import json
from unittest.mock import create_autospec
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.interactors.stage_actions_validation_interactor \
    import (
        EmptyStageDisplayLogic, DuplicateStageButtonsException,
        DuplicateStageActionNamesException, EmptyStageButtonText
    )
from ib_tasks.interactors.stage_actions_validation_interactor \
    import StageActionsAndTasksValidationInteractor
from ib_tasks.tests.factories.interactor_dtos import StageActionDTOFactory


class TestStageActionsAndTasksValidationInteractor:

    @staticmethod
    def test_given_invalid_stage_ids_raises_exception():
        # Arrange
        expected_stage_ids = ["stage_2"]
        expected_stage_ids_dict = json.dumps(
            {"invalid_stage_ids": expected_stage_ids}
        )
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        stage_ids = ["stage_1", "stage_2"]
        storage = create_autospec(StorageInterface)
        storage.get_valid_stage_ids.return_value = ["stage_1"]
        interactor = StageActionsAndTasksValidationInteractor(
            storage=storage
        )
        from ib_tasks.exceptions.custom_exceptions \
            import InvalidStageIdsException

        # Act
        with pytest.raises(InvalidStageIdsException) as err:
            assert interactor.validations_for_actions_dto(
                actions_dto=actions_dto)

        # Assert
        assert err.value.stage_ids_dict == expected_stage_ids_dict
        storage.get_valid_stage_ids\
            .assert_called_once_with(stage_ids=stage_ids)

    @staticmethod
    def test_given_invalid_roles_raises_exception(mocker):
        expected_stage_roles = {
            "stage_1": ["ROLE_1"],
            "stage_2": ["ROLE_2"]
        }
        expected_stage_role_dict = json.dumps(expected_stage_roles)
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=3)
        storage = create_autospec(StorageInterface)
        stage_ids = ["stage_1", "stage_2", "stage_3"]
        storage.get_valid_stage_ids.return_value = stage_ids
        interactor = StageActionsAndTasksValidationInteractor(
            storage=storage
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_invalid_mock
        mocker_obj = prepare_get_roles_for_invalid_mock(mocker)

        from ib_tasks.exceptions.custom_exceptions \
            import InvalidRolesException

        # Act
        with pytest.raises(InvalidRolesException) as err:
            interactor.validations_for_actions_dto(actions_dto=actions_dto)

        # Assert
        assert err.value.stage_roles_dict == expected_stage_role_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_empty_stage_display_logic_raises_exception(mocker):
        expected_stage_ids = {"stage_ids": ["stage_3"]}
        expected_stage_ids_dict = json.dumps(expected_stage_ids)
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        action_dto = StageActionDTOFactory(logic="")
        actions_dto.append(action_dto)
        storage = create_autospec(StorageInterface)
        stage_ids = ["stage_1", "stage_2", "stage_3"]
        storage.get_valid_stage_ids.return_value = stage_ids
        interactor = StageActionsAndTasksValidationInteractor(
            storage=storage
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(EmptyStageDisplayLogic) as err:
            interactor.validations_for_actions_dto(actions_dto=actions_dto)

        assert err.value.stage_ids_dict == expected_stage_ids_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_empty_stage_button_text_raises_exception(mocker):
        expected_stage_ids = {"stage_ids": ["stage_3"]}
        expected_stage_ids_dict = json.dumps(expected_stage_ids)
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        action_dto = StageActionDTOFactory(button_text="")
        actions_dto.append(action_dto)

        storage = create_autospec(StorageInterface)
        stage_ids = ["stage_1", "stage_2", "stage_3"]
        storage.get_valid_stage_ids.return_value = stage_ids
        interactor = StageActionsAndTasksValidationInteractor(
            storage=storage
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(EmptyStageButtonText) as err:
            interactor.validations_for_actions_dto(actions_dto=actions_dto)

        assert err.value.stage_ids_dict == expected_stage_ids_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_duplicate_stage_buttons_raises_exception(mocker):
        expected_stage_buttons = {
            "stage_1": ["add"]
        }
        expected_stage_buttons_dict = json.dumps(expected_stage_buttons)
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(
            size=2, stage_id="stage_1", button_text="add"
        )
        action_dto = StageActionDTOFactory(stage_id="stage_2", button_text="pay")
        actions_dto.append(action_dto)
        storage = create_autospec(StorageInterface)
        stage_ids = ["stage_1", "stage_2"]
        storage.get_valid_stage_ids.return_value = stage_ids
        interactor = StageActionsAndTasksValidationInteractor(
            storage=storage
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(DuplicateStageButtonsException) as err:
            interactor.validations_for_actions_dto(actions_dto=actions_dto)

        assert err.value.stage_buttons_dict == expected_stage_buttons_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_duplicate_stage_action_names_raises_exception(mocker):
        expected_stage_actions = {
            "stage_1": ["action_name_1"]
        }
        expected_stage_actions_dict = json.dumps(expected_stage_actions)
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(
            size=2, stage_id="stage_1", action_name="action_name_1"
        )
        action_dto = StageActionDTOFactory(stage_id="stage_2")
        actions_dto.append(action_dto)
        storage = create_autospec(StorageInterface)
        storage.get_valid_stage_ids.return_value = ["stage_1", "stage_2"]
        interactor = StageActionsAndTasksValidationInteractor(
            storage=storage
        )

        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(DuplicateStageActionNamesException) as err:
            interactor.validations_for_actions_dto(actions_dto=actions_dto)

        assert err.value.stage_actions == expected_stage_actions_dict
        mocker_obj.assert_called_once()