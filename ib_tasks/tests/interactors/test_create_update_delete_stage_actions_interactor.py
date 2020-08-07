import pytest
import json
from unittest.mock import create_autospec

from ib_tasks.exceptions.task_custom_exceptions import InvalidTransitionTemplateIds
from ib_tasks.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_tasks.interactors.create_update_delete_stage_actions \
    import (
        EmptyStageDisplayLogic, DuplicateStageButtonsException,
        DuplicateStageActionNamesException, EmptyStageButtonText
    )
from ib_tasks.interactors.create_update_delete_stage_actions \
    import CreateUpdateDeleteStageActionsInteractor
from ib_tasks.interactors.storage_interfaces.task_template_storage_interface import TaskTemplateStorageInterface
from ib_tasks.tests.factories.interactor_dtos import StageActionDTOFactory


class TestCreateUpdateDeleteStageActionsInteractor:

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
        template_storage = create_autospec(TaskTemplateStorageInterface)
        storage.get_valid_stage_ids.return_value = ["stage_1"]
        interactor = CreateUpdateDeleteStageActionsInteractor(
            storage=storage,
            template_storage=template_storage,
            actions_dto=actions_dto
        )
        from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageIdsException

        # Act
        with pytest.raises(InvalidStageIdsException) as err:
            assert interactor.create_update_delete_stage_actions()

        # Assert
        assert err.value.stage_ids_dict == expected_stage_ids_dict
        storage.get_valid_stage_ids\
            .assert_called_once_with(stage_ids=stage_ids)

    @staticmethod
    def test_given_invalid_transition_template_ids_raises_exception():
        # Arrange
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        stage_ids = ["stage_1", "stage_2"]
        transition_ids = ["transition_template_id_1", "transition_template_id_2"]
        storage = create_autospec(StorageInterface)
        template_storage = create_autospec(TaskTemplateStorageInterface)
        storage.get_valid_stage_ids.return_value = ["stage_1", "stage_2"]
        template_storage.get_valid_transition_template_ids.return_value = []
        interactor = CreateUpdateDeleteStageActionsInteractor(
            storage=storage,
            template_storage=template_storage,
            actions_dto=actions_dto
        )

        # Act
        with pytest.raises(InvalidTransitionTemplateIds) as err:
            assert interactor.create_update_delete_stage_actions()

        # Assert

        storage.get_valid_stage_ids \
            .assert_called_once_with(stage_ids=stage_ids)
        template_storage.get_valid_transition_template_ids.\
            assert_called_once_with(transition_ids)

    @staticmethod
    def test_given_invalid_roles_raises_exception(mocker):
        stage_ids = ["stage_1", "stage_2", "stage_3"]
        expected_stage_roles = {
            "stage_1": ["ROLE_1", "ROLE_2"],
            "stage_2": ["ROLE_2"],
            "stage_3": ["ROLE_4"]
        }
        expected_stage_role_dict = json.dumps(expected_stage_roles)
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=3)
        storage = create_autospec(StorageInterface)
        template_storage = create_autospec(TaskTemplateStorageInterface)
        template_storage.get_valid_transition_template_ids.return_value =\
        ["transition_template_id_1", "transition_template_id_2", "transition_template_id_3"]
        stage_ids = ["stage_1", "stage_2", "stage_3"]
        storage.get_valid_stage_ids.return_value = stage_ids
        interactor = CreateUpdateDeleteStageActionsInteractor(
            storage=storage,
            template_storage=template_storage,
            actions_dto=actions_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_invalid_mock
        mocker_obj = prepare_get_roles_for_invalid_mock(mocker)

        from ib_tasks.exceptions.roles_custom_exceptions import InvalidRolesException

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
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        action_dto = StageActionDTOFactory(logic="")
        actions_dto.append(action_dto)
        storage = create_autospec(StorageInterface)
        stage_ids = ["stage_1", "stage_2", "stage_3"]
        template_storage = create_autospec(TaskTemplateStorageInterface)
        template_storage.get_valid_transition_template_ids.return_value = \
            ["transition_template_id_1", "transition_template_id_2", "transition_template_id_3"]
        storage.get_valid_stage_ids.return_value = stage_ids
        interactor = CreateUpdateDeleteStageActionsInteractor(
            storage=storage,
            template_storage=template_storage,
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
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        action_dto = StageActionDTOFactory(button_text="")
        actions_dto.append(action_dto)

        storage = create_autospec(StorageInterface)
        stage_ids = ["stage_1", "stage_2", "stage_3"]
        storage.get_valid_stage_ids.return_value = stage_ids
        interactor = CreateUpdateDeleteStageActionsInteractor(
            storage=storage,
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
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(
            size=2, stage_id="stage_1", button_text="add"
        )
        action_dto = StageActionDTOFactory(stage_id="stage_2", button_text="pay")
        actions_dto.append(action_dto)
        storage = create_autospec(StorageInterface)
        stage_ids = ["stage_1", "stage_2"]
        storage.get_valid_stage_ids.return_value = stage_ids
        interactor = CreateUpdateDeleteStageActionsInteractor(
            storage=storage,
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
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(
            size=2, stage_id="stage_1", action_name="action_name_1"
        )
        action_dto = StageActionDTOFactory(stage_id="stage_2")
        actions_dto.append(action_dto)
        storage = create_autospec(StorageInterface)
        storage.get_valid_stage_ids.return_value = ["stage_1", "stage_2"]
        interactor = CreateUpdateDeleteStageActionsInteractor(
            storage=storage,
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

        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        stage_actions_dto = []
        create_stage_actions_dto = actions_dto
        stage_ids = ["stage_1", "stage_2"]
        storage = create_autospec(StorageInterface)
        storage.get_valid_stage_ids.return_value = stage_ids
        storage.get_stage_action_names.return_value = stage_actions_dto
        interactor = CreateUpdateDeleteStageActionsInteractor(
            storage=storage,
            actions_dto=actions_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        interactor.create_update_delete_stage_actions()

        # Assert
        storage.get_stage_action_names\
            .assert_called_once_with(stage_ids=stage_ids)
        storage.create_stage_actions \
            .assert_called_once_with(stage_actions=create_stage_actions_dto)
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_update_stage_actions_updates_actions(mocker):
        from ib_tasks.tests.factories.interactor_dtos import StageActionDTOFactory
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        from ib_tasks.interactors.storage_interfaces.stage_dtos import StageActionNamesDTO
        stage_actions_dto = [
            StageActionNamesDTO(
                stage_id="stage_1", action_names=["action_name_1"]
            )
        ]
        update_stage_actions_dto = [actions_dto[0]]
        stage_ids = ["stage_1", "stage_2"]
        storage = create_autospec(StorageInterface)
        storage.get_valid_stage_ids.return_value = stage_ids
        storage.get_stage_action_names.return_value = stage_actions_dto
        interactor = CreateUpdateDeleteStageActionsInteractor(
            storage=storage,
            actions_dto=actions_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        interactor.create_update_delete_stage_actions()

        # Assert
        storage.get_stage_action_names\
            .assert_called_once_with(stage_ids=stage_ids)
        storage.update_stage_actions \
            .assert_called_once_with(stage_actions=update_stage_actions_dto)
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_delete_stage_actions_deletes_actions(mocker):
        from ib_tasks.interactors.storage_interfaces.stage_dtos import StageActionNamesDTO
        expected_stage_actions = [
            StageActionNamesDTO(
                stage_id="stage_3", action_names=["action_name_3"]
            )
        ]
        from ib_tasks.tests.factories.interactor_dtos import StageActionDTOFactory
        StageActionDTOFactory.reset_sequence(0)
        actions_dto = StageActionDTOFactory.create_batch(size=2)
        stage_actions_dto = [
            StageActionNamesDTO(
                stage_id="stage_1", action_names=["action_name_1"]
            ),
            StageActionNamesDTO(
                stage_id="stage_3", action_names=["action_name_3"]
            )
        ]
        update_stage_actions_dto = [actions_dto[0]]
        stage_ids = ["stage_1", "stage_2"]
        storage = create_autospec(StorageInterface)
        storage.get_valid_stage_ids.return_value = stage_ids
        storage.get_stage_action_names.return_value = stage_actions_dto
        interactor = CreateUpdateDeleteStageActionsInteractor(
            storage=storage,
            actions_dto=actions_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        interactor.create_update_delete_stage_actions()

        # Assert
        storage.get_stage_action_names\
            .assert_called_once_with(stage_ids=stage_ids)
        storage.update_stage_actions \
            .assert_called_once_with(stage_actions=update_stage_actions_dto)
        storage.delete_stage_actions \
            .assert_called_once_with(stage_actions=expected_stage_actions)
        mocker_obj.assert_called_once()
