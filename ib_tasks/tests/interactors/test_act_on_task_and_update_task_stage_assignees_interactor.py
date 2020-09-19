import datetime
from unittest.mock import patch

import mock
import pytest
from freezegun import freeze_time

from ib_tasks.interactors.update_task_stage_assignees_interactor import \
    UpdateTaskStageAssigneesInteractor
from ib_tasks.interactors.user_action_on_task.user_action_on_task_interactor import \
    UserActionOnTaskInteractor
from ib_tasks.tests.factories.interactor_dtos import StageAssigneeDTOFactory, \
    FieldDisplayDTOFactory, TaskCurrentStageDetailsDTOFactory


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

    @pytest.fixture
    def assignees(self):
        from ib_tasks.interactors.stage_dtos import TaskStageAssigneeDetailsDTO
        from ib_tasks.adapters.dtos import AssigneeDetailsDTO
        return TaskStageAssigneeDetailsDTO(
            task_id=1,
            stage_id='stage_id_1',
            assignee_details=AssigneeDetailsDTO(assignee_id='1',
                                                name='name',
                                                profile_pic_url='pavan.com')
        )

    @pytest.fixture()
    def task_complete_details(self, assignees):
        task_display_id = "task_1"
        task_id = 1
        task_complete_details = self.prepare_task_complete_details(
            task_id=task_id, assignees=assignees,
            task_display_id=task_display_id
        )
        return task_complete_details

    @staticmethod
    def prepare_task_complete_details(task_id, assignees,
                                      task_display_id):
        from ib_tasks.interactors.presenter_interfaces.dtos \
            import TaskCompleteDetailsDTO
        from ib_tasks.tests.common_fixtures.interactors \
            import prepare_task_boards_details
        task_board_details = prepare_task_boards_details()
        from ib_tasks.interactors.stage_dtos import TaskStageDTO
        from ib_tasks.tests.factories.storage_dtos import ActionDTOFactory
        return TaskCompleteDetailsDTO(
            task_id=task_id,
            task_display_id=task_display_id,
            task_boards_details=task_board_details,
            actions_dto=[ActionDTOFactory()],
            field_dtos=[FieldDisplayDTOFactory()],
            assignees_details=[assignees],
            task_stage_details=[
                TaskStageDTO(
                    stage_id='stage_1', db_stage_id=1,
                    display_name='display_name',
                    stage_colour='blue')
            ]
        )

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

    @freeze_time("2020-01-1 05:21:34")
    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_scenario_when_task_due_date_is_not_updated_raises_exception(
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
        stage_display_name = "stage_1"
        due_date = datetime.datetime.now()
        from ib_tasks.exceptions.task_custom_exceptions import \
            TaskDelayReasonIsNotUpdated
        exception_object = TaskDelayReasonIsNotUpdated(
            task_display_id=task_display_id, due_date=due_date,
            stage_display_name=stage_display_name)
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
        presenter_mock.get_response_for_task_delay_reason_not_updated. \
            assert_called_once_with(exception_object)

    @patch.object(UpdateTaskStageAssigneesInteractor,
                  'validate_and_update_task_stage_assignees')
    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_invalid_stages_raises_exception(
            self, user_action_on_task_mock, update_task_stage_assignees_mock,
            field_storage_mock, storage_mock, mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            task_complete_details):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        stage_ids = [1, 2]
        stage_assignees_dto = StageAssigneeDTOFactory.create_batch(
            2, db_stage_id=1)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        task_current_stages_details = TaskCurrentStageDetailsDTOFactory()
        user_action_on_task_mock.return_value = (
            task_complete_details, task_current_stages_details, None,
            stage_ids)
        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidDbStageIdsListException
        exception_object = InvalidDbStageIdsListException(invalid_stage_ids=
                                                          stage_ids)
        update_task_stage_assignees_mock.side_effect = exception_object
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
        presenter_mock.raise_invalid_stage_ids_exception. \
            assert_called_once_with(invalid_stage_ids=stage_ids)

    @patch.object(UpdateTaskStageAssigneesInteractor,
                  'validate_and_update_task_stage_assignees')
    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_virtual_stages_for_updating_assignees_raises_exception(
            self, user_action_on_task_mock, update_task_stage_assignees_mock,
            field_storage_mock, storage_mock, mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            task_complete_details):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        stage_ids = [1, 2]
        stage_assignees_dto = StageAssigneeDTOFactory.create_batch(
            2, db_stage_id=1)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        task_current_stages_details = TaskCurrentStageDetailsDTOFactory()
        user_action_on_task_mock.return_value = (
            task_complete_details, task_current_stages_details, None,
            stage_ids)
        from ib_tasks.exceptions.stage_custom_exceptions import \
            VirtualStageIdsException
        exception_object = VirtualStageIdsException(virtual_stage_ids=
                                                    stage_ids)
        update_task_stage_assignees_mock.side_effect = exception_object
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
        presenter_mock.raise_virtual_stage_ids_exception. \
            assert_called_once_with(virtual_stage_ids=stage_ids)

    @patch.object(UpdateTaskStageAssigneesInteractor,
                  'validate_and_update_task_stage_assignees')
    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_user_not_member_of_project_raises_exception(
            self, user_action_on_task_mock, update_task_stage_assignees_mock,
            field_storage_mock, storage_mock, mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            task_complete_details):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        stage_ids = [1, 2]
        stage_assignees_dto = StageAssigneeDTOFactory.create_batch(
            2, db_stage_id=1)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        task_current_stages_details = TaskCurrentStageDetailsDTOFactory()
        user_action_on_task_mock.return_value = (
            task_complete_details, task_current_stages_details, None,
            stage_ids)
        from ib_tasks.adapters.roles_service import \
            UserNotAMemberOfAProjectException
        exception_object = UserNotAMemberOfAProjectException()
        update_task_stage_assignees_mock.side_effect = exception_object
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
        presenter_mock.get_response_for_user_not_in_project. \
            assert_called_once()

    @patch.object(UpdateTaskStageAssigneesInteractor,
                  'validate_and_update_task_stage_assignees')
    @patch.object(UserActionOnTaskInteractor,
                  'user_action_on_task')
    def test_given_assignees_who_not_having_permission_raises_exception(
            self, user_action_on_task_mock, update_task_stage_assignees_mock,
            field_storage_mock, storage_mock, mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            task_complete_details):
        # Arrange
        task_display_id = "IBWF-1"
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        stage_ids = [1, 2]
        stage_assignees_dto = StageAssigneeDTOFactory.create_batch(
            2, db_stage_id=1)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        task_current_stages_details = TaskCurrentStageDetailsDTOFactory()
        user_action_on_task_mock.return_value = (
            task_complete_details, task_current_stages_details, None,
            stage_ids)
        from ib_tasks.exceptions.stage_custom_exceptions import \
            StageIdsWithInvalidPermissionForAssignee
        exception_object = StageIdsWithInvalidPermissionForAssignee(
            invalid_stage_ids=stage_ids)
        update_task_stage_assignees_mock.side_effect = exception_object
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
        presenter_mock. \
            raise_stage_ids_with_invalid_permission_for_assignee_exception. \
            assert_called_once_with(invalid_stage_ids=stage_ids)

    @patch.object(UserActionOnTaskInteractor, 'user_action_on_task')
    def test_given_valid_details(
            self, user_action_on_task_mock,
            field_storage_mock, storage_mock, mock_object,
            stage_storage_mock, action_storage_mock, task_storage_mock,
            presenter_mock, task_stage_storage_mock, create_task_storage_mock,
            elastic_storage_mock, gof_storage_mock, task_template_storage_mock,
            task_complete_details):
        # Arrange
        task_display_id = "IBWF-1"
        task_id = 1
        action_id = 1
        board_id = "board_1"
        user_id = "user_1"
        stage_ids = ["stage_id_1", "stage_id_2", "stage_id_3"]
        stage_assignees_dto = StageAssigneeDTOFactory.create_batch(
            2, db_stage_id=1)
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        task_storage_mock.get_task_id_for_task_display_id.return_value = task_id
        task_current_stages_details = TaskCurrentStageDetailsDTOFactory()
        user_action_on_task_mock.return_value = (
            task_complete_details, task_current_stages_details, None,
            stage_ids)
        stage_storage_mock.get_stage_ids_excluding_virtual_stages. \
            return_value = ["stage_id_1", "stage_id_2"]

        stage_storage_mock.get_virtual_stages_already_having_in_task.return_value = []
        stage_storage_mock. \
            get_db_stage_ids_for_given_stage_ids.return_value = [3]
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

        task_stage_storage_mock. \
            create_task_stage_history_records_for_virtual_stages. \
            assert_called_once_with(stage_ids=[3], task_id=task_id)
