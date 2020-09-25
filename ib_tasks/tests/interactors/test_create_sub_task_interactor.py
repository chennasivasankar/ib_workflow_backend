from unittest import mock

import pytest

from ib_tasks.exceptions.custom_exceptions import InvalidProjectId
from ib_tasks.exceptions.gofs_custom_exceptions import \
    DuplicateSameGoFOrderForAGoF
from ib_tasks.tests.factories.interactor_dtos import CreateSubTaskDTOFactory, \
    BasicTaskDetailsDTOFactory, GoFFieldsDTOFactory, FieldValuesDTOFactory


class TestCreateSubTaskInteractor:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        CreateSubTaskDTOFactory.reset_sequence()
        BasicTaskDetailsDTOFactory.reset_sequence()
        GoFFieldsDTOFactory.reset_sequence()
        FieldValuesDTOFactory.reset_sequence()

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
        from ib_tasks.interactors.presenter_interfaces \
            .create_sub_task_presenter import CreateSubTaskPresenterInterface
        return mock.create_autospec(CreateSubTaskPresenterInterface)

    @pytest.fixture
    def mock_object(self):
        return mock.Mock()

    @pytest.fixture
    def create_task_mock(self, mocker):
        path = "ib_tasks.interactors.create_or_update_task" \
               ".create_task_interactor.CreateTaskInteractor.create_task"
        return mocker.patch(path)

    @pytest.fixture
    def create_task_log_mock(self, mocker):
        path = "ib_tasks.interactors.task_log_interactor.TaskLogInteractor" \
               ".create_task_log"
        return mocker.patch(path)

    @pytest.fixture
    def interactor(
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            action_storage_mock, elastic_storage_mock, task_stage_storage_mock
    ):
        from ib_tasks.interactors.create_sub_task_interactor import \
            CreateSubTaskInteractor
        interactor = CreateSubTaskInteractor(
            task_storage=task_storage_mock,
            gof_storage=gof_storage_mock,
            task_template_storage=task_template_storage_mock,
            create_task_storage=create_task_storage_mock,
            storage=storage_mock,
            field_storage=field_storage_mock,
            stage_storage=stage_storage_mock,
            action_storage=action_storage_mock,
            elastic_storage=elastic_storage_mock,
            task_stage_storage=task_stage_storage_mock)
        return interactor

    def test_with_invalid_parent_task_id(
            self, interactor, presenter_mock, mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        parent_task_id = task_dto.parent_task_id
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskDisplayId
        interactor.task_storage.validate_task_display_id_and_return_task_id \
            .side_effect = InvalidTaskDisplayId(parent_task_id)
        presenter_mock.raise_invalid_parent_task_id.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        call_args = presenter_mock.raise_invalid_parent_task_id.call_args
        error_object = call_args[0][0]
        invalid_parent_task_id = error_object.task_display_id

        assert invalid_parent_task_id == parent_task_id

    def test_with_invalid_project_id(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        project_id = task_dto.basic_task_details_dto.project_id
        create_task_mock.side_effect = InvalidProjectId(project_id)
        presenter_mock.raise_invalid_project_id.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        call_args = presenter_mock.raise_invalid_project_id.call_args
        error_object = call_args[0][0]
        invalid_project_id = error_object.project_id

        assert invalid_project_id == project_id

    def test_with_invalid_invalid_task_template_db_id(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        template_id = task_dto.basic_task_details_dto.task_template_id
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskTemplateDBId
        create_task_mock.side_effect = InvalidTaskTemplateDBId(template_id)
        presenter_mock.raise_invalid_task_template_id.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        call_args = presenter_mock.raise_invalid_task_template_id.call_args
        error_object = call_args[0][0]
        invalid_template_id = error_object.task_template_id

        assert invalid_template_id == template_id

    def test_with_invalid_task_template_of_project(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_template_id = task_dto.basic_task_details_dto.task_template_id
        given_project_id = task_dto.basic_task_details_dto.project_id
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskTemplateOfProject
        create_task_mock.side_effect = InvalidTaskTemplateOfProject(
            given_project_id, given_template_id)
        presenter_mock.raise_invalid_task_template_of_project.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        call_args = presenter_mock.raise_invalid_task_template_of_project.call_args
        error_object = call_args[0][0]
        project_id = error_object.project_id
        template_id = error_object.template_id

        assert project_id == given_project_id
        assert template_id == given_template_id

    def test_with_invalid_action(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_action_id = task_dto.basic_task_details_dto.action_id
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException
        create_task_mock.side_effect = InvalidActionException(given_action_id)
        presenter_mock.raise_invalid_action_id.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        call_args = presenter_mock.raise_invalid_action_id.call_args
        error_object = call_args[0][0]
        invalid_action_id = error_object.action_id

        assert invalid_action_id == given_action_id

    def test_with_duplicate_same_gof_order_for_a_gof(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_gof_id = "FIN_REQUESTER_DETAILS"
        given_duplicate_same_gof_orders = [1]
        create_task_mock.side_effect = DuplicateSameGoFOrderForAGoF(
            given_gof_id, given_duplicate_same_gof_orders)
        presenter_mock.raise_duplicate_same_gof_orders_for_a_gof.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        call_args = presenter_mock.raise_duplicate_same_gof_orders_for_a_gof.call_args
        error_object = call_args[0][0]
        gof_id = error_object.gof_id
        same_gof_orders = error_object.same_gof_orders

        assert gof_id == given_gof_id
        assert same_gof_orders == given_duplicate_same_gof_orders

    def test_with_priority_none_when_action_type_is_not_no_validations(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        from ib_tasks.exceptions.task_custom_exceptions import \
            PriorityIsRequired
        create_task_mock.side_effect = PriorityIsRequired()
        presenter_mock.raise_priority_is_required.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        call_args = presenter_mock.raise_priority_is_required.call_args

    def test_with_due_datetime_with_out_start_datetime(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_due_date = task_dto.basic_task_details_dto.due_datetime
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueDateTimeWithoutStartDateTimeIsNotValid
        create_task_mock.side_effect = DueDateTimeWithoutStartDateTimeIsNotValid(
            given_due_date)
        presenter_mock.raise_due_date_time_without_start_datetime.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        call_args = presenter_mock.raise_due_date_time_without_start_datetime.call_args

        error_object = call_args[0][0]
        due_datetime = error_object.due_datetime

        assert due_datetime == given_due_date
