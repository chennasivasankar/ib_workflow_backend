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
from ib_tasks.interactors.create_update_task_template_stage_actions_interactor \
    import CreateUpdateTaskTemplateStageActionsInteractor
from ib_tasks.tests.factories.interactor_dtos \
    import TaskTemplateStageActionDTOFactory


class TestCreateUpdateTasksInteractor:

    @staticmethod
    def test_given_invalid_task_template_ids_raises_exception():
        # Arrange
        expected_task_template_ids = ["task_template_2"]
        expected_task_ids_dict = json.dumps(
            {"task_template_ids": expected_task_template_ids}
        )
        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(size=2)
        stage_ids = ["stage_1", "stage_2"]
        storage = create_autospec(StorageInterface)
        task_template_ids = ["task_template_1", "task_template_2"]
        storage.get_valid_task_template_ids.return_value = ["task_template_1"]
        storage.get_valid_stage_ids.return_value = ["stage_1", "stage_2"]

        interactor = CreateUpdateTaskTemplateStageActionsInteractor(
            storage=storage,
            tasks_dto=tasks_dto
        )
        from ib_tasks.exceptions.custom_exceptions \
            import InvalidTaskTemplateId

        # Act
        with pytest.raises(InvalidTaskTemplateId) as err:
            assert interactor.create_update_tasks()

        # Assert
        assert err.value.task_template_ids_dict == expected_task_ids_dict
        storage.get_valid_task_template_ids \
            .assert_called_once_with(task_template_ids=task_template_ids)

    @staticmethod
    def test_given_invalid_stage_ids_raises_exception():
        # Arrange
        expected_stage_ids = ["stage_2"]
        expected_stage_ids_dict = json.dumps(
            {"invalid_stage_ids": expected_stage_ids}
        )
        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(size=2)
        stage_ids = ["stage_1", "stage_2"]
        storage = create_autospec(StorageInterface)
        task_template_ids = ["task_template_1", "task_template_2"]
        storage.get_valid_task_template_ids.return_value = task_template_ids
        storage.get_valid_stage_ids.return_value = ["stage_1"]

        interactor = CreateUpdateTaskTemplateStageActionsInteractor(
            storage=storage,
            tasks_dto=tasks_dto
        )
        from ib_tasks.exceptions.custom_exceptions \
            import InvalidStageIdsException

        # Act
        with pytest.raises(InvalidStageIdsException) as err:
            assert interactor.create_update_tasks()

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
        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(size=3)
        storage = create_autospec(StorageInterface)
        stage_ids = ["stage_1", "stage_2", "stage_3"]
        task_template_ids = [
            "task_template_1", "task_template_2", "task_template_3"
        ]
        storage.get_valid_task_template_ids.return_value = task_template_ids
        storage.get_valid_stage_ids.return_value = stage_ids

        interactor = CreateUpdateTaskTemplateStageActionsInteractor(
            storage=storage,
            tasks_dto=tasks_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_invalid_mock
        mocker_obj = prepare_get_roles_for_invalid_mock(mocker)

        from ib_tasks.exceptions.custom_exceptions \
            import InvalidRolesException

        # Act
        with pytest.raises(InvalidRolesException) as err:
            interactor.create_update_tasks()

        # Assert
        assert err.value.stage_roles_dict == expected_stage_role_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_empty_stage_display_logic_raises_exception(mocker):
        expected_stage_ids = {"stage_ids": ["stage_3"]}
        expected_stage_ids_dict = json.dumps(expected_stage_ids)
        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(size=2)
        task_dto = TaskTemplateStageActionDTOFactory(logic="")
        tasks_dto.append(task_dto)
        storage = create_autospec(StorageInterface)
        stage_ids = ["stage_1", "stage_2", "stage_3"]
        storage.get_valid_stage_ids.return_value = stage_ids
        task_template_ids = [
            "task_template_1", "task_template_2", "task_template_3"
        ]
        storage.get_valid_task_template_ids.return_value = task_template_ids

        interactor = CreateUpdateTaskTemplateStageActionsInteractor(
            storage=storage,

            tasks_dto=tasks_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(EmptyStageDisplayLogic) as err:
            interactor.create_update_tasks()

        assert err.value.stage_ids_dict == expected_stage_ids_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_empty_stage_button_text_raises_exception(mocker):
        expected_stage_ids = {"stage_ids": ["stage_3"]}
        expected_stage_ids_dict = json.dumps(expected_stage_ids)
        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(size=2)
        task_dto = TaskTemplateStageActionDTOFactory(button_text="")
        tasks_dto.append(task_dto)

        storage = create_autospec(StorageInterface)
        stage_ids = ["stage_1", "stage_2", "stage_3"]
        storage.get_valid_stage_ids.return_value = stage_ids
        task_template_ids = [
            "task_template_1", "task_template_2", "task_template_3"
        ]
        storage.get_valid_task_template_ids.return_value = task_template_ids

        interactor = CreateUpdateTaskTemplateStageActionsInteractor(
            storage=storage,

            tasks_dto=tasks_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(EmptyStageButtonText) as err:
            interactor.create_update_tasks()

        assert err.value.stage_ids_dict == expected_stage_ids_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_duplicate_stage_buttons_raises_exception(mocker):
        expected_stage_buttons = {
            "stage_1": ["add"]
        }
        expected_stage_buttons_dict = json.dumps(expected_stage_buttons)
        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(
            size=2, stage_id="stage_1", button_text="add"
        )
        task_dto = TaskTemplateStageActionDTOFactory(
            stage_id="stage_2", button_text="pay")
        tasks_dto.append(task_dto)
        storage = create_autospec(StorageInterface)
        stage_ids = ["stage_1", "stage_2"]
        storage.get_valid_stage_ids.return_value = stage_ids
        task_template_ids = [
            "task_template_1", "task_template_2", "task_template_3"
        ]
        storage.get_valid_task_template_ids.return_value = task_template_ids

        interactor = CreateUpdateTaskTemplateStageActionsInteractor(
            storage=storage,

            tasks_dto=tasks_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(DuplicateStageButtonsException) as err:
            interactor.create_update_tasks()

        assert err.value.stage_buttons_dict == expected_stage_buttons_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_duplicate_stage_action_names_raises_exception(mocker):
        expected_stage_actions = {
            "stage_1": ["action_name_1"]
        }
        expected_stage_actions_dict = json.dumps(expected_stage_actions)
        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(
            size=2, stage_id="stage_1", action_name="action_name_1"
        )
        task_dto = TaskTemplateStageActionDTOFactory(stage_id="stage_2")
        tasks_dto.append(task_dto)
        storage = create_autospec(StorageInterface)
        storage.get_valid_stage_ids.return_value = ["stage_1", "stage_2"]
        task_template_ids = [
            "task_template_1", "task_template_2", "task_template_3"
        ]
        storage.get_valid_task_template_ids.return_value = task_template_ids

        interactor = CreateUpdateTaskTemplateStageActionsInteractor(
            storage=storage,
            tasks_dto=tasks_dto
        )

        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        with pytest.raises(DuplicateStageActionNamesException) as err:
            interactor.create_update_tasks()

        assert err.value.stage_actions == expected_stage_actions_dict
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_valid_create_tasks_dto_creates_tasks(mocker):

        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(size=2)
        stage_actions_dto = []
        create_tasks_dto = tasks_dto
        stage_ids = ["stage_1", "stage_2"]
        storage = create_autospec(StorageInterface)
        storage.get_valid_stage_ids.return_value = stage_ids
        storage.get_stage_action_names.return_value = stage_actions_dto
        task_template_ids = ["task_template_1", "task_template_2"]
        storage.get_valid_task_template_ids.return_value = task_template_ids
        interactor = CreateUpdateTaskTemplateStageActionsInteractor(
            storage=storage, tasks_dto=tasks_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        interactor.create_update_tasks()

        # Assert
        storage.get_stage_action_names \
            .assert_called_once_with(stage_ids=stage_ids)
        storage.create_task_template_stage_actions \
            .assert_called_once_with(tasks_dto=create_tasks_dto)
        mocker_obj.assert_called_once()

    @staticmethod
    def test_given_valid_update_tasks_dto_updates_tasks(mocker):
        TaskTemplateStageActionDTOFactory.reset_sequence(0)
        tasks_dto = TaskTemplateStageActionDTOFactory.create_batch(size=2)
        from ib_tasks.interactors.storage_interfaces.dtos \
            import StageActionNamesDTO
        stage_actions_dto = [
            StageActionNamesDTO(
                stage_id="stage_1", action_names=["action_name_1"]
            )
        ]
        update_tasks_dto = [tasks_dto[0]]
        stage_ids = ["stage_1", "stage_2"]
        storage = create_autospec(StorageInterface)
        storage.get_valid_stage_ids.return_value = stage_ids
        storage.get_stage_action_names.return_value = stage_actions_dto
        task_template_ids = ["task_template_1", "task_template_2"]
        storage.get_valid_task_template_ids.return_value = task_template_ids
        interactor = CreateUpdateTaskTemplateStageActionsInteractor(
            storage=storage, tasks_dto=tasks_dto
        )
        from ib_tasks.tests.common_fixtures.adapters.roles_service \
            import prepare_get_roles_for_valid_mock
        mocker_obj = prepare_get_roles_for_valid_mock(mocker)

        # Act
        interactor.create_update_tasks()

        # Assert
        storage.get_stage_action_names \
            .assert_called_once_with(stage_ids=stage_ids)
        storage.update_task_template_stage_actions \
            .assert_called_once_with(tasks_dto=update_tasks_dto)
        mocker_obj.assert_called_once()
