import mock
from unittest.mock import patch
import pytest

from ib_tasks.interactors.get_task_current_board_complete_details_interactor import \
    GetTaskCurrentBoardCompleteDetailsInteractor
from ib_tasks.interactors.user_action_on_task_interactor import \
    UserActionOnTaskInteractor
from ib_tasks.tests.factories.interactor_dtos import StageAssigneeDTOFactory


class TestActOnTaskAndUpdateTaskStageAssigneesInteractor:
    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageAssigneeDTOFactory.reset_sequence()

    @pytest.fixture
    def task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        return mock.create_autospec(TaskStorageInterface)

    @pytest.fixture
    def gof_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.gof_storage_interface \
            import GoFStorageInterface
        return mock.create_autospec(GoFStorageInterface)

    @pytest.fixture
    def task_template_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_template_storage_interface import \
            TaskTemplateStorageInterface
        return mock.create_autospec(TaskTemplateStorageInterface)

    @pytest.fixture
    def create_task_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .create_or_update_task_storage_interface import \
            CreateOrUpdateTaskStorageInterface
        return mock.create_autospec(CreateOrUpdateTaskStorageInterface)

    @pytest.fixture
    def storage_mock(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        return mock.create_autospec(StorageInterface)

    @pytest.fixture
    def field_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .fields_storage_interface import \
            FieldsStorageInterface
        return mock.create_autospec(FieldsStorageInterface)

    @pytest.fixture
    def stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .stages_storage_interface import StageStorageInterface
        return mock.create_autospec(StageStorageInterface)

    @pytest.fixture
    def action_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .action_storage_interface import ActionStorageInterface
        return mock.create_autospec(ActionStorageInterface)

    @pytest.fixture
    def elastic_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .elastic_storage_interface import ElasticSearchStorageInterface
        return mock.create_autospec(ElasticSearchStorageInterface)

    @pytest.fixture
    def task_stage_storage_mock(self):
        from ib_tasks.interactors.storage_interfaces \
            .task_stage_storage_interface import \
            TaskStageStorageInterface
        return mock.create_autospec(TaskStageStorageInterface)

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces. \
            act_on_task_and_upadte_task_stage_assignees_presenter_interface import \
            ActOnTaskAndUpdateTaskStageAssigneesPresenterInterface
        return mock.create_autospec(
            ActOnTaskAndUpdateTaskStageAssigneesPresenterInterface)

    @pytest.fixture
    def user_action_on_task_mock(self, mocker):
        path = "ib_tasks.interactors.user_action_on_task_interactor" \
               ".UserActionOnTaskInteractor.act_on_task"
        return mocker.patch(path)

    @pytest.fixture
    def stage_assignees_dto(self):
        return StageAssigneeDTOFactory.create_batch(2)

    @pytest.fixture
    def mock_object(self):
        from unittest.mock import Mock
        mock_object = Mock()
        return mock_object

    def test_given_invalid_task_display_id_raise_exception(
            self, field_storage_mock, storage_mock, mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskDisplayId

        task_display_id = "IBWF-1"
        action_id = 1
        board_id = None
        user_id = "user_1"
        exception_object = InvalidTaskDisplayId(task_display_id)
        task_storage_mock.check_is_valid_task_display_id.return_value = False

        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        presenter_mock.raise_invalid_task_display_id.return_value = \
            mock_object

        # Assert
        call_tuple = presenter_mock.raise_invalid_task_display_id.call_args
        error_obj = call_tuple.args[0]
        assert error_obj.task_display_id == exception_object.task_display_id

    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_invalid_board_raises_exception(
            self, user_action_on_task, field_storage_mock, storage_mock,
            mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        from ib_tasks.interactors.user_action_on_task_interactor import \
            InvalidBoardIdException
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        exception_object = InvalidBoardIdException(board_id=board_id)
        user_action_on_task.side_effect = exception_object
        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)
        # Assert
        presenter_mock.raise_exception_for_invalid_board. \
            assert_called_once_with(error_obj=exception_object)

    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_invalid_action_raises_exception(
            self, user_action_on_task, field_storage_mock, storage_mock,
            mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException
        exception_object = InvalidActionException(action_id=action_id)
        user_action_on_task.side_effect = exception_object
        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        # Assert
        presenter_mock.raise_exception_for_invalid_action. \
            assert_called_once_with(error_obj=exception_object)

    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_invalid_action_raises_exception(
            self, user_action_on_task, field_storage_mock, storage_mock,
            mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException
        exception_object = InvalidActionException(action_id=action_id)
        user_action_on_task.side_effect = exception_object
        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        # Assert
        presenter_mock.raise_exception_for_invalid_action. \
            assert_called_once_with(error_obj=exception_object)

    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_invalid_present_stage_action_raises_exception(
            self, user_action_on_task, field_storage_mock, storage_mock,
            mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidPresentStageAction
        exception_object = InvalidPresentStageAction(action_id=action_id)
        user_action_on_task.side_effect = exception_object
        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        # Assert
        presenter_mock.raise_exception_for_invalid_present_actions. \
            assert_called_once_with(error_obj=exception_object)

    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_user_permission_denied_raises_exception(
            self, user_action_on_task, field_storage_mock, storage_mock,
            mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserActionPermissionDenied
        exception_object = UserActionPermissionDenied(action_id=action_id)
        user_action_on_task.side_effect = exception_object
        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        # Assert
        presenter_mock.raise_exception_for_user_action_permission_denied. \
            assert_called_once_with(error_obj=exception_object)

    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_unfilled_details_for_gofs_raises_exception(
            self, user_action_on_task, field_storage_mock, storage_mock,
            mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        from ib_tasks.exceptions.gofs_custom_exceptions import \
            UserDidNotFillRequiredGoFs
        exception_object = UserDidNotFillRequiredGoFs(gof_display_names=[])
        user_action_on_task.side_effect = exception_object
        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        # Assert
        presenter_mock.raise_user_did_not_fill_required_gofs. \
            assert_called_once_with(exception_object)

    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_unfilled_details_for_fields_raises_exception(
            self, user_action_on_task, field_storage_mock, storage_mock,
            mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        from ib_tasks.exceptions.fields_custom_exceptions import \
            UserDidNotFillRequiredFields
        exception_object = UserDidNotFillRequiredFields(unfilled_field_dtos=[])
        user_action_on_task.side_effect = exception_object
        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        # Assert
        presenter_mock.raise_user_did_not_fill_required_fields. \
            assert_called_once_with(exception_object)

    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_user_board_permission_denied_raises_exception(
            self, user_action_on_task,
            field_storage_mock, storage_mock, mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserBoardPermissionDenied
        exception_object = UserBoardPermissionDenied(board_id=board_id)
        user_action_on_task.side_effect = exception_object
        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        # Assert
        presenter_mock.raise_exception_for_user_board_permission_denied. \
            assert_called_once_with(exception_object)

    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_invalid_key_raises_exception(
            self, user_action_on_task,
            field_storage_mock, storage_mock, mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidKeyError
        exception_object = InvalidKeyError()
        user_action_on_task.side_effect = exception_object
        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        # Assert
        presenter_mock.raise_invalid_key_error.assert_called_once()

    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_invalid_custom_logic_raises_exception(
            self, user_action_on_task,
            field_storage_mock, storage_mock, mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidCustomLogicException
        exception_object = InvalidCustomLogicException()
        user_action_on_task.side_effect = exception_object
        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        # Assert
        presenter_mock.raise_invalid_custom_logic_function_exception.assert_called_once()

    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_invalid_module_path_raises_exception(
            self, user_action_on_task,
            field_storage_mock, storage_mock, mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        path_name = "ib_tasks.populate.stage_ac.stage_1_action_name_1"
        from ib_tasks.exceptions.custom_exceptions import \
            InvalidModulePathFound
        exception_object = InvalidModulePathFound(path_name=path_name)
        user_action_on_task.side_effect = exception_object
        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        # Assert
        presenter_mock.raise_invalid_path_not_found_exception.assert_called_once()

    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_user_who_is_not_in_project_raises_exception(
            self, user_action_on_task,
            field_storage_mock, storage_mock, mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        from ib_tasks.exceptions.adapter_exceptions import \
            UserIsNotInProjectException
        exception_object = UserIsNotInProjectException()
        user_action_on_task.side_effect = exception_object
        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        # Assert
        presenter_mock.get_response_for_user_not_in_project.assert_called_once()

    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_user_who_is_not_in_project_raises_exception(
            self, user_action_on_task,
            field_storage_mock, storage_mock, mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            stage_assignees_dto):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        method_name = "stage_1_action_name_1"
        from ib_tasks.exceptions.custom_exceptions import InvalidMethodFound
        exception_object = InvalidMethodFound(method_name=method_name)
        user_action_on_task.side_effect = exception_object
        from ib_tasks.interactors. \
            act_on_task_and_update_task_stage_assignees_interactor import \
            ActOnTaskAndUpdateTaskStageAssigneesInteractor
        interactor = ActOnTaskAndUpdateTaskStageAssigneesInteractor(
            storage=storage_mock, action_storage=action_storage_mock,
            stage_storage=stage_storage_mock, task_storage=task_storage_mock,
            task_stage_storage=task_stage_storage_mock,
            create_task_storage=create_task_storage_mock,
            field_storage=field_storage_mock,
            elasticsearch_storage=elastic_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            action_id=action_id, board_id=board_id, user_id=user_id)

        # Act
        interactor \
            .act_on_task_interactor_and_update_task_stage_assignees_wrapper(
            task_display_id=task_display_id, presenter=presenter_mock,
            stage_assignee_dtos=stage_assignees_dto)

        # Assert
        presenter_mock.raise_invalid_method_not_found_exception.\
            assert_called_once_with(method_name=method_name)
