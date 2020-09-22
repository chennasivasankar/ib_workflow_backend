import datetime

import factory
import freezegun
import mock
import pytest

from ib_tasks.exceptions.gofs_custom_exceptions import \
    DuplicateSameGoFOrderForAGoF
from ib_tasks.interactors.create_or_update_task.create_task_interactor import \
    CreateTaskInteractor
from ib_tasks.tests.factories.interactor_dtos import GoFFieldsDTOFactory, \
    FieldValuesDTOFactory, CreateTaskDTOFactory, \
    TaskCurrentStageDetailsDTOFactory
from ib_tasks.tests.factories.presenter_dtos import \
    TaskCompleteDetailsDTOFactory, AllTasksOverviewDetailsDTOFactory
from ib_tasks.tests.factories.storage_dtos import TaskGoFDetailsDTOFactory, \
    TaskGoFFieldDTOFactory, FieldIdWithFieldDisplayNameDTOFactory


class TestCreateTaskInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        FieldValuesDTOFactory.reset_sequence()
        GoFFieldsDTOFactory.reset_sequence()
        CreateTaskDTOFactory.reset_sequence()
        TaskGoFFieldDTOFactory.reset_sequence()
        FieldIdWithFieldDisplayNameDTOFactory.reset_sequence()
        TaskCompleteDetailsDTOFactory.reset_sequence()
        TaskCurrentStageDetailsDTOFactory.reset_sequence()
        AllTasksOverviewDetailsDTOFactory.reset_sequence()

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
        from ib_tasks.interactors.presenter_interfaces.create_task_presenter \
            import CreateTaskPresenterInterface
        return mock.create_autospec(CreateTaskPresenterInterface)

    @pytest.fixture
    def mock_object(self):
        return mock.Mock()

    @pytest.fixture
    def user_action_on_task_mock(self, mocker):
        path = "ib_tasks.interactors.user_action_on_task." \
               "user_action_on_task_interactor" \
               ".UserActionOnTaskInteractor" \
               ".user_action_on_task_and_set_random_assignees"
        return mocker.patch(path)

    @pytest.fixture
    def create_task_log_mock(self, mocker):
        path = "ib_tasks.interactors.task_log_interactor.TaskLogInteractor" \
               ".create_task_log"
        return mocker.patch(path)

    @pytest.fixture
    def task_details_validations_mock(self, mocker):
        path = "ib_tasks.interactors.create_or_update_task" \
               ".task_details_validations_interactor" \
               ".TaskDetailsValidationsInteractor" \
               ".perform_task_details_validations"
        return mocker.patch(path)

    @pytest.fixture
    def task_crud_create_task_mock(self, mocker):
        path = "ib_tasks.interactors.create_or_update_task.task_crud_operations_interactor.TaskCrudOperationsInteractor.create_task"
        return mocker.patch(path)

    @pytest.fixture
    def task_crud_create_task_gofs_mock(self, mocker):
        path = "ib_tasks.interactors.create_or_update_task.task_crud_operations_interactor.TaskCrudOperationsInteractor.create_task_gofs"
        return mocker.patch(path)

    @pytest.fixture
    def task_crud_create_task_gof_fields_mock(self, mocker):
        path = "ib_tasks.interactors.create_or_update_task.task_crud_operations_interactor.TaskCrudOperationsInteractor.create_task_gof_fields"
        return mocker.patch(path)

    @pytest.fixture
    def user_action_on_task_success_return_value(self):
        return (
            TaskCompleteDetailsDTOFactory(),
            TaskCurrentStageDetailsDTOFactory(),
            AllTasksOverviewDetailsDTOFactory())

    def test_with_invalid_project_id(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        task_request_json = '{"key": "value"}'
        given_project_id = "project_id"
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__project_id=given_project_id)

        from ib_tasks.exceptions.custom_exceptions import InvalidProjectId
        task_details_validations_mock.side_effect = InvalidProjectId(
            given_project_id)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_project_id.return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_project_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_project_id.call_args
        error_object = call_args[0][0]
        invalid_project_id = error_object.project_id
        assert invalid_project_id == given_project_id

    def test_with_invalid_task_template_id(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_template_id = "template_id"
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__task_template_id=given_template_id)
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskTemplateDBId
        task_details_validations_mock.side_effect = InvalidTaskTemplateDBId(
            given_template_id)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        presenter_mock.raise_invalid_task_template_id.return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_task_template_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_task_template_id.call_args
        error_object = call_args[0][0]
        invalid_template_id = error_object.task_template_id
        assert invalid_template_id == given_template_id

    def test_with_invalid_task_template_of_project(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_template_id = "template_id"
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__task_template_id=given_template_id)
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskTemplateOfProject
        task_details_validations_mock.side_effect = \
            InvalidTaskTemplateOfProject(
                task_dto.basic_task_details_dto.project_id,
                given_template_id)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_task_template_of_project \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_task_template_of_project \
            .assert_called_once()
        call_args = presenter_mock.raise_invalid_task_template_of_project \
            .call_args
        error_object = call_args[0][0]
        template_id = error_object.template_id
        project_id = error_object.project_id
        assert template_id == given_template_id
        assert project_id == task_dto.basic_task_details_dto.project_id

    def test_with_invalid_action_id(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_action_id = 1
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__action_id=given_action_id)
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException
        task_details_validations_mock.side_effect = InvalidActionException(
            given_action_id)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_action_id.return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_action_id.assert_called_once()
        call_args = presenter_mock.raise_invalid_action_id.call_args
        error_object = call_args[0][0]
        invalid_action_id = error_object.action_id
        assert invalid_action_id == given_action_id

    @freezegun.freeze_time('2020-09-09 13:00:00')
    def test_with_expired_due_date(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_start_datetime = datetime.datetime(2020, 8, 20)
        given_due_datetime = datetime.datetime(2020, 9, 1)
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__start_datetime=given_start_datetime,
            basic_task_details_dto__due_datetime=given_due_datetime)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueDateTimeHasExpired
        task_details_validations_mock.side_effect = DueDateTimeHasExpired(
            given_due_datetime)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_due_date_time_has_expired \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_due_date_time_has_expired.assert_called_once()
        call_args = presenter_mock.raise_due_date_time_has_expired.call_args
        error_object = call_args[0][0]
        invalid_due_date = error_object.due_datetime
        assert invalid_due_date == given_due_datetime

    @freezegun.freeze_time('2020-09-09 13:00:00')
    def test_with_expired_due_date_when_due_date_is_today(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_start_datetime = datetime.datetime(2020, 8, 20)
        given_due_datetime = datetime.datetime(2020, 9, 9, 13, 0, 0)
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__start_datetime=given_start_datetime,
            basic_task_details_dto__due_datetime=given_due_datetime)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueDateTimeHasExpired
        task_details_validations_mock.side_effect = DueDateTimeHasExpired(
            given_due_datetime)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_due_date_time_has_expired \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_due_date_time_has_expired.assert_called_once()
        call_args = presenter_mock.raise_due_date_time_has_expired.call_args
        error_object = call_args[0][0]
        invalid_due_date = error_object.due_datetime
        assert invalid_due_date == given_due_datetime

    def test_with_start_date_ahead_of_due_date(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_start_datetime = datetime.datetime(2020, 9, 9)
        given_due_datetime = datetime.datetime(2020, 9, 1)
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__start_datetime=given_start_datetime,
            basic_task_details_dto__due_datetime=given_due_datetime)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            StartDateIsAheadOfDueDate
        task_details_validations_mock.side_effect = StartDateIsAheadOfDueDate(
            given_start_datetime, given_due_datetime)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_start_date_is_ahead_of_due_date \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_start_date_is_ahead_of_due_date \
            .assert_called_once()
        call_args = presenter_mock.raise_start_date_is_ahead_of_due_date \
            .call_args
        error_object = call_args[0][0]
        invalid_start_date = error_object.given_start_date
        invalid_due_date = error_object.given_due_date
        assert invalid_start_date == given_start_datetime
        assert invalid_due_date == given_due_datetime

    def test_with_duplicate_same_gof_order_for_a_gof(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_gof_id = "gof_0"
        given_same_gof_order = 1
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=3, gof_id=given_gof_id, same_gof_order=given_same_gof_order)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)
        task_details_validations_mock.side_effect = \
            DuplicateSameGoFOrderForAGoF(given_gof_id, [given_same_gof_order])
        storage_mock.validate_action.return_value = True

        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_duplicate_same_gof_orders_for_a_gof \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_duplicate_same_gof_orders_for_a_gof \
            .assert_called_once()
        call_args = presenter_mock.raise_duplicate_same_gof_orders_for_a_gof \
            .call_args
        error_object = call_args[0][0]
        same_orders_gof_id = error_object.gof_id
        duplicate_same_gof_orders = error_object.same_gof_orders
        assert same_orders_gof_id == given_gof_id
        assert duplicate_same_gof_orders == [given_same_gof_order]

    def test_without_priority_when_action_type_is_not_no_validations(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_action_id = 1
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__priority=None,
            basic_task_details_dto__action_id=given_action_id)
        from ib_tasks.exceptions.task_custom_exceptions import \
            PriorityIsRequired
        task_details_validations_mock.side_effect = PriorityIsRequired
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_priority_is_required \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_priority_is_required.assert_called_once()

    @freezegun.freeze_time('2020-09-09 13:00:00')
    def test_with_due_datetime_without_start_datetime(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_action_id = 1
        given_due_datetime = datetime.datetime.now()
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__start_datetime=None,
            basic_task_details_dto__due_datetime=given_due_datetime,
            basic_task_details_dto__action_id=given_action_id)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueDateTimeWithoutStartDateTimeIsNotValid
        task_details_validations_mock.side_effect = \
            DueDateTimeWithoutStartDateTimeIsNotValid(given_due_datetime)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_due_date_time_without_start_datetime \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_due_date_time_without_start_datetime \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_due_date_time_without_start_datetime.call_args
        error_object = call_args[0][0]
        due_datetime = error_object.due_datetime
        assert due_datetime == given_due_datetime

    def test_without_start_date_time_when_action_type_is_not_no_validations(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_action_id = 1
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__start_datetime=None,
            basic_task_details_dto__due_datetime=None,
            basic_task_details_dto__action_id=given_action_id)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            StartDateTimeIsRequired
        task_details_validations_mock.side_effect = StartDateTimeIsRequired
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_start_date_time_is_required \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_start_date_time_is_required.assert_called_once()

    def test_without_due_date_time_when_action_type_is_not_no_validations(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_action_id = 1
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__due_datetime=None,
            basic_task_details_dto__action_id=given_action_id)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueDateTimeIsRequired
        task_details_validations_mock.side_effect = DueDateTimeIsRequired
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_due_date_time_is_required \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_due_date_time_is_required.assert_called_once()

    def test_with_invalid_gof_ids(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_gof_ids = ["gof_0", "gof_1", "gof_2"]
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=3, gof_id=factory.Iterator(given_gof_ids)
        )
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
        task_details_validations_mock.side_effect = InvalidGoFIds(
            given_gof_ids)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_gof_ids.return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_gof_ids.assert_called_once()
        call_args = presenter_mock.raise_invalid_gof_ids.call_args
        error_object = call_args[0][0]
        invalid_gof_ids = error_object.gof_ids
        assert invalid_gof_ids == given_gof_ids

    def test_with_invalid_gofs_to_task_template(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_task_template_id = "template_0"
        given_gof_ids = ["gof_0", "gof_1", "gof_2"]
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=3, gof_id=factory.Iterator(given_gof_ids)
        )
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__task_template_id=given_task_template_id,
            gof_fields_dtos=gof_fields_dtos
        )

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidGoFsOfTaskTemplate
        task_details_validations_mock \
            .side_effect = InvalidGoFsOfTaskTemplate(given_gof_ids,
                                                     given_task_template_id)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_gofs_given_to_a_task_template \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_gofs_given_to_a_task_template \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_gofs_given_to_a_task_template \
                .call_args
        error_object = call_args[0][0]
        invalid_gof_ids = error_object.gof_ids
        invalid_gofs_template_id = error_object.task_template_id
        assert invalid_gof_ids == given_gof_ids
        assert invalid_gofs_template_id == given_task_template_id

    def test_with_invalid_field_ids(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_ids = ["field_0", "field_1", "field_2"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=3, field_id=factory.Iterator(given_field_ids))
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidFieldIds
        task_details_validations_mock \
            .side_effect = InvalidFieldIds(given_field_ids)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_field_ids.return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_field_ids.assert_called_once()
        call_args = presenter_mock.raise_invalid_field_ids.call_args
        error_object = call_args[0][0]
        invalid_field_ids = error_object.field_ids
        assert invalid_field_ids == given_field_ids

    def test_with_duplicate_field_ids_to_a_gof(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_gof_id = "gof_0"
        given_duplicate_field_ids = ["field_0", "field_0"]
        given_field_ids = given_duplicate_field_ids + ["field_2"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=3, field_id=factory.Iterator(given_field_ids))
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, gof_id=given_gof_id, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.fields_custom_exceptions import \
            DuplicateFieldIdsToGoF
        task_details_validations_mock \
            .side_effect = DuplicateFieldIdsToGoF(given_gof_id,
                                                  given_duplicate_field_ids)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_duplicate_field_ids_to_a_gof.return_value = \
            mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_duplicate_field_ids_to_a_gof.assert_called_once()
        call_args = presenter_mock.raise_duplicate_field_ids_to_a_gof.call_args
        error_object = call_args[0][0]
        invalid_gof_id = error_object.gof_id
        invalid_field_ids = error_object.field_ids
        assert invalid_gof_id == given_gof_id
        assert invalid_field_ids == given_duplicate_field_ids

    def test_with_invalid_field_ids_to_a_gof(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_gof_id = "gof_0"
        given_field_ids = ["field_0", "field_0", "field_2"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=3, field_id=factory.Iterator(given_field_ids))
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, gof_id=given_gof_id, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidFieldsOfGoF
        task_details_validations_mock \
            .side_effect = InvalidFieldsOfGoF(given_gof_id, given_field_ids)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_fields_given_to_a_gof.return_value = \
            mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_fields_given_to_a_gof.assert_called_once()
        call_args = presenter_mock.raise_invalid_fields_given_to_a_gof \
            .call_args
        error_object = call_args[0][0]
        invalid_gof_id = error_object.gof_id
        invalid_field_ids = error_object.field_ids
        assert invalid_gof_id == given_gof_id
        assert invalid_field_ids == given_field_ids

    def test_with_user_who_does_not_have_write_permission_to_a_gof(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_created_by_id = "user_0"
        given_gof_id = "gof_0"
        given_required_user_roles = ["role_1", "role_2"]
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(size=1,
                                                          gof_id=given_gof_id)
        task_dto = CreateTaskDTOFactory(
            gof_fields_dtos=gof_fields_dtos,
            basic_task_details_dto__created_by_id=given_created_by_id)

        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserNeedsGoFWritablePermission
        task_details_validations_mock \
            .side_effect = UserNeedsGoFWritablePermission(
                given_created_by_id, given_gof_id, given_required_user_roles)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_user_needs_gof_writable_permission.return_value \
            = \
            mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_needs_gof_writable_permission \
            .assert_called_once()
        call_args = presenter_mock.raise_user_needs_gof_writable_permission \
            .call_args
        error_object = call_args[0][0]
        user_id = error_object.user_id
        invalid_gof_id = error_object.gof_id
        required_roles = error_object.required_roles
        assert user_id == given_created_by_id
        assert invalid_gof_id == given_gof_id
        assert required_roles == given_required_user_roles

    def test_with_user_who_does_not_have_write_permission_to_a_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_created_by_id = "user_0"
        given_required_user_roles = ["role_1", "role_2"]
        given_field_id = "field_0"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(
            gof_fields_dtos=gof_fields_dtos,
            basic_task_details_dto__created_by_id=given_created_by_id)

        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserNeedsFieldWritablePermission
        task_details_validations_mock \
            .side_effect = UserNeedsFieldWritablePermission(
                given_created_by_id, given_field_id, given_required_user_roles)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_user_needs_field_writable_permission \
            .return_value \
            = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_needs_field_writable_permission \
            .assert_called_once()
        call_args = presenter_mock.raise_user_needs_field_writable_permission \
            .call_args
        error_object = call_args[0][0]
        user_id = error_object.user_id
        invalid_field_id = error_object.field_id
        required_roles = error_object.required_roles
        assert user_id == given_created_by_id
        assert invalid_field_id == given_field_id
        assert required_roles == given_required_user_roles

    def test_with_unfilled_fields_which_are_permitted_and_required_for_user(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_unfilled_field_dtos = FieldIdWithFieldDisplayNameDTOFactory()
        task_dto = CreateTaskDTOFactory()

        from ib_tasks.exceptions.fields_custom_exceptions import \
            UserDidNotFillRequiredFields
        task_details_validations_mock \
            .side_effect = UserDidNotFillRequiredFields(
                given_unfilled_field_dtos)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_user_did_not_fill_required_fields \
            .return_value \
            = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_did_not_fill_required_fields \
            .assert_called_once()
        call_args = presenter_mock.raise_user_did_not_fill_required_fields \
            .call_args
        error_object = call_args[0][0]
        unfilled_field_dtos = error_object.unfilled_field_dtos
        assert unfilled_field_dtos == given_unfilled_field_dtos

    def test_with_empty_response_to_a_required_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        given_field_response = ""
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            EmptyValueForRequiredField
        task_details_validations_mock \
            .side_effect = EmptyValueForRequiredField(given_field_id)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_empty_value_in_required_field.return_value = \
            mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_empty_value_in_required_field \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_empty_value_in_required_field.call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        assert invalid_field_id == given_field_id

    def test_with_invalid_response_to_a_phone_number_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        given_field_response = "890808"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidPhoneNumberValue
        task_details_validations_mock \
            .side_effect = InvalidPhoneNumberValue(given_field_id,
                                                   given_field_response)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_phone_number_value \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_phone_number_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_phone_number_value \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_email_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        given_field_response = "sljlsjls@gmail"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidEmailFieldValue
        task_details_validations_mock \
            .side_effect = InvalidEmailFieldValue(given_field_id,
                                                  given_field_response)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_email_address \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_email_address \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_email_address.call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_url_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        given_field_response = "invalid url"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidURLValue
        task_details_validations_mock \
            .side_effect = InvalidURLValue(given_field_id,
                                           given_field_response)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_url_address \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_url_address \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_url_address \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_weak_password_response_to_a_password_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        given_field_response = "weak password"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            NotAStrongPassword
        task_details_validations_mock \
            .side_effect = NotAStrongPassword(given_field_id,
                                              given_field_response)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_weak_password \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_weak_password \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_weak_password \
                .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_number_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        given_field_response = "two"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidNumberValue
        task_details_validations_mock \
            .side_effect = InvalidNumberValue(given_field_id,
                                              given_field_response)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_number_value \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_number_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_number_value.call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_float_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        given_field_response = "two point five"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFloatValue
        task_details_validations_mock \
            .side_effect = InvalidFloatValue(given_field_id,
                                             given_field_response)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_float_value \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_float_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_float_value.call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response

    def test_with_invalid_response_to_a_dropdown_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        given_field_response = '["choice 5"]'
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidValueForDropdownField
        task_details_validations_mock \
            .side_effect = InvalidValueForDropdownField(
                given_field_id, given_field_response, valid_choices
            )
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_dropdown_value \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_dropdown_value \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_dropdown_value.call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_dropdown_choices = error_object.valid_values

        assert invalid_field_id == given_field_id
        assert valid_dropdown_choices == valid_choices
        assert invalid_field_response == given_field_response

    def test_with_invalid_name_to_a_gof_selector_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        valid_choices = ["gof selector name 1", "gof selector name 2"]
        given_field_response = '["gof selector name 5"]'
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectNameInGoFSelectorField
        task_details_validations_mock \
            .side_effect = IncorrectNameInGoFSelectorField(
                given_field_id, given_field_response, valid_choices
            )
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock \
            .raise_invalid_name_in_gof_selector \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_name_in_gof_selector \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_name_in_gof_selector \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_gof_selector_choices = error_object.valid_gof_selector_names

        assert invalid_field_id == given_field_id
        assert valid_gof_selector_choices == valid_choices
        assert invalid_field_response == given_field_response

    def test_with_invalid_choice_to_a_radio_group_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        given_field_response = '["choice 5"]'
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectRadioGroupChoice
        task_details_validations_mock \
            .side_effect = IncorrectRadioGroupChoice(
                given_field_id, given_field_response, valid_choices
            )
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock \
            .raise_invalid_choice_in_radio_group_field \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_choice_in_radio_group_field \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_choice_in_radio_group_field \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_radio_group_choices = error_object.valid_radio_group_options

        assert invalid_field_id == given_field_id
        assert valid_radio_group_choices == valid_choices
        assert invalid_field_response == given_field_response

    def test_with_invalid_choice_to_a_check_box_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        invalid_checkbox_options_selected = ["choice 5"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=invalid_checkbox_options_selected)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectCheckBoxOptionsSelected
        task_details_validations_mock \
            .side_effect = IncorrectCheckBoxOptionsSelected(
                given_field_id, invalid_checkbox_options_selected,
                valid_choices)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock \
            .raise_invalid_checkbox_group_options_selected \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_checkbox_group_options_selected \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_checkbox_group_options_selected \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_check_box_response = error_object.invalid_checkbox_options
        valid_check_box_choices = error_object.valid_check_box_options

        assert invalid_field_id == given_field_id
        assert invalid_check_box_response == invalid_checkbox_options_selected
        assert valid_check_box_choices == valid_choices

    def test_with_invalid_option_to_a_multi_select_options_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        invalid_multi_select_options_selected = ["choice 5"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=invalid_multi_select_options_selected)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectOptionsSelected
        task_details_validations_mock \
            .side_effect = IncorrectMultiSelectOptionsSelected(
            given_field_id, invalid_multi_select_options_selected,
            valid_choices
        )
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock \
            .raise_invalid_multi_select_options_selected \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_multi_select_options_selected \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_multi_select_options_selected \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_multi_select_options_response = \
            error_object.invalid_multi_select_options
        valid_multi_select_options = error_object.valid_multi_select_options

        assert invalid_field_id == given_field_id
        assert invalid_multi_select_options_response == \
               invalid_multi_select_options_selected
        assert valid_multi_select_options == valid_choices

    def test_with_invalid_option_to_a_multi_select_label_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        valid_choices = ["choice 1", "choice 2", "choice 3"]
        invalid_multi_select_labels_selected = ["choice 5"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=invalid_multi_select_labels_selected)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectLabelsSelected
        task_details_validations_mock \
            .side_effect = IncorrectMultiSelectLabelsSelected(
                given_field_id, invalid_multi_select_labels_selected,
                valid_choices)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock \
            .raise_invalid_multi_select_labels_selected \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_multi_select_labels_selected \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_multi_select_labels_selected \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_multi_select_labels_response = \
            error_object.invalid_multi_select_labels
        valid_multi_select_labels = error_object.valid_multi_select_labels

        assert invalid_field_id == given_field_id
        assert invalid_multi_select_labels_response == \
               invalid_multi_select_labels_selected
        assert valid_multi_select_labels == valid_choices

    def test_with_invalid_date_format_to_a_date_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        from ib_tasks.constants.config import DATE_FORMAT
        expected_format = DATE_FORMAT
        given_field_response = "05-04-2020"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidDateFormat
        task_details_validations_mock \
            .side_effect = InvalidDateFormat(
            given_field_id, given_field_response, expected_format
        )
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock \
            .raise_invalid_date_format \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_date_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_date_format \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_format = error_object.expected_format

        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response
        assert valid_format == expected_format

    def test_with_invalid_time_format_to_a_time_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        from ib_tasks.constants.config import TIME_FORMAT
        expected_format = TIME_FORMAT
        given_field_response = "2:30 PM"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidTimeFormat
        task_details_validations_mock \
            .side_effect = InvalidTimeFormat(
                given_field_id, given_field_response, expected_format
            )
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock \
            .raise_invalid_time_format \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_time_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_time_format \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_field_response = error_object.field_value
        valid_format = error_object.expected_format

        assert invalid_field_id == given_field_id
        assert invalid_field_response == given_field_response
        assert valid_format == expected_format

    def test_with_invalid_url_to_a_image_uploader_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        given_field_response = "invalid image url"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForImage
        task_details_validations_mock \
            .side_effect = InvalidUrlForImage(given_field_id,
                                              given_field_response)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_image_url.return_value = \
            mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_image_url \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_image_url \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_image_url = error_object.image_url

        assert invalid_field_id == given_field_id
        assert given_field_response == invalid_image_url

    def test_with_invalid_image_format_to_a_image_uploader_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        given_field_response = "invalid image format url"
        given_format = ".svg"
        allowed_formats = [".png", ".jpeg"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidImageFormat
        task_details_validations_mock \
            .side_effect = InvalidImageFormat(given_field_id, given_format,
                                              allowed_formats)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock \
            .raise_not_acceptable_image_format \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_not_acceptable_image_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_not_acceptable_image_format \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        given_invalid_format = error_object.given_format
        valid_formats = error_object.allowed_formats

        assert invalid_field_id == given_field_id
        assert given_invalid_format == given_format
        assert valid_formats == allowed_formats

    def test_with_invalid_url_to_a_file_uploader_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        given_field_response = "invalid file url"
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForFile
        task_details_validations_mock \
            .side_effect = InvalidUrlForFile(given_field_id,
                                             given_field_response)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock \
            .raise_invalid_file_url \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_file_url \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_invalid_file_url \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        invalid_file_url = error_object.file_url

        assert invalid_field_id == given_field_id
        assert invalid_file_url == given_field_response

    def test_with_invalid_file_format_to_a_file_uploader_field(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_field_id = "field_0"
        given_field_response = "invalid file format url"
        given_format = ".zip"
        allowed_formats = [".pdf", ".xls"]
        field_values_dtos = FieldValuesDTOFactory.build_batch(
            size=1, field_id=given_field_id,
            field_response=given_field_response)
        gof_fields_dtos = GoFFieldsDTOFactory.build_batch(
            size=1, field_values_dtos=field_values_dtos)
        task_dto = CreateTaskDTOFactory(gof_fields_dtos=gof_fields_dtos)

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFileFormat
        task_details_validations_mock \
            .side_effect = InvalidFileFormat(given_field_id, given_format,
                                             allowed_formats)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock \
            .raise_not_acceptable_file_format \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_not_acceptable_file_format \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_not_acceptable_file_format \
            .call_args
        error_object = call_args[0][0]
        invalid_field_id = error_object.field_id
        given_invalid_format = error_object.given_format
        valid_formats = error_object.allowed_formats

        assert invalid_field_id == given_field_id
        assert given_invalid_format == given_format
        assert valid_formats == allowed_formats

    def test_with_valid_task_details_creates_task(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock,
            user_action_on_task_mock, task_crud_create_task_mock,
            task_crud_create_task_gofs_mock,
            task_crud_create_task_gof_fields_mock,
            user_action_on_task_success_return_value
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        created_task_id = 1
        task_dto = CreateTaskDTOFactory()
        from ib_tasks.interactors.storage_interfaces.task_dtos import \
            TaskGoFWithTaskIdDTO
        expected_task_gof_dtos = [
            TaskGoFWithTaskIdDTO(
                task_id=created_task_id,
                gof_id=gof_fields_dto.gof_id,
                same_gof_order=gof_fields_dto.same_gof_order
            )
            for gof_fields_dto in task_dto.gof_fields_dtos
        ]
        expected_task_gof_details_dtos = TaskGoFDetailsDTOFactory.build_batch(
            size=2)
        task_gof_ids = [0, 0, 1, 1]
        expected_task_gof_field_dtos = TaskGoFFieldDTOFactory.build_batch(
            size=4, task_gof_id=factory.Iterator(task_gof_ids))
        task_crud_create_task_mock.return_value = created_task_id
        task_crud_create_task_gofs_mock.return_value = \
            expected_task_gof_details_dtos
        user_action_on_task_mock.return_value = user_action_on_task_success_return_value
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        task_crud_create_task_mock.assert_called_once_with(
            task_dto.basic_task_details_dto)
        task_crud_create_task_gofs_mock.assert_called_once_with(
            expected_task_gof_dtos)
        task_crud_create_task_gof_fields_mock.assert_called_once_with(
            expected_task_gof_field_dtos)
        create_task_storage_mock.set_status_variables_for_template_and_task \
            .assert_called_once_with(
                task_dto.basic_task_details_dto.task_template_id,
                created_task_id)
        create_task_storage_mock.create_initial_task_stage.\
            assert_called_once_with(
                task_id=created_task_id,
                template_id=task_dto.basic_task_details_dto.task_template_id)

    def test_with_not_permitted_user_action(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock,
            user_action_on_task_mock, task_crud_create_task_mock,
            task_crud_create_task_gofs_mock,
            task_crud_create_task_gof_fields_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateTaskDTOFactory()

        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserActionPermissionDenied
        user_action_on_task_mock.side_effect = UserActionPermissionDenied(
            task_dto.basic_task_details_dto.action_id)
        presenter_mock.raise_user_action_permission_denied \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_user_action_permission_denied \
            .assert_called_once()
        call_args = presenter_mock. \
            raise_user_action_permission_denied \
            .call_args
        error_object = call_args[0][0]
        invalid_action_id = error_object.action_id
        assert invalid_action_id == task_dto.basic_task_details_dto.action_id

    def test_with_invalid_present_stage_action(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock,
            user_action_on_task_mock, task_crud_create_task_mock,
            task_crud_create_task_gofs_mock,
            task_crud_create_task_gof_fields_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        given_action_id = 1
        task_dto = CreateTaskDTOFactory(
            basic_task_details_dto__action_id=given_action_id)

        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidPresentStageAction
        user_action_on_task_mock.side_effect = InvalidPresentStageAction(
            given_action_id)
        presenter_mock.raise_invalid_present_stage_actions \
            .return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock \
            .raise_invalid_present_stage_actions \
            .assert_called_once()
        call_args = \
            presenter_mock.raise_invalid_present_stage_actions \
                .call_args
        error_object = call_args[0][0]
        invalid_action_id = error_object.action_id
        assert invalid_action_id == given_action_id

    def test_with_invalid_key_error(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock,
            user_action_on_task_mock, task_crud_create_task_mock,
            task_crud_create_task_gofs_mock,
            task_crud_create_task_gof_fields_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateTaskDTOFactory()

        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )

        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidKeyError
        user_action_on_task_mock.side_effect = InvalidKeyError()
        presenter_mock.raise_invalid_key_error \
            .return_value = \
            mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object

    def test_with_invalid_module_path(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock,
            user_action_on_task_mock, task_crud_create_task_mock,
            task_crud_create_task_gofs_mock,
            task_crud_create_task_gof_fields_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateTaskDTOFactory()

        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        given_module_path = "invalid module path"
        from ib_tasks.interactors \
            .get_next_stages_random_assignees_of_a_task_interactor import \
            InvalidModulePathFound
        user_action_on_task_mock.side_effect = InvalidModulePathFound(
            given_module_path)
        presenter_mock.raise_invalid_path_not_found.return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_path_not_found.assert_called_once()
        call_args = presenter_mock.raise_invalid_path_not_found.call_args
        error_object = call_args[0][0]
        invalid_path_name = error_object.path_name
        assert invalid_path_name == given_module_path

    def test_with_invalid_method_name(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock,
            user_action_on_task_mock, task_crud_create_task_mock,
            task_crud_create_task_gofs_mock,
            task_crud_create_task_gof_fields_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateTaskDTOFactory()

        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        given_method_name = "invalid method"

        from ib_tasks.interactors.user_action_on_task \
            .call_action_logic_function_and_get_or_update_task_status_variables_interactor \
            import InvalidMethodFound
        user_action_on_task_mock.side_effect = InvalidMethodFound(
            given_method_name)
        presenter_mock.raise_invalid_method_not_found.return_value = \
            mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_method_not_found.assert_called_once()
        call_args = presenter_mock.raise_invalid_method_not_found.call_args
        error_object = call_args[0][0]
        invalid_method_name = error_object.method_name
        assert invalid_method_name == given_method_name

    def test_with_duplicate_stage_ids(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock,
            user_action_on_task_mock, task_crud_create_task_mock,
            task_crud_create_task_gofs_mock,
            task_crud_create_task_gof_fields_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateTaskDTOFactory()

        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        given_duplicate_stage_ids = [1, 2]
        from ib_tasks.exceptions.stage_custom_exceptions import \
            DuplicateStageIds
        user_action_on_task_mock.side_effect = DuplicateStageIds(
            given_duplicate_stage_ids)
        presenter_mock.raise_duplicate_stage_ids_not_valid \
            .return_value = \
            mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_duplicate_stage_ids_not_valid \
            .assert_called_once()
        call_args = presenter_mock.raise_duplicate_stage_ids_not_valid.call_args
        error_object = call_args[0][0]
        duplicate_stage_ids = error_object.duplicate_stage_ids
        assert duplicate_stage_ids == given_duplicate_stage_ids

    def test_with_invalid_db_stage_ids(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock,
            user_action_on_task_mock, task_crud_create_task_mock,
            task_crud_create_task_gofs_mock,
            task_crud_create_task_gof_fields_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateTaskDTOFactory()

        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        given_invalid_db_stage_ids = [1, 2]

        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidDbStageIdsListException
        user_action_on_task_mock.side_effect = InvalidDbStageIdsListException(
            given_invalid_db_stage_ids)
        presenter_mock.raise_invalid_stage_ids.return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_stage_ids.assert_called_once()
        call_args = presenter_mock.raise_invalid_stage_ids.call_args
        error_object = call_args[0][0]
        invalid_db_stage_ids = error_object.invalid_stage_ids
        assert invalid_db_stage_ids == given_invalid_db_stage_ids

    def test_with_invalid_assignee_permission_for_given_stage_ids(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock,
            user_action_on_task_mock, task_crud_create_task_mock,
            task_crud_create_task_gofs_mock,
            task_crud_create_task_gof_fields_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateTaskDTOFactory()

        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        given_stage_ids = [1, 2]

        from ib_tasks.exceptions.stage_custom_exceptions import \
            StageIdsWithInvalidPermissionForAssignee
        user_action_on_task_mock.side_effect = \
            StageIdsWithInvalidPermissionForAssignee(given_stage_ids)
        presenter_mock.raise_invalid_stage_assignees.return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_stage_assignees.assert_called_once()
        call_args = presenter_mock.raise_invalid_stage_assignees.call_args
        error_object = call_args[0][0]
        given_invalid_stage_ids = error_object.invalid_stage_ids
        assert given_invalid_stage_ids == given_stage_ids

    def test_with_invalid_stage_ids_list(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock,
            user_action_on_task_mock, task_crud_create_task_mock,
            task_crud_create_task_gofs_mock,
            task_crud_create_task_gof_fields_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        created_task_id = 1
        task_dto = CreateTaskDTOFactory()
        expected_task_gof_details_dtos = TaskGoFDetailsDTOFactory.build_batch(
            size=2)

        create_task_storage_mock.create_task \
            .return_value = created_task_id
        create_task_storage_mock.create_task_gofs.return_value = \
            expected_task_gof_details_dtos

        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidStageIdsListException
        stage_ids = ["stage_1", "stage_2"]
        user_action_on_task_mock.side_effect = InvalidStageIdsListException(
            stage_ids)
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_invalid_stage_ids_list.return_value = \
            mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_stage_ids_list.assert_called_once()
        call_args = presenter_mock.raise_invalid_stage_ids_list.call_args
        error_object = call_args[0][0]
        invalid_stage_ids = error_object.invalid_stage_ids
        assert invalid_stage_ids == stage_ids

    def test_with_invalid_task_json(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock,
            user_action_on_task_mock, task_crud_create_task_mock,
            task_crud_create_task_gofs_mock,
            task_crud_create_task_gof_fields_mock, create_task_log_mock,
            user_action_on_task_success_return_value
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateTaskDTOFactory()
        user_action_on_task_mock.return_value = \
            user_action_on_task_success_return_value
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskJson
        given_message = "invalid task json"
        create_task_log_mock.side_effect = InvalidTaskJson(given_message)
        presenter_mock.raise_invalid_task_json.return_value = mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_task_json.assert_called_once()
        call_args = presenter_mock.raise_invalid_task_json.call_args
        error_object = call_args[0][0]
        message = error_object.message
        assert message == given_message

    def test_with_invalid_stage_permitted_gofs_raises_exception(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock,
            user_action_on_task_mock, task_crud_create_task_mock,
            task_crud_create_task_gofs_mock,
            task_crud_create_task_gof_fields_mock, create_task_log_mock,
            user_action_on_task_success_return_value
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateTaskDTOFactory()
        user_action_on_task_mock.return_value = \
            user_action_on_task_success_return_value
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        from ib_tasks.exceptions.gofs_custom_exceptions import \
            InvalidStagePermittedGoFs

        given_gof_ids = ["gof_1", "gof_2"]
        given_stage_id = 1

        create_task_log_mock.side_effect = InvalidStagePermittedGoFs(
            given_gof_ids, given_stage_id
        )
        presenter_mock.raise_invalid_stage_permitted_gofs.return_value = \
            mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_stage_permitted_gofs.assert_called_once()
        call_args = presenter_mock.raise_invalid_stage_permitted_gofs \
            .call_args
        error_object = call_args[0][0]

        gof_ids = error_object.gof_ids
        stage_id = error_object.stage_id
        assert gof_ids == given_gof_ids
        assert stage_id == given_stage_id

    def test_with_empty_stage_ids_list_raises_exception(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock, storage_mock,
            field_storage_mock, stage_storage_mock, action_storage_mock,
            elastic_storage_mock, presenter_mock, mock_object,
            task_stage_storage_mock, task_details_validations_mock,
            user_action_on_task_mock, task_crud_create_task_mock,
            task_crud_create_task_gofs_mock,
            task_crud_create_task_gof_fields_mock
    ):
        # Arrange
        task_request_json = '{"key": "value"}'
        created_task_id = 1
        task_dto = CreateTaskDTOFactory()
        expected_task_gof_details_dtos = TaskGoFDetailsDTOFactory.build_batch(
            size=2)

        create_task_storage_mock.create_task \
            .return_value = created_task_id
        create_task_storage_mock.create_task_gofs.return_value = \
            expected_task_gof_details_dtos

        from ib_tasks.exceptions.stage_custom_exceptions import \
            StageIdsListEmptyException
        user_action_on_task_mock.side_effect = StageIdsListEmptyException()
        interactor = CreateTaskInteractor(
            task_storage=task_storage_mock, gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock, storage=storage_mock,
            field_storage=field_storage_mock, stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock
        )
        presenter_mock.raise_stage_ids_list_empty.return_value = \
            mock_object

        # Act
        response = interactor.create_task_wrapper(
            presenter_mock, task_dto, task_request_json=task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_stage_ids_list_empty.assert_called_once()
