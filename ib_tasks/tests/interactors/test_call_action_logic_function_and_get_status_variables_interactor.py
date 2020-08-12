import pytest
from mock import create_autospec

from ib_tasks.exceptions.custom_exceptions import InvalidModulePathFound, \
    InvalidMethodFound
from ib_tasks.interactors.call_action_logic_function_and_get_status_variables_interactor import \
    CallActionLogicFunctionAndGetTaskStatusVariablesInteractor
from ib_tasks.tests.factories.storage_dtos import StatusVariableDTOFactory


class TestCallActionLogicFunctionAndGetTaskStatusVariablesInteractor:
    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        storage = create_autospec(
            StorageInterface)
        return storage

    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
            TaskStorageInterface
        task_storage = create_autospec(
            TaskStorageInterface)
        return task_storage

    @pytest.fixture
    def action_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
            ActionStorageInterface
        action_storage = create_autospec(
            ActionStorageInterface)
        return action_storage

    @staticmethod
    def stage_display_mock(mocker):
        path = 'ib_tasks.interactors.get_stage_display_logic_interactor.StageDisplayLogicInteractor' \
               '.get_stage_display_logic_condition'
        mock_obj = mocker.patch(path)
        return mock_obj

    @staticmethod
    @pytest.fixture()
    def stage_display_value():
        from ib_tasks.tests.factories.storage_dtos \
            import StageDisplayValueDTOFactory
        StageDisplayValueDTOFactory.reset_sequence(0)
        stage_values = [
            StageDisplayValueDTOFactory(),
            StageDisplayValueDTOFactory(),
            StageDisplayValueDTOFactory()
        ]
        return stage_values

    @staticmethod
    def test_assert_called_with_expected_arguments(mocker, storage_mock,
                                                   action_storage_mock,
                                                   task_storage_mock):
        # Arrange
        mock_task_dict = {'status_variables': {'variable_1': 'stage_1'}}
        action_id = 1
        task_id = 1
        path_name = "ib_tasks.populate.dynamic_logic_test_file.stage_1_action_name_1"
        mock_obj = mocker.patch(path_name)

        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        storage_mock.get_status_variables_to_task.return_value = statuses
        interactor = CallActionLogicFunctionAndGetTaskStatusVariablesInteractor(
            storage=storage_mock, task_storage=task_storage_mock,
            action_storage=action_storage_mock)

        # Act
        interactor \
            .get_status_variables_dtos_of_task_based_on_action(
            action_id=action_id, task_id=task_id)

        # Assert
        storage_mock.get_path_name_to_action.assert_called_once_with(
            action_id=action_id)
        mock_obj.assert_called_once_with(
            task_dict=mock_task_dict, global_constants={},
            stage_value_dict={})
        task_storage_mock.check_is_task_exists.assert_called_once_with(
            task_id=task_id)
        action_storage_mock.validate_action.assert_called_once_with(
            action_id=action_id)
        storage_mock.get_global_constants_to_task \
            .assert_called_once_with(task_id=task_id)
        storage_mock.get_stage_dtos_to_task \
            .assert_called_once_with(task_id=task_id)

    @staticmethod
    def test_given_invalid_path_raises_exception(storage_mock,
                                                 task_storage_mock,
                                                 action_storage_mock):
        # Arrange
        task_id = 1
        action_id = 1
        path_name = "ib_tasks.populate.stage_ac.stage_1_action_name_1"
        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        storage_mock.get_status_variables_to_task.return_value = statuses

        interactor = CallActionLogicFunctionAndGetTaskStatusVariablesInteractor(
            storage=storage_mock, task_storage=task_storage_mock,
            action_storage=action_storage_mock)

        # Act
        with pytest.raises(InvalidModulePathFound) as error:
            interactor \
                .get_status_variables_dtos_of_task_based_on_action(
                action_id=action_id, task_id=task_id)

        # Assert
        assert error.value.path_name == path_name
        storage_mock.get_path_name_to_action.assert_called_once_with(
            action_id=action_id)

    @staticmethod
    def test_given_invalid_method_name_raises_exception(mocker, storage_mock,
                                                        task_storage_mock,
                                                        action_storage_mock):
        # Arrange
        task_id = 1
        action_id = 1

        path_name = "ib_tasks.populate.stage_actions_logic.stage_1_action_name_1"
        mock_obj = mocker.patch("importlib.import_module")
        mock_obj.side_effect = InvalidMethodFound(
            method_name="stage_1_action_name_1")
        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        storage_mock.get_status_variables_to_task.return_value = statuses

        interactor = CallActionLogicFunctionAndGetTaskStatusVariablesInteractor(
            storage=storage_mock, task_storage=task_storage_mock,
            action_storage=action_storage_mock)

        # Act
        with pytest.raises(InvalidMethodFound) as error:
            interactor \
                .get_status_variables_dtos_of_task_based_on_action(
                action_id=action_id, task_id=task_id)

        # Assert
        assert error.value.method_name == "stage_1_action_name_1"
        storage_mock.get_path_name_to_action.assert_called_once_with(
            action_id=action_id)

    @staticmethod
    def test_access_invalid_key_raises_invalid_key_error(storage_mock,
                                                         action_storage_mock,
                                                         task_storage_mock):
        # Arrange
        action_id = 1
        task_id = 1

        path_name = "ib_tasks.populate.dynamic_logic_test_file.stage_1_action_name_1"

        storage_mock.get_path_name_to_action.return_value = path_name
        StatusVariableDTOFactory.reset_sequence()
        statuses = [StatusVariableDTOFactory()]
        storage_mock.get_status_variables_to_task.return_value = statuses

        interactor = CallActionLogicFunctionAndGetTaskStatusVariablesInteractor(
            storage=storage_mock, task_storage=task_storage_mock,
            action_storage=action_storage_mock)
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidKeyError

        # Act
        with pytest.raises(InvalidKeyError):
            interactor \
                .get_status_variables_dtos_of_task_based_on_action(
                action_id=action_id, task_id=task_id)
        # Assert
        storage_mock.get_path_name_to_action.assert_called_once_with(
            action_id=action_id
        )
