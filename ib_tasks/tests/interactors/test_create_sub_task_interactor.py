from unittest import mock

import pytest

from ib_tasks.exceptions.custom_exceptions import InvalidProjectId
from ib_tasks.exceptions.field_values_custom_exceptions import \
    InvalidDateFormat, InvalidTimeFormat, InvalidUrlForImage, \
    InvalidImageFormat, InvalidUrlForFile, InvalidFileFormat
from ib_tasks.exceptions.fields_custom_exceptions import \
    UserDidNotFillRequiredFields
from ib_tasks.exceptions.gofs_custom_exceptions import \
    DuplicateSameGoFOrderForAGoF, InvalidGoFIds, InvalidStagePermittedGoFs
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskJson
from ib_tasks.interactors.create_sub_task_interactor import \
    CreateSubTaskInteractor
from ib_tasks.tests.factories.interactor_dtos import CreateSubTaskDTOFactory, \
    BasicTaskDetailsDTOFactory, GoFFieldsDTOFactory, FieldValuesDTOFactory
from ib_tasks.tests.factories.storage_dtos import \
    FieldWithGoFDisplayNameDTOFactory


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
            self, task_storage_mock, gof_storage_mock,
            task_template_storage_mock, create_task_storage_mock,
            storage_mock, field_storage_mock, stage_storage_mock,
            action_storage_mock, elastic_storage_mock, task_stage_storage_mock,
            presenter_mock, mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        parent_task_id = task_dto.parent_task_id
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskDisplayId
        task_storage_mock.validate_task_display_id_and_return_task_id \
            .side_effect = InvalidTaskDisplayId(parent_task_id)
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
        presenter_mock.raise_invalid_parent_task_id.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_parent_task_id.assert_called_once()

        task_storage_mock.validate_task_display_id_and_return_task_id \
            .assert_called_once_with(parent_task_id)
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
        presenter_mock.raise_invalid_project_id.assert_called_once()

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
        presenter_mock.raise_invalid_task_template_id.assert_called_once()

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
        presenter_mock.raise_invalid_task_template_of_project.assert_called_once()

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
        presenter_mock.raise_invalid_action_id.assert_called_once()

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
        presenter_mock.raise_duplicate_same_gof_orders_for_a_gof.assert_called_once()

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
        presenter_mock.raise_priority_is_required.assert_called_once()

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
        presenter_mock.raise_due_date_time_without_start_datetime.assert_called_once()
        call_args = presenter_mock.raise_due_date_time_without_start_datetime.call_args

        error_object = call_args[0][0]
        due_datetime = error_object.due_datetime

        assert due_datetime == given_due_date

    def test_with_start_datetime_as_none_when_action_type_is_not_no_validations(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            StartDateTimeIsRequired
        create_task_mock.side_effect = StartDateTimeIsRequired()
        presenter_mock.raise_start_date_time_is_required.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_start_date_time_is_required.assert_called_once()

    def test_with_due_datetime_as_none_when_action_type_is_not_no_validations(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueDateTimeIsRequired
        create_task_mock.side_effect = DueDateTimeIsRequired()
        presenter_mock.raise_due_date_time_is_required.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_due_date_time_is_required.assert_called_once()

    def test_with_start_date_ahead_of_due_date(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_start_date = task_dto.basic_task_details_dto.start_datetime
        given_due_date = task_dto.basic_task_details_dto.due_datetime
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            StartDateIsAheadOfDueDate
        create_task_mock.side_effect = StartDateIsAheadOfDueDate(
            given_start_date, given_due_date)
        presenter_mock.raise_start_date_is_ahead_of_due_date.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_start_date_is_ahead_of_due_date.assert_called_once()

        call_args = presenter_mock.raise_start_date_is_ahead_of_due_date \
            .call_args
        error_object = call_args[0][0]
        start_date = error_object.given_start_date
        due_date = error_object.given_due_date

        assert start_date == given_start_date
        assert due_date == given_due_date

    def test_with_expired_due_date(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_due_date = task_dto.basic_task_details_dto.due_datetime
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueDateTimeHasExpired
        create_task_mock.side_effect = DueDateTimeHasExpired(given_due_date)
        presenter_mock.raise_due_date_time_has_expired.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_due_date_time_has_expired.assert_called_once()

        call_args = presenter_mock.raise_due_date_time_has_expired \
            .call_args
        error_object = call_args[0][0]
        due_date = error_object.due_datetime

        assert due_date == given_due_date

    def test_with_invalid_gof_ids(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_invalid_gof_ids = ["PAYMENT_REQUESTER_DETAILS"]
        create_task_mock.side_effect = InvalidGoFIds(given_invalid_gof_ids)
        presenter_mock.raise_invalid_gof_ids.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_gof_ids.assert_called_once()

        call_args = presenter_mock.raise_invalid_gof_ids.call_args
        error_object = call_args[0][0]
        gof_ids = error_object.gof_ids

        assert gof_ids == given_invalid_gof_ids

    def test_with_invalid_gofs_given_to_a_task_template(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_task_template_id = \
            task_dto.basic_task_details_dto.task_template_id
        given_invalid_gof_display_names = ["payment requester details"]
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidGoFsOfTaskTemplate
        create_task_mock.side_effect = InvalidGoFsOfTaskTemplate(
            given_invalid_gof_display_names, given_task_template_id)
        presenter_mock.raise_invalid_gofs_given_to_a_task_template.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_gofs_given_to_a_task_template.assert_called_once()

        call_args = presenter_mock.raise_invalid_gofs_given_to_a_task_template.call_args
        error_object = call_args[0][0]
        gof_display_names = error_object.gofs_display_names
        template_id = error_object.task_template_id

        assert gof_display_names == given_invalid_gof_display_names
        assert template_id == given_task_template_id

    def test_with_invalid_field_ids(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_ids = ["PAYMENT_REQUESTER_NAME"]
        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidFieldIds
        create_task_mock.side_effect = InvalidFieldIds(given_field_ids)
        presenter_mock.raise_invalid_field_ids.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_field_ids.assert_called_once()

        call_args = presenter_mock.raise_invalid_field_ids.call_args
        error_object = call_args[0][0]
        invalid_field_ids = error_object.field_ids

        assert invalid_field_ids == given_field_ids

    def test_with_duplicate_field_ids_to_a_gof(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_duplicate_field_ids = ["PAYMENT_REQUESTER_NAME"]
        given_gof_id = "PAYMENT_REQUESTER_DETAILS"
        from ib_tasks.exceptions.fields_custom_exceptions import \
            DuplicateFieldIdsToGoF
        create_task_mock.side_effect = DuplicateFieldIdsToGoF(
            given_gof_id, given_duplicate_field_ids)
        presenter_mock.raise_duplicate_field_ids_to_a_gof.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_duplicate_field_ids_to_a_gof.assert_called_once()

        call_args = presenter_mock.raise_duplicate_field_ids_to_a_gof.call_args
        error_object = call_args[0][0]
        gof_id = error_object.gof_id
        duplicate_field_ids = error_object.field_ids

        assert gof_id == given_gof_id
        assert duplicate_field_ids == given_duplicate_field_ids

    def test_with_invalid_fields_given_to_a_gof(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_names = ["payment requester name"]
        given_gof_display_name = "payment requester details"
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidFieldsOfGoF
        create_task_mock.side_effect = InvalidFieldsOfGoF(
            given_gof_display_name, given_field_display_names)
        presenter_mock.raise_invalid_fields_given_to_a_gof.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_fields_given_to_a_gof.assert_called_once()

        call_args = presenter_mock.raise_invalid_fields_given_to_a_gof.call_args
        error_object = call_args[0][0]
        gof_display_name = error_object.gof_display_name
        field_display_names = error_object.field_display_names

        assert gof_display_name == given_gof_display_name
        assert field_display_names == given_field_display_names

    def test_with_invalid_stage_permitted_gofs(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_stage_id = 1
        given_gof_display_names = ["payment requester details"]
        create_task_mock.side_effect = InvalidStagePermittedGoFs(
            given_gof_display_names, given_stage_id)
        presenter_mock.raise_invalid_stage_permitted_gofs.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_stage_permitted_gofs.assert_called_once()

        call_args = presenter_mock.raise_invalid_stage_permitted_gofs.call_args
        error_object = call_args[0][0]
        gof_display_names = error_object.gof_display_names
        stage_id = error_object.stage_id

        assert gof_display_names == given_gof_display_names
        assert stage_id == given_stage_id

    def test_with_user_who_does_not_have_field_writable_permission(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_user_id = "1223-s232-k980-1234"
        given_field_display_name = "payment request name"
        given_required_roles = ["PAYMENT_REQUESTER"]
        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserNeedsFieldWritablePermission
        create_task_mock.side_effect = UserNeedsFieldWritablePermission(
            given_user_id, given_field_display_name, given_required_roles)
        presenter_mock.raise_user_needs_field_writable_permission.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_needs_field_writable_permission.assert_called_once()

        call_args = presenter_mock.raise_user_needs_field_writable_permission.call_args
        error_object = call_args[0][0]
        user_id = error_object.user_id
        field_display_name = error_object.field_display_name
        required_roles = error_object.required_roles

        assert user_id == given_user_id
        assert field_display_name == given_field_display_name
        assert required_roles == given_required_roles

    def test_with_required_and_permitted_fields_unfilled(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        FieldWithGoFDisplayNameDTOFactory.reset_sequence()
        given_unfilled_field_dtos = \
            FieldWithGoFDisplayNameDTOFactory.build_batch(size=2)
        create_task_mock.side_effect = UserDidNotFillRequiredFields(
            given_unfilled_field_dtos)
        presenter_mock.raise_user_did_not_fill_required_fields.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_did_not_fill_required_fields.assert_called_once()

        call_args = presenter_mock.raise_user_did_not_fill_required_fields.call_args
        error_object = call_args[0][0]
        unfilled_field_dtos = error_object.unfilled_field_dtos

        assert unfilled_field_dtos == given_unfilled_field_dtos

    def test_with_empty_value_in_required_field(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester name"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            EmptyValueForRequiredField
        create_task_mock.side_effect = EmptyValueForRequiredField(
            given_field_display_name)
        presenter_mock.raise_empty_value_in_required_field.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_empty_value_in_required_field.assert_called_once()

        call_args = presenter_mock.raise_empty_value_in_required_field.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name

        assert field_display_name == given_field_display_name

    def test_with_invalid_phone_number_value(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester name"
        given_field_value = "field response"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidPhoneNumberValue
        create_task_mock.side_effect = InvalidPhoneNumberValue(
            given_field_display_name, given_field_value)
        presenter_mock.raise_invalid_phone_number_value.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_phone_number_value.assert_called_once()

        call_args = presenter_mock.raise_invalid_phone_number_value.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        field_value = error_object.field_value

        assert field_display_name == given_field_display_name
        assert field_value == given_field_value

    def test_with_invalid_email_address(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester email"
        given_field_value = "field response"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidEmailFieldValue
        create_task_mock.side_effect = InvalidEmailFieldValue(
            given_field_display_name, given_field_value)
        presenter_mock.raise_invalid_email_address.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_email_address.assert_called_once()

        call_args = presenter_mock.raise_invalid_email_address.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        field_value = error_object.field_value

        assert field_display_name == given_field_display_name
        assert field_value == given_field_value

    def test_with_invalid_url_address(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester url"
        given_field_value = "field response"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidURLValue
        create_task_mock.side_effect = InvalidURLValue(
            given_field_display_name, given_field_value)
        presenter_mock.raise_invalid_url_address.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_url_address.assert_called_once()

        call_args = presenter_mock.raise_invalid_url_address.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        field_value = error_object.field_value

        assert field_display_name == given_field_display_name
        assert field_value == given_field_value

    def test_with_weak_password(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester password"
        given_field_value = "field response"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            NotAStrongPassword
        create_task_mock.side_effect = NotAStrongPassword(
            given_field_display_name, given_field_value)
        presenter_mock.raise_weak_password.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_weak_password.assert_called_once()

        call_args = presenter_mock.raise_weak_password.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        field_value = error_object.field_value

        assert field_display_name == given_field_display_name
        assert field_value == given_field_value

    def test_with_invalid_number_value(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester number"
        given_field_value = "field response"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidNumberValue
        create_task_mock.side_effect = InvalidNumberValue(
            given_field_display_name, given_field_value)
        presenter_mock.raise_invalid_number_value.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_number_value.assert_called_once()

        call_args = presenter_mock.raise_invalid_number_value.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        field_value = error_object.field_value

        assert field_display_name == given_field_display_name
        assert field_value == given_field_value

    def test_with_invalid_float_value(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester float"
        given_field_value = "field response"
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFloatValue
        create_task_mock.side_effect = InvalidFloatValue(
            given_field_display_name, given_field_value)
        presenter_mock.raise_invalid_float_value.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_float_value.assert_called_once()

        call_args = presenter_mock.raise_invalid_float_value.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        field_value = error_object.field_value

        assert field_display_name == given_field_display_name
        assert field_value == given_field_value

    def test_with_invalid_dropdown_value(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester dropdown"
        given_field_value = "field response"
        given_valid_values = ["online", "offline"]
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidValueForDropdownField
        create_task_mock.side_effect = InvalidValueForDropdownField(
            given_field_display_name, given_field_value, given_valid_values)
        presenter_mock.raise_invalid_dropdown_value.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_dropdown_value.assert_called_once()

        call_args = presenter_mock.raise_invalid_dropdown_value.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        field_value = error_object.field_value
        valid_values = error_object.valid_values

        assert field_display_name == given_field_display_name
        assert field_value == given_field_value
        assert valid_values == given_valid_values

    def test_with_invalid_name_in_gof_selector(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester gof selector"
        given_field_value = "field response"
        given_valid_gof_selector_names = ["online", "offline"]
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectNameInGoFSelectorField
        create_task_mock.side_effect = IncorrectNameInGoFSelectorField(
            given_field_display_name, given_field_value,
            given_valid_gof_selector_names)
        presenter_mock.raise_invalid_name_in_gof_selector.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_name_in_gof_selector.assert_called_once()

        call_args = presenter_mock.raise_invalid_name_in_gof_selector.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        field_value = error_object.field_value
        valid_gof_selector_names = error_object.valid_gof_selector_names

        assert field_display_name == given_field_display_name
        assert field_value == given_field_value
        assert valid_gof_selector_names == given_valid_gof_selector_names

    def test_with_invalid_choice_in_radio_group_field(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester radio group"
        given_field_value = "field response"
        given_valid_radio_group_options = ["online", "offline"]
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectRadioGroupChoice
        create_task_mock.side_effect = IncorrectRadioGroupChoice(
            given_field_display_name, given_field_value,
            given_valid_radio_group_options)
        presenter_mock.raise_invalid_choice_in_radio_group_field.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_choice_in_radio_group_field.assert_called_once()

        call_args = presenter_mock.raise_invalid_choice_in_radio_group_field.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        field_value = error_object.field_value
        valid_radio_group_options = error_object.valid_radio_group_options

        assert field_display_name == given_field_display_name
        assert field_value == given_field_value
        assert valid_radio_group_options == given_valid_radio_group_options

    def test_with_invalid_checkbox_group_options_selected(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester checkbox options"
        given_invalid_checkbox_options = ["field response"]
        given_valid_check_box_options = ["online", "offline"]
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectCheckBoxOptionsSelected
        create_task_mock.side_effect = IncorrectCheckBoxOptionsSelected(
            given_field_display_name, given_invalid_checkbox_options,
            given_valid_check_box_options)
        presenter_mock.raise_invalid_checkbox_group_options_selected.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_checkbox_group_options_selected.assert_called_once()

        call_args = presenter_mock.raise_invalid_checkbox_group_options_selected.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        invalid_checkbox_options = error_object.invalid_checkbox_options
        valid_check_box_options = error_object.valid_check_box_options

        assert field_display_name == given_field_display_name
        assert invalid_checkbox_options == given_invalid_checkbox_options
        assert valid_check_box_options == given_valid_check_box_options

    def test_with_invalid_multi_select_options_selected(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester multiselect options"
        given_invalid_multiselect_options = ["field response"]
        given_valid_multi_select_options = ["online", "offline"]
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectOptionsSelected
        create_task_mock.side_effect = IncorrectMultiSelectOptionsSelected(
            given_field_display_name, given_invalid_multiselect_options,
            given_valid_multi_select_options)
        presenter_mock.raise_invalid_multi_select_options_selected.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_multi_select_options_selected.assert_called_once()

        call_args = presenter_mock.raise_invalid_multi_select_options_selected.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        invalid_multi_select_options = error_object.invalid_multi_select_options
        valid_multi_select_options = error_object.valid_multi_select_options

        assert field_display_name == given_field_display_name
        assert invalid_multi_select_options == given_invalid_multiselect_options
        assert valid_multi_select_options == given_valid_multi_select_options

    def test_with_invalid_multi_select_labels_selected(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester multiselect labels"
        given_invalid_multiselect_labels = ["field response"]
        given_valid_multiselect_labels = ["online", "offline"]
        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectLabelsSelected
        create_task_mock.side_effect = IncorrectMultiSelectLabelsSelected(
            given_field_display_name, given_invalid_multiselect_labels,
            given_valid_multiselect_labels)
        presenter_mock.raise_invalid_multi_select_labels_selected.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_multi_select_labels_selected.assert_called_once()

        call_args = presenter_mock.raise_invalid_multi_select_labels_selected.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        invalid_multi_select_labels = error_object.invalid_multi_select_labels
        valid_multi_select_labels = error_object.valid_multi_select_labels

        assert field_display_name == given_field_display_name
        assert invalid_multi_select_labels == given_invalid_multiselect_labels
        assert valid_multi_select_labels == given_valid_multiselect_labels

    def test_with_invalid_date_format(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester date"
        given_field_value = "2020 8 9"
        given_expected_format = "yyyy-mm-dd"
        create_task_mock.side_effect = InvalidDateFormat(
            given_field_display_name, given_field_value, given_expected_format)
        presenter_mock.raise_invalid_date_format.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_date_format.assert_called_once()

        call_args = presenter_mock.raise_invalid_date_format.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        field_value = error_object.field_value
        expected_format = error_object.expected_format

        assert field_display_name == given_field_display_name
        assert field_value == given_field_value
        assert expected_format == given_expected_format

    def test_with_invalid_time_format(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester time"
        given_field_value = "8 9"
        given_expected_format = "HH:MM:SS"
        create_task_mock.side_effect = InvalidTimeFormat(
            given_field_display_name, given_field_value, given_expected_format)
        presenter_mock.raise_invalid_time_format.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_time_format.assert_called_once()

        call_args = presenter_mock.raise_invalid_time_format.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        field_value = error_object.field_value
        expected_format = error_object.expected_format

        assert field_display_name == given_field_display_name
        assert field_value == given_field_value
        assert expected_format == given_expected_format

    def test_with_invalid_image_url(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester image url"
        given_image_url = "image url"
        create_task_mock.side_effect = InvalidUrlForImage(
            given_field_display_name, given_image_url)
        presenter_mock.raise_invalid_image_url.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_image_url.assert_called_once()

        call_args = presenter_mock.raise_invalid_image_url.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        image_url = error_object.image_url

        assert field_display_name == given_field_display_name
        assert image_url == given_image_url

    def test_with_not_acceptable_image_format(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester image format"
        given_image_format = ".format"
        given_allowed_formats = [".png", ".jpg"]
        create_task_mock.side_effect = InvalidImageFormat(
            given_field_display_name, given_image_format,
            given_allowed_formats)
        presenter_mock.raise_not_acceptable_image_format.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_not_acceptable_image_format.assert_called_once()

        call_args = presenter_mock.raise_not_acceptable_image_format.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        given_format = error_object.given_format
        allowed_formats = error_object.allowed_formats

        assert field_display_name == given_field_display_name
        assert given_format == given_image_format
        assert allowed_formats == given_allowed_formats

    def test_with_invalid_file_url(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester file url"
        given_file_url = "file url"
        create_task_mock.side_effect = InvalidUrlForFile(
            given_field_display_name, given_file_url)
        presenter_mock.raise_invalid_file_url.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_file_url.assert_called_once()

        call_args = presenter_mock.raise_invalid_file_url.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        file_url = error_object.file_url

        assert field_display_name == given_field_display_name
        assert file_url == given_file_url

    def test_with_not_acceptable_file_format(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_field_display_name = "payment requester file format"
        given_response = ".file_format"
        given_allowed_formats = [".zip", ".tar"]
        create_task_mock.side_effect = InvalidFileFormat(
            given_field_display_name, given_response, given_allowed_formats)
        presenter_mock.raise_not_acceptable_file_format.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_not_acceptable_file_format.assert_called_once()

        call_args = presenter_mock.raise_not_acceptable_file_format.call_args
        error_object = call_args[0][0]
        field_display_name = error_object.field_display_name
        given_response = error_object.given_format
        allowed_formats = error_object.allowed_formats

        assert field_display_name == given_field_display_name
        assert given_response == given_response
        assert allowed_formats == given_allowed_formats

    def test_with_user_action_permission_denied(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_action_id = 1
        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserActionPermissionDenied
        create_task_mock.side_effect = UserActionPermissionDenied(
            given_action_id)
        presenter_mock.raise_user_action_permission_denied.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_user_action_permission_denied.assert_called_once()

        call_args = presenter_mock.raise_user_action_permission_denied.call_args
        error_object = call_args[0][0]
        action_id = error_object.action_id

        assert action_id == given_action_id

    def test_with_invalid_present_stage_actions(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_action_id = 1
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidPresentStageAction
        create_task_mock.side_effect = InvalidPresentStageAction(
            given_action_id)
        presenter_mock.raise_invalid_present_stage_actions.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_present_stage_actions.assert_called_once()

        call_args = presenter_mock.raise_invalid_present_stage_actions.call_args
        error_object = call_args[0][0]
        action_id = error_object.action_id

        assert action_id == given_action_id

    def test_with_invalid_key_error(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_action_id = 1
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidKeyError
        create_task_mock.side_effect = InvalidKeyError()
        presenter_mock.raise_invalid_key_error.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_key_error.assert_called_once()

    def test_with_invalid_method_not_found(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_method_name = "method name"
        from ib_tasks.interactors.user_action_on_task.call_action_logic_function_and_get_or_update_task_status_variables_interactor import \
            InvalidMethodFound
        create_task_mock.side_effect = InvalidMethodFound(given_method_name)
        presenter_mock.raise_invalid_method_not_found.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_method_not_found.assert_called_once()
        call_args = presenter_mock.raise_invalid_method_not_found.call_args

        error_object = call_args[0][0]
        method_name = error_object.method_name

        assert method_name == given_method_name

    def test_with_duplicate_stage_ids_not_valid(
            self, interactor, presenter_mock, create_task_mock,
            mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_duplicate_stage_ids = [1, 2]
        from ib_tasks.exceptions.stage_custom_exceptions import \
            DuplicateStageIds
        create_task_mock.side_effect = DuplicateStageIds(
            given_duplicate_stage_ids)
        presenter_mock.raise_duplicate_stage_ids_not_valid.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_duplicate_stage_ids_not_valid.assert_called_once()
        call_args = presenter_mock.raise_duplicate_stage_ids_not_valid.call_args

        error_object = call_args[0][0]
        duplicate_stage_ids = error_object.duplicate_stage_ids

        assert duplicate_stage_ids == given_duplicate_stage_ids

    def test_with_invalid_stage_ids(
            self, interactor, presenter_mock, create_task_mock, mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_invalid_stage_ids = [1, 2]
        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidDbStageIdsListException
        create_task_mock.side_effect = InvalidDbStageIdsListException(
            given_invalid_stage_ids)
        presenter_mock.raise_invalid_stage_ids.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_stage_ids.assert_called_once()
        call_args = presenter_mock.raise_invalid_stage_ids.call_args

        error_object = call_args[0][0]
        invalid_stage_ids = error_object.invalid_stage_ids

        assert invalid_stage_ids == given_invalid_stage_ids

    def test_with_stage_ids_list_empty(
            self, interactor, presenter_mock, create_task_mock, mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        from ib_tasks.exceptions.stage_custom_exceptions import \
            StageIdsListEmptyException
        create_task_mock.side_effect = StageIdsListEmptyException()
        presenter_mock.raise_stage_ids_list_empty.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_stage_ids_list_empty.assert_called_once()

    def test_with_invalid_task_json(
            self, interactor, presenter_mock, create_task_mock,
            create_task_log_mock, mock_object):
        # Arrange
        task_request_json = '{"key": "value"}'
        task_dto = CreateSubTaskDTOFactory()
        given_message = "given task json is not valid"
        create_task_log_mock.side_effect = InvalidTaskJson(given_message)
        presenter_mock.raise_invalid_task_json.return_value = mock_object

        # Act
        response = interactor.create_sub_task_wrapper(
            presenter_mock, task_dto, task_request_json)

        # Assert
        assert response == mock_object
        presenter_mock.raise_invalid_task_json.assert_called_once()

        call_args = presenter_mock.raise_invalid_task_json.call_args
        error_object = call_args[0][0]
        message = error_object.message

        assert message == given_message
