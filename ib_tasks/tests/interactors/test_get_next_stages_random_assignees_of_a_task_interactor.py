import pytest
from unittest.mock import create_autospec, patch
from ib_tasks.interactors.call_action_logic_function_and_get_status_variables_interactor import \
    CallActionLogicFunctionAndGetTaskStatusVariablesInteractor
from ib_tasks.interactors.get_next_stages_random_assignees_of_a_task_interactor import \
    GetNextStagesRandomAssigneesOfATaskInteractor, InvalidModulePathFound, \
    InvalidMethodFound
from ib_tasks.interactors.get_task_stage_logic_satisfied_next_stages_given_status_vars import \
    GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor
from ib_tasks.interactors.get_users_with_less_tasks_for_stages import \
    GetUsersWithLessTasksInGivenStagesInteractor


class TestGetNextStagesRandomAssigneesOfATaskInteractor:
    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        storage = create_autospec(
            StorageInterface)
        return storage

    @pytest.fixture
    def stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
            StageStorageInterface
        stage_storage = create_autospec(
            StageStorageInterface)
        return stage_storage

    @pytest.fixture
    def task_stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import \
            TaskStageStorageInterface
        task_stage_storage = create_autospec(
            TaskStageStorageInterface)
        return task_stage_storage

    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
            TaskStorageInterface
        task_storage = create_autospec(
            TaskStorageInterface)
        return task_storage

    @staticmethod
    def stage_display_mock(mocker):
        path = 'ib_tasks.interactors.get_stage_display_logic_interactor.StageDisplayLogicInteractor' \
               '.get_stage_display_logic_condition'
        mock_obj = mocker.patch(path)
        return mock_obj

    @pytest.fixture
    def action_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
            ActionStorageInterface
        action_storage = create_autospec(
            ActionStorageInterface)
        return action_storage

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces. \
            get_next_stages_random_assignees_of_a_task_presenter import \
            GetNextStagesRandomAssigneesOfATaskPresenterInterface
        presenter_mock = create_autospec(
            GetNextStagesRandomAssigneesOfATaskPresenterInterface)
        return presenter_mock

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

    @pytest.fixture
    def mock_object(self):
        from unittest.mock import Mock
        mock_object = Mock()
        return mock_object

    def test_given_invalid_task_display_id_raise_exception(self, mock_object,
                                                           storage_mock,
                                                           stage_storage_mock,
                                                           action_storage_mock,
                                                           task_storage_mock,
                                                           presenter_mock,
                                                           task_stage_storage_mock):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskDisplayId

        task_display_id = "IBWF-1"
        action_id = 1
        exception_object = InvalidTaskDisplayId(task_display_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = False

        interactor = GetNextStagesRandomAssigneesOfATaskInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock)

        # Act
        interactor \
            .get_next_stages_random_assignees_of_a_task_wrapper(
            action_id=action_id, task_display_id=task_display_id,
            presenter=presenter_mock)

        presenter_mock.raise_invalid_task_display_id.return_value = \
            mock_object

        # Assert
        call_tuple = presenter_mock.raise_invalid_task_display_id.call_args
        error_obj = call_tuple.args[0]
        assert error_obj.task_display_id == exception_object.task_display_id

    def test_given_invalid_action_id_raise_exception(
            self, mock_object, storage_mock, stage_storage_mock,
            action_storage_mock, task_storage_mock, presenter_mock,
            task_stage_storage_mock):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException
        exception_object = InvalidActionException(action_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = False

        interactor = GetNextStagesRandomAssigneesOfATaskInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock)

        # Act
        interactor \
            .get_next_stages_random_assignees_of_a_task_wrapper(
            action_id=action_id, task_display_id=task_display_id,
            presenter=presenter_mock)

        presenter_mock.raise_exception_for_invalid_action.return_value = \
            mock_object

        # Assert
        call_tuple = presenter_mock.raise_exception_for_invalid_action.call_args
        error_obj = call_tuple.args[0]
        assert error_obj.task_display_id == exception_object.action_id

    @patch.object(CallActionLogicFunctionAndGetTaskStatusVariablesInteractor,
                  'get_status_variables_dtos_of_task_based_on_action')
    def test_given_invalid_path_raises_exception(self, action_logic_mock,
                                                 storage_mock,
                                                 stage_storage_mock,
                                                 action_storage_mock,
                                                 task_storage_mock,
                                                 presenter_mock,
                                                 task_stage_storage_mock):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        path_name = "ib_tasks.populate.stage_ac.stage_1_action_name_1"
        exception_object = InvalidModulePathFound(path_name)
        action_logic_mock.side_effect = exception_object
        interactor = GetNextStagesRandomAssigneesOfATaskInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock)

        # Act
        interactor \
            .get_next_stages_random_assignees_of_a_task_wrapper(
            action_id=action_id, task_display_id=task_display_id,
            presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_path_not_found_exception. \
            assert_called_once_with(path_name=path_name)

    @staticmethod
    @patch.object(CallActionLogicFunctionAndGetTaskStatusVariablesInteractor,
                  'get_status_variables_dtos_of_task_based_on_action')
    def test_given_invalid_method_name_raises_exception(action_logic_mock,
                                                        storage_mock,
                                                        stage_storage_mock,
                                                        action_storage_mock,
                                                        task_storage_mock,
                                                        presenter_mock,
                                                        task_stage_storage_mock):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1

        method_name = "stage_1_action_name_1"
        action_logic_mock.side_effect = InvalidMethodFound(
            method_name=method_name
        )

        interactor = GetNextStagesRandomAssigneesOfATaskInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock)

        # Act
        interactor \
            .get_next_stages_random_assignees_of_a_task_wrapper(
            action_id=action_id, task_display_id=task_display_id,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_invalid_method_not_found_exception. \
            assert_called_once_with(method_name=method_name)

    @staticmethod
    @patch.object(CallActionLogicFunctionAndGetTaskStatusVariablesInteractor,
                  'get_status_variables_dtos_of_task_based_on_action')
    def test_access_invalid_key_raises_invalid_key_error(action_logic_mock,
                                                         storage_mock,
                                                         presenter_mock,
                                                         stage_storage_mock,
                                                         action_storage_mock,
                                                         task_storage_mock,
                                                         task_stage_storage_mock):
        # Arrange
        action_id = 1
        task_display_id = "IBWF-1"

        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidKeyError
        action_logic_mock.side_effect = InvalidKeyError()

        interactor = GetNextStagesRandomAssigneesOfATaskInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock)

        # Act
        interactor \
            .get_next_stages_random_assignees_of_a_task_wrapper(
            action_id=action_id, task_display_id=task_display_id,
            presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_key_error.assert_called_once()

    # @patch.object(GetUsersWithLessTasksInGivenStagesInteractor,
    #               'get_users_with_less_tasks_in_given_stages')
    # @patch.object(
    #     GetTaskStageLogicSatisfiedNextStagesGivenStatusVarsInteractor,
    #     'get_task_stage_logic_satisfied_next_stages')
    # @patch.object(CallActionLogicFunctionAndGetTaskStatusVariablesInteractor,
    #               'get_status_variables_dtos_of_task_based_on_action')
    # def test_given_valid_details_get_next_stage_assignees(
    #         self, action_logic_mock, next_stages_mock,
    #         users_with_less_tasks_mock, storage_mock,
    #         presenter_mock, stage_storage_mock, action_storage_mock,
    #         task_storage_mock, task_stage_storage_mock):
    #     # Arrange
    #
    #     task_display_id = "IBWF-1"
    #     action_id = 1
    #     task_storage_mock.check_is_valid_task_display_id.return_value = True
    #     task_storage_mock.get_task_id_for_task_display_id.return_value=1
