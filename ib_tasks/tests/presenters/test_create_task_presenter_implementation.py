import datetime
import json

import pytest


class TestCreateTaskPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_tasks.presenters.create_task_presenter import \
            CreateTaskPresenterImplementation
        presenter = CreateTaskPresenterImplementation()

        return presenter

    def test_raise_invalid_project_id(self, snapshot, presenter):
        # Arrange
        project_id = "project_1"
        from ib_tasks.exceptions.custom_exceptions import InvalidProjectId
        err = InvalidProjectId(project_id)

        # Act
        response_object = presenter.raise_invalid_project_id(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_task_template_id(self, snapshot, presenter):
        # Arrange
        invalid_template_id = "template_1"

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskTemplateDBId
        err = InvalidTaskTemplateDBId(invalid_template_id)

        # Act
        response_object = presenter.raise_invalid_task_template_id(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_task_template_of_project(self, snapshot, presenter):
        # Arrange
        project_id = "project_1"
        template_id = "template_1"
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskTemplateOfProject
        err = InvalidTaskTemplateOfProject(project_id, template_id)

        # Act
        response_object = presenter.raise_invalid_task_template_of_project(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_action_id(self, snapshot, presenter):
        # Arrange
        expected_invalid_action_id = 1

        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException
        err = InvalidActionException(expected_invalid_action_id)

        # Act
        response_object = presenter.raise_invalid_action_id(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_duplicate_same_gof_orders_for_a_gof(
            self, snapshot, presenter):
        # Arrange
        expected_duplicate_same_gof_order = [1, 2]
        expected_gof_id = "gof_1"

        from ib_tasks.exceptions.gofs_custom_exceptions import \
            DuplicateSameGoFOrderForAGoF
        err = DuplicateSameGoFOrderForAGoF(
            expected_gof_id, expected_duplicate_same_gof_order)

        # Act
        response_object = \
            presenter.raise_duplicate_same_gof_orders_for_a_gof(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_priority_is_required(self, snapshot, presenter):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions import \
            PriorityIsRequired
        err = PriorityIsRequired()

        # Act
        response_object = presenter.raise_priority_is_required(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_due_date_time_without_start_datetime(
            self, snapshot, presenter):
        # Arrange
        due_datetime = datetime.datetime(2020, 5, 6, 4, 3, 1)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueDateTimeWithoutStartDateTimeIsNotValid
        err = DueDateTimeWithoutStartDateTimeIsNotValid(due_datetime)

        # Act
        response_object = \
            presenter.raise_due_date_time_without_start_datetime(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_start_date_time_is_required(self, snapshot, presenter):
        # Arrange
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            StartDateTimeIsRequired
        err = StartDateTimeIsRequired()

        # Act
        response_object = \
            presenter.raise_start_date_time_is_required(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_due_date_time_is_required(self, snapshot, presenter):
        # Arrange
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueDateTimeIsRequired
        err = DueDateTimeIsRequired()

        # Act
        response_object = presenter.raise_due_date_time_is_required(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_start_date_is_ahead_of_due_date(self, snapshot, presenter):
        # Arrange
        expected_start_date = datetime.date(2020, 5, 4)
        expected_due_date = datetime.date(2020, 4, 4)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            StartDateIsAheadOfDueDate

        err = StartDateIsAheadOfDueDate(expected_start_date, expected_due_date)

        # Act
        response_object = presenter.raise_start_date_is_ahead_of_due_date(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_due_date_time_has_expired(self, snapshot, presenter):
        # Arrange
        expected_due_date = datetime.datetime(2020, 4, 4, 2, 3, 1)
        from ib_tasks.exceptions.datetime_custom_exceptions import \
            DueDateTimeHasExpired

        err = DueDateTimeHasExpired(expected_due_date)

        # Act
        response_object = presenter.raise_due_date_time_has_expired(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_gof_ids(self, snapshot, presenter):
        # Arrange
        expected_invalid_gof_ids = ["gof_1", "gof_2"]

        from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
        err = InvalidGoFIds(expected_invalid_gof_ids)

        # Act
        response_object = presenter.raise_invalid_gof_ids(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_gofs_given_to_a_task_template(
            self, snapshot, presenter):
        # Arrange
        task_template_id = "template_1"
        expected_invalid_gofs_to_task_template = ["gof_1", "gof_2"]

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidGoFsOfTaskTemplate
        err = InvalidGoFsOfTaskTemplate(
            expected_invalid_gofs_to_task_template, task_template_id)

        # Act
        response_object = \
            presenter.raise_invalid_gofs_given_to_a_task_template(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_field_ids(self, snapshot, presenter):
        # Arrange
        expected_invalid_filed_ids = ["field_1", "field_2"]

        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidFieldIds
        err = InvalidFieldIds(expected_invalid_filed_ids)

        # Act
        response_object = presenter.raise_invalid_field_ids(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_duplicate_field_ids_to_a_gof(self, snapshot, presenter):
        # Arrange
        expected_gof_id = "gof_1"
        expected_duplicate_field_ids = ["field_1", "field_2"]

        from ib_tasks.exceptions.fields_custom_exceptions import \
            DuplicateFieldIdsToGoF
        err = DuplicateFieldIdsToGoF(
            expected_gof_id, expected_duplicate_field_ids)

        # Act
        response_object = \
            presenter.raise_duplicate_field_ids_to_a_gof(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_fields_given_to_a_gof(self, snapshot, presenter):
        # Arrange
        expected_gof_id = "gof_1"
        expected_invalid_field_ids = ["field_1", "field_2"]

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidFieldsOfGoF
        err = InvalidFieldsOfGoF(expected_gof_id, expected_invalid_field_ids)

        # Act
        response_object = presenter.raise_invalid_fields_given_to_a_gof(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_stage_permitted_gofs(self, snapshot, presenter):
        # Arrange
        expected_gof_ids = ["gof_1", "gof_2"]
        stage_id = 1
        expected_invalid_field_ids = ["field_1", "field_2"]

        from ib_tasks.exceptions.gofs_custom_exceptions import \
            InvalidStagePermittedGoFs
        err = InvalidStagePermittedGoFs(expected_gof_ids, stage_id)

        # Act
        response_object = presenter.raise_invalid_stage_permitted_gofs(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_user_needs_gof_writable_permission(
            self, snapshot, presenter):
        # Arrange
        expected_user_id = 'user_1'
        expected_gof_id = "gof_1"
        expected_roles = ["role_1", "role_2"]

        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserNeedsGoFWritablePermission
        err = UserNeedsGoFWritablePermission(
            expected_user_id, expected_gof_id, expected_roles)

        # Act
        response_object = \
            presenter.raise_user_needs_gof_writable_permission(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_user_needs_field_writable_permission(
            self, snapshot, presenter):
        # Arrange
        expected_user_id = 'user_1'
        expected_field_id = "field_1"
        expected_roles = ["role_1", "role_2"]

        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserNeedsFieldWritablePermission
        err = UserNeedsFieldWritablePermission(
            expected_user_id, expected_field_id, expected_roles)

        # Act
        response_object = \
            presenter.raise_user_needs_field_writable_permission(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_user_did_not_fill_required_fields(
            self, snapshot, presenter):
        # Arrange
        from ib_tasks.exceptions.fields_custom_exceptions import \
            UserDidNotFillRequiredFields
        from ib_tasks.tests.factories.storage_dtos import \
            FieldIdWithFieldDisplayNameDTOFactory

        FieldIdWithFieldDisplayNameDTOFactory.reset_sequence()
        unfilled_field_dtos = \
            FieldIdWithFieldDisplayNameDTOFactory.create_batch(size=2)

        err = UserDidNotFillRequiredFields(unfilled_field_dtos)

        # Act
        response_object = \
            presenter.raise_user_did_not_fill_required_fields(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_empty_value_in_required_field(self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            EmptyValueForRequiredField

        err = EmptyValueForRequiredField(expected_field_id)

        # Act
        response_object = \
            presenter.raise_empty_value_in_required_field(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_phone_number_value(
            self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_phone_number = "99987272"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidPhoneNumberValue
        err = InvalidPhoneNumberValue(expected_field_id, expected_phone_number)

        # Act
        response_object = presenter.raise_invalid_phone_number_value(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_email_address(
            self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_email = "google@google.mail"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidEmailFieldValue
        err = InvalidEmailFieldValue(expected_field_id, expected_email)

        # Act
        response_object = presenter.raise_invalid_email_address(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_url_address(
            self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_url = "http://google.mail"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidURLValue
        err = InvalidURLValue(expected_field_id, expected_url)

        # Act
        response_object = presenter.raise_invalid_url_address(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_weak_password(self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_password = "admin123"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            NotAStrongPassword
        err = NotAStrongPassword(expected_field_id, expected_password)

        # Act
        response_object = presenter.raise_weak_password(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_number_value(
            self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_number = "98656"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidNumberValue
        err = InvalidNumberValue(expected_field_id, expected_number)

        # Act
        response_object = presenter.raise_invalid_number_value(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_float_value(
            self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_float = "98656.0.0"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFloatValue
        err = InvalidFloatValue(expected_field_id, expected_float)

        # Act
        response_object = presenter.raise_invalid_float_value(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_dropdown_value(
            self, snapshot, presenter):
        # Arrange
        expected_valid_values = ["Mr", "Mrs"]
        expected_field_id = "field_1"
        expected_dropdown_value = "city"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidValueForDropdownField
        err = InvalidValueForDropdownField(
            expected_field_id, expected_dropdown_value, expected_valid_values)

        # Act
        response_object = presenter.raise_invalid_dropdown_value(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_name_in_gof_selector_field_value(
            self, snapshot, presenter):
        # Arrange
        expected_valid_values = ["Mr", "Mrs"]
        expected_field_id = "field_1"
        expected_gof_name_value = "city"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectNameInGoFSelectorField
        err = IncorrectNameInGoFSelectorField(
            expected_field_id, expected_gof_name_value, expected_valid_values)

        # Act
        response_object = presenter.raise_invalid_name_in_gof_selector(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_choice_in_radio_group_field(
            self, snapshot, presenter):
        # Arrange
        expected_valid_values = ["Mr", "Mrs"]
        expected_field_id = "field_1"
        expected_radio_choice = "city"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectRadioGroupChoice
        err = IncorrectRadioGroupChoice(
            expected_field_id, expected_radio_choice, expected_valid_values)

        # Act
        response_object = presenter. \
            raise_invalid_choice_in_radio_group_field(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_checkbox_group_options_selected(
            self, snapshot, presenter):
        # Arrange
        expected_valid_values = ["Mr", "Mrs"]
        expected_field_id = "field_1"
        expected_checkbox_choices = ["city", "town"]

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectCheckBoxOptionsSelected
        err = IncorrectCheckBoxOptionsSelected(
            expected_field_id, expected_checkbox_choices,
            expected_valid_values)

        # Act
        response_object = presenter. \
            raise_invalid_checkbox_group_options_selected(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_multi_select_options_selected(
            self, snapshot, presenter):
        # Arrange
        expected_valid_values = ["Mr", "Mrs"]
        expected_field_id = "field_1"
        expected_multi_select_options_selected = ["city", "town"]

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectOptionsSelected
        err = IncorrectMultiSelectOptionsSelected(
            expected_field_id, expected_multi_select_options_selected,
            expected_valid_values)

        # Act
        response_object = presenter. \
            raise_invalid_multi_select_options_selected(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_multi_select_labels_selected(
            self, snapshot, presenter):
        # Arrange
        expected_valid_values = ["Mr", "Mrs"]
        expected_field_id = "field_1"
        expected_multi_select_labels_selected = ["city", "town"]

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            IncorrectMultiSelectLabelsSelected
        err = IncorrectMultiSelectLabelsSelected(
            expected_field_id, expected_multi_select_labels_selected,
            expected_valid_values)

        # Act
        response_object = presenter. \
            raise_invalid_multi_select_labels_selected(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_date_format(
            self, snapshot, presenter):
        # Arrange
        expected_given_date_format = "03-05-2020"
        expected_field_id = "field_1"
        expected_valid_date_format = "YYYY-MM-DD"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidDateFormat
        err = InvalidDateFormat(
            expected_field_id, expected_given_date_format,
            expected_valid_date_format)

        # Act
        response_object = presenter.raise_invalid_date_format(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_time_format(
            self, snapshot, presenter):
        # Arrange
        expected_given_time_format = "55:04:03"
        expected_field_id = "field_1"
        expected_valid_time_format = "HH:MM:SS"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidTimeFormat
        err = InvalidTimeFormat(
            expected_field_id, expected_given_time_format,
            expected_valid_time_format)

        # Act
        response_object = presenter.raise_invalid_time_format(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_image_url(self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_invalid_image_url = "http://google.com"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForImage
        err = InvalidUrlForImage(expected_field_id, expected_invalid_image_url)

        # Act
        response_object = presenter.raise_invalid_image_url(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_not_acceptable_image_format(
            self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_invalid_image_format = ".png"
        expected_valid_formats = [".jpg", ".jpeg"]

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidImageFormat
        err = InvalidImageFormat(
            expected_field_id, expected_invalid_image_format,
            expected_valid_formats)

        # Act
        response_object = presenter.raise_not_acceptable_image_format(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_file_url(self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_invalid_file_url = "http://google.com"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForFile
        err = InvalidUrlForFile(
            expected_field_id, expected_invalid_file_url)

        # Act
        response_object = presenter.raise_invalid_file_url(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_not_acceptable_file_format(
            self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_invalid_file_format = ".png"
        expected_valid_formats = [".pdf", ".txt"]

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFileFormat
        err = InvalidFileFormat(
            expected_field_id, expected_invalid_file_format,
            expected_valid_formats)

        # Act
        response_object = presenter.raise_not_acceptable_file_format(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_user_action_permission_denied(
            self, snapshot, presenter):
        # Arrange
        expected_action_id = 1

        from ib_tasks.exceptions.permission_custom_exceptions import \
            UserActionPermissionDenied
        err = UserActionPermissionDenied(expected_action_id)

        # Act
        response_object = presenter.raise_user_action_permission_denied(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_exception_for_invalid_present_stage_actions(
            self, snapshot, presenter):
        # Arrange
        action_id = 1
        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidPresentStageAction
        err = InvalidPresentStageAction(action_id)

        # Act
        response_object = presenter.raise_invalid_present_stage_actions(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_key_error(self, snapshot, presenter):
        # Act
        response_object = presenter.raise_invalid_key_error()

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_path_not_found_exception(self, snapshot, presenter):
        # Arrange
        expected_path_name = "home"

        from ib_tasks.interactors.user_action_on_task. \
            call_action_logic_function_and_get_or_update_task_status_variables_interactor \
            import InvalidModulePathFound
        error_object = InvalidModulePathFound(expected_path_name)

        # Act
        response_object = presenter.raise_invalid_path_not_found(error_object)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_method_not_found_exception(
            self, snapshot, presenter):
        # Arrange
        expected_method = "some_method"
        from ib_tasks.interactors.user_action_on_task. \
            call_action_logic_function_and_get_or_update_task_status_variables_interactor \
            import InvalidMethodFound
        error_object = InvalidMethodFound(expected_method)

        # Act
        response_object = \
            presenter.raise_invalid_method_not_found(error_object)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_duplicate_stage_ids_not_valid(self, snapshot, presenter):
        # Arrange
        from ib_tasks.exceptions.stage_custom_exceptions import \
            DuplicateStageIds

        expected_duplicate_stage_ids = [1, 2, 3]
        err = DuplicateStageIds(
            duplicate_stage_ids=expected_duplicate_stage_ids)

        # Act
        response_object = presenter.raise_duplicate_stage_ids_not_valid(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_stage_ids_exception(self, snapshot, presenter):
        # Arrange
        expected_invalid_stage_ids = [1, 2]
        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidDbStageIdsListException
        error_object = InvalidDbStageIdsListException(
            expected_invalid_stage_ids)

        # Act
        response_object = presenter.raise_invalid_stage_ids(error_object)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_stage_ids_with_invalid_permission_for_assignee_exception(
            self, snapshot, presenter):
        # Arrange

        expected_stage_ids_without_assignee_permissions = [1, 2]
        from ib_tasks.exceptions.stage_custom_exceptions import \
            StageIdsWithInvalidPermissionForAssignee
        err = StageIdsWithInvalidPermissionForAssignee(
            invalid_stage_ids=expected_stage_ids_without_assignee_permissions)

        # Act
        response_object = presenter.raise_invalid_stage_assignees(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_stage_ids_list_empty(self, snapshot, presenter):
        # Arrange
        from ib_tasks.exceptions.stage_custom_exceptions import \
            StageIdsListEmptyException
        err = StageIdsListEmptyException()

        # Act
        response_object = presenter.raise_stage_ids_list_empty(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_stage_ids_list(self, snapshot, presenter):
        # Arrange
        invalid_stage_ids = ["stage_1", "stage_2"]
        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidStageIdsListException
        err = InvalidStageIdsListException(invalid_stage_ids)

        # Act
        response_object = presenter.raise_invalid_stage_ids_list(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_raise_invalid_task_json(self, snapshot, presenter):
        # Arrange
        task_json = '{"task_id": "task_1"}'
        from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskJson
        err = InvalidTaskJson(task_json)

        # Act
        response_object = presenter.raise_invalid_task_json(err)

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response['http_status_code'], 'http_status_code')
        snapshot.assert_match(response['res_status'], 'res_status')
        snapshot.assert_match(response['response'], 'response')

    def test_get_create_task_response(self, snapshot, presenter):
        # Arrange
        from ib_tasks.tests.factories.interactor_dtos import \
            TaskCurrentStageDetailsDTOFactory
        from ib_tasks.tests.factories.presenter_dtos import \
            AllTasksOverviewDetailsDTOFactory
        from ib_tasks.tests.factories.presenter_dtos import \
            TaskIdWithStageDetailsDTOFactory

        AllTasksOverviewDetailsDTOFactory.reset_sequence()
        TaskCurrentStageDetailsDTOFactory.reset_sequence()
        TaskIdWithStageDetailsDTOFactory.reset_sequence()

        all_tasks_overview_dto = AllTasksOverviewDetailsDTOFactory()
        task_current_stage_details_dto = TaskCurrentStageDetailsDTOFactory()

        # Act
        response_object = presenter.get_create_task_response(
            task_current_stage_details_dto=task_current_stage_details_dto,
            all_tasks_overview_dto=all_tasks_overview_dto
        )

        # Assert
        response = json.loads(response_object.content)
        snapshot.assert_match(response, 'create_task_response')
