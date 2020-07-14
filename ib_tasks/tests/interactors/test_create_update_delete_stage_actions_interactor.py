import pytest
import json
from unittest.mock import create_autospec
from ib_tasks.interactors.storage_interfaces.action_storage_interface \
    import ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_storage_interface \
    import StageStorageInterface
from ib_tasks.interactors.create_update_delete_stage_actions_interactor \
    import (
        CreateUpdateDeleteStageActionsInteractor, EmptyStageDisplayLogic,
        DuplicateStageButtonsException, DuplicateStageActionNamesException,
        EmptyStageButtonText
    )
from ib_tasks.interactors.dtos import ActionDto
from ib_tasks.tests.factories.interactor_dtos import ActionDtoFactory


class TestCreateUpdateDeleteStageActionsInteractor:

    @staticmethod
    def test_given_invalid_stage_ids_raises_exception():
        # Arrange
        expected_stage_ids = ["stage_2"]
        expected_stage_ids_dict = json.dumps(
            {"invalid_stage_ids": expected_stage_ids}
        )
        ActionDtoFactory.reset_sequence(0)
        actions_dto = ActionDtoFactory.create_batch(size=2)
        stage_ids = ["stage_1", "stage_2"]
        stage_storage = create_autospec(StageStorageInterface)
        stage_storage.get_db_stage_ids.return_value = ["stage_1"]
        action_storage = create_autospec(ActionStorageInterface)
        interactor = CreateUpdateDeleteStageActionsInteractor(
            stage_storage=stage_storage, action_storage=action_storage,
            actions_dto=actions_dto
        )
        from ib_tasks.exceptions.custom_exceptions \
            import InvalidStageIdsException

        # Act
        with pytest.raises(InvalidStageIdsException) as err:
            assert interactor.create_update_delete_stage_actions()

        # Assert
        assert err.value.stage_ids_dict == expected_stage_ids_dict
        stage_storage.get_db_stage_ids\
            .assert_called_once_with(stage_ids=stage_ids)

    @staticmethod
    def test_given_invalid_roles_raises_exception(mocker):
        expected_stage_roles = {
            "stage_1": ["ROLE_1"],
            "stage_2": ["ROLE_2"]
        }
        expected_stage_role_dict = json.dumps(expected_stage_roles)
        ActionDtoFactory.reset_sequence(0)
        actions_dto = ActionDtoFactory.create_batch(size=3)
        stage_storage = create_autospec(StageStorageInterface)
        stage_ids = ["stage_1", "stage_2", "stage_3"]
        stage_storage.get_db_stage_ids.return_value = stage_ids
        action_storage = create_autospec(ActionStorageInterface)
        interactor = CreateUpdateDeleteStageActionsInteractor(
            stage_storage=stage_storage, action_storage=action_storage,
            actions_dto=actions_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_invalid_mock
        mocker_obj = prepare_get_roles_for_invalid_mock(mocker)

        from ib_tasks.exceptions.custom_exceptions \
            import InvalidRolesException

        # Act
        with pytest.raises(InvalidRolesException) as err:
            interactor.create_update_delete_stage_actions()

        # Assert
        assert err.value.stage_roles_dict == expected_stage_role_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_empty_stage_display_logic_raises_exception(mocker):
        expected_stage_ids = {"stage_ids": ["stage_3"]}
        expected_stage_ids_dict = json.dumps(expected_stage_ids)
        ActionDtoFactory.reset_sequence(0)
        actions_dto = ActionDtoFactory.create_batch(size=2)
        action_dto = ActionDtoFactory(logic="")
        actions_dto.append(action_dto)
        stage_storage = create_autospec(StageStorageInterface)
        stage_ids = ["stage_1", "stage_2", "stage_3"]
        stage_storage.get_db_stage_ids.return_value = stage_ids
        action_storage = create_autospec(ActionStorageInterface)
        interactor = CreateUpdateDeleteStageActionsInteractor(
            stage_storage=stage_storage,
            action_storage=action_storage,
            actions_dto=actions_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(EmptyStageDisplayLogic) as err:
            interactor.create_update_delete_stage_actions()

        assert err.value.stage_ids_dict == expected_stage_ids_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_empty_stage_button_text_raises_exception(mocker):
        expected_stage_ids = {"stage_ids": ["stage_3"]}
        expected_stage_ids_dict = json.dumps(expected_stage_ids)
        ActionDtoFactory.reset_sequence(0)
        actions_dto = ActionDtoFactory.create_batch(size=2)
        action_dto = ActionDtoFactory(button_text="")
        actions_dto.append(action_dto)

        stage_storage = create_autospec(StageStorageInterface)
        stage_ids = ["stage_1", "stage_2", "stage_3"]
        stage_storage.get_db_stage_ids.return_value = stage_ids
        action_storage = create_autospec(ActionStorageInterface)
        interactor = CreateUpdateDeleteStageActionsInteractor(
            stage_storage=stage_storage,
            action_storage=action_storage,
            actions_dto=actions_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(EmptyStageButtonText) as err:
            interactor.create_update_delete_stage_actions()

        assert err.value.stage_ids_dict == expected_stage_ids_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_duplicate_stage_buttons_raises_exception(mocker):
        expected_stage_buttons = {
            "stage_1": ["add"]
        }
        expected_stage_buttons_dict = json.dumps(expected_stage_buttons)
        ActionDtoFactory.reset_sequence(0)
        actions_dto = ActionDtoFactory.create_batch(
            size=2, stage_id="stage_1", button_text="add"
        )
        action_dto = ActionDtoFactory(stage_id="stage_2", button_text="pay")
        actions_dto.append(action_dto)
        stage_storage = create_autospec(StageStorageInterface)
        stage_ids = ["stage_1", "stage_2"]
        stage_storage.get_db_stage_ids.return_value = stage_ids
        action_storage = create_autospec(ActionStorageInterface)
        interactor = CreateUpdateDeleteStageActionsInteractor(
            stage_storage=stage_storage,
            action_storage=action_storage,
            actions_dto=actions_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(DuplicateStageButtonsException) as err:
            interactor.create_update_delete_stage_actions()

        assert err.value.stage_buttons_dict == expected_stage_buttons_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_duplicate_stage_action_names_raises_exception(mocker):
        expected_stage_actions = {
            "stage_1": ["action_name_1"]
        }
        expected_stage_actions_dict = json.dumps(expected_stage_actions)
        ActionDtoFactory.reset_sequence(0)
        actions_dto = ActionDtoFactory.create_batch(
            size=2, stage_id="stage_1", action_name="action_name_1"
        )
        action_dto = ActionDtoFactory(stage_id="stage_2")
        actions_dto.append(action_dto)
        stage_storage = create_autospec(StageStorageInterface)
        stage_storage.get_db_stage_ids.return_value = ["stage_1", "stage_2"]
        action_storage = create_autospec(ActionStorageInterface)
        interactor = CreateUpdateDeleteStageActionsInteractor(
            stage_storage=stage_storage, action_storage=action_storage,
            actions_dto=actions_dto
        )

        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(DuplicateStageActionNamesException) as err:
            interactor.create_update_delete_stage_actions()

        assert err.value.stage_actions == expected_stage_actions_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_create_stage_actions_creates_actions(mocker):

        ActionDtoFactory.reset_sequence(0)
        actions_dto = ActionDtoFactory.create_batch(size=2)
        stage_actions_dto = []
        create_stage_actions_dto = actions_dto
        stage_ids = ["stage_1", "stage_2"]
        stage_storage = create_autospec(StageStorageInterface)
        stage_storage.get_db_stage_ids.return_value = stage_ids
        action_storage = create_autospec(ActionStorageInterface)
        action_storage.get_stage_action_names.return_value = stage_actions_dto
        interactor = CreateUpdateDeleteStageActionsInteractor(
            stage_storage=stage_storage, action_storage=action_storage,
            actions_dto=actions_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        interactor.create_update_delete_stage_actions()

        # Assert
        action_storage.get_stage_action_names\
            .assert_called_once_with(stage_ids=stage_ids)
        action_storage.create_stage_actions \
            .assert_called_once_with(stage_actions=create_stage_actions_dto)
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_update_stage_actions_updates_actions(mocker):
        from ib_tasks.tests.factories.interactor_dtos import ActionDtoFactory
        ActionDtoFactory.reset_sequence(0)
        actions_dto = ActionDtoFactory.create_batch(size=2)
        from ib_tasks.interactors.storage_interfaces.dtos \
            import StageActionsDto
        stage_actions_dto = [
            StageActionsDto(
                stage_id="stage_1", action_names=["action_name_1"]
            )
        ]
        update_stage_actions_dto = [actions_dto[0]]
        stage_ids = ["stage_1", "stage_2"]
        stage_storage = create_autospec(StageStorageInterface)
        stage_storage.get_db_stage_ids.return_value = stage_ids
        action_storage = create_autospec(ActionStorageInterface)
        action_storage.get_stage_action_names.return_value = stage_actions_dto
        interactor = CreateUpdateDeleteStageActionsInteractor(
            stage_storage=stage_storage, action_storage=action_storage,
            actions_dto=actions_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        interactor.create_update_delete_stage_actions()

        # Assert
        action_storage.get_stage_action_names\
            .assert_called_once_with(stage_ids=stage_ids)
        action_storage.update_stage_actions \
            .assert_called_once_with(stage_actions=update_stage_actions_dto)
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_delete_stage_actions_deletes_actions(mocker):
        from ib_tasks.interactors.storage_interfaces.dtos \
            import StageActionsDto
        expected_stage_actions = [
            StageActionsDto(
                stage_id="stage_3", action_names=["action_name_3"]
            )
        ]
        from ib_tasks.tests.factories.interactor_dtos import ActionDtoFactory
        ActionDtoFactory.reset_sequence(0)
        actions_dto = ActionDtoFactory.create_batch(size=2)
        stage_actions_dto = [
            StageActionsDto(
                stage_id="stage_1", action_names=["action_name_1"]
            ),
            StageActionsDto(
                stage_id="stage_3", action_names=["action_name_3"]
            )
        ]
        delete_action_names = ["action_name_3"]
        update_stage_actions_dto = [actions_dto[0]]
        stage_ids = ["stage_1", "stage_2"]
        stage_storage = create_autospec(StageStorageInterface)
        stage_storage.get_db_stage_ids.return_value = stage_ids
        action_storage = create_autospec(ActionStorageInterface)
        action_storage.get_stage_action_names.return_value = stage_actions_dto
        interactor = CreateUpdateDeleteStageActionsInteractor(
            stage_storage=stage_storage, action_storage=action_storage,
            actions_dto=actions_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        interactor.create_update_delete_stage_actions()

        # Assert
        action_storage.get_stage_action_names\
            .assert_called_once_with(stage_ids=stage_ids)
        action_storage.update_stage_actions \
            .assert_called_once_with(stage_actions=update_stage_actions_dto)
        action_storage.delete_stage_actions \
            .assert_called_once_with(stage_actions=expected_stage_actions)
        mocker_obj.assert_called_once()
