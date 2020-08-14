import json

import pytest


class TestCreateTransitionChecklistTemplatePresenterImplementation:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        pass

    @pytest.fixture
    def presenter(self):
        from ib_tasks.presenters.create_transition_checklist_presenter import \
            CreateTransitionChecklistTemplatePresenterImplementation
        return CreateTransitionChecklistTemplatePresenterImplementation()

    def test_with_invalid_task_display_id(self, presenter, snapshot):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskDisplayId
        task_display_id = "task_display_id"
        err = InvalidTaskDisplayId(task_display_id)

        # Act
        json_response = presenter.raise_invalid_task_display_id(err)

        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')

    def test_raise_invalid_task_id(self, presenter, snapshot):
        # Arrange

        task_id = 1
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskIdException
        err = InvalidTaskIdException(task_id)

        # Act
        json_response = presenter.raise_invalid_task_id(err)

        # Assert
        json_json_response = json.loads(json_response.content)
        snapshot.assert_match(
            json_json_response['http_status_code'], 'http_status_code')
        snapshot.assert_match(json_json_response['res_status'], 'res_status')
        snapshot.assert_match(json_json_response['response'],
                              'json_response')

    def test_raise_invalid_transition_checklist_template_id(self, snapshot,
                                                            presenter):
        # Arrange
        transition_checklist_template_id = "transition_checklist_template_id"

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTransitionChecklistTemplateId
        err = InvalidTransitionChecklistTemplateId(
            transition_checklist_template_id)

        # Act
        response = presenter.raise_invalid_transition_checklist_template_id(
            err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_invalid_action(self, snapshot, presenter):
        # Arrange
        action_id = 1

        from ib_tasks.exceptions.action_custom_exceptions import \
            InvalidActionException
        err = InvalidActionException(action_id=action_id)

        # Act
        response = presenter.raise_invalid_action(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_invalid_gof_ids(self, snapshot, presenter):
        # Arrange
        expected_invalid_gof_ids = ["gof_1", "gof_2"]

        from ib_tasks.exceptions.gofs_custom_exceptions import InvalidGoFIds
        err = InvalidGoFIds(expected_invalid_gof_ids)

        # Act
        response = presenter.raise_invalid_gof_ids(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_invalid_field_ids(self, snapshot, presenter):
        # Arrange
        expected_invalid_filed_ids = ["field_1", "field_2"]

        from ib_tasks.exceptions.fields_custom_exceptions import \
            InvalidFieldIds
        err = InvalidFieldIds(expected_invalid_filed_ids)

        # Act
        response = presenter.raise_invalid_field_ids(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

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
        response = \
            presenter.raise_invalid_gofs_given_to_a_task_template(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_duplicate_field_ids_to_a_gof(self, snapshot, presenter):
        # Arrange
        expected_gof_id = "gof_1"
        expected_duplicate_field_ids = ["field_1", "field_2"]

        from ib_tasks.exceptions.fields_custom_exceptions import \
            DuplicateFieldIdsToGoF
        err = DuplicateFieldIdsToGoF(
            expected_gof_id, expected_duplicate_field_ids)

        # Act
        response = \
            presenter.raise_duplicate_field_ids_to_a_gof(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_invalid_fields_given_to_a_gof(self, snapshot, presenter):
        # Arrange
        expected_gof_id = "gof_1"
        expected_invalid_field_ids = ["field_1", "field_2"]

        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidFieldsOfGoF
        err = InvalidFieldsOfGoF(expected_gof_id, expected_invalid_field_ids)

        # Act
        response = presenter.raise_invalid_fields_given_to_a_gof(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

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
        response = \
            presenter.raise_user_needs_gof_writable_permission(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

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
        response = \
            presenter.raise_user_needs_field_writable_permission(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_exception_for_empty_value_in_required_field(
            self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            EmptyValueForRequiredField
        err = EmptyValueForRequiredField(expected_field_id)

        # Act
        response = \
            presenter.raise_exception_for_empty_value_in_required_field(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_exception_for_invalid_phone_number_value(
            self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_phone_number = "99987272"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidPhoneNumberValue
        err = InvalidPhoneNumberValue(expected_field_id, expected_phone_number)

        # Act
        response = \
            presenter.raise_exception_for_invalid_phone_number_value(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_exception_for_invalid_email_address(
            self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_email = "google@google.mail"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidEmailFieldValue
        err = InvalidEmailFieldValue(expected_field_id, expected_email)

        # Act
        response = \
            presenter.raise_exception_for_invalid_email_address(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_exception_for_invalid_url_address(
            self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_url = "http://google.mail"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidURLValue
        err = InvalidURLValue(expected_field_id, expected_url)

        # Act
        response = \
            presenter.raise_exception_for_invalid_url_address(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_exception_for_weak_password(self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_password = "admin123"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            NotAStrongPassword
        err = NotAStrongPassword(expected_field_id, expected_password)

        # Act
        response = presenter.raise_exception_for_weak_password(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_exception_for_invalid_number_value(
            self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_number = "98656"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidNumberValue
        err = InvalidNumberValue(expected_field_id, expected_number)

        # Act
        response = \
            presenter.raise_exception_for_invalid_number_value(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_exception_for_invalid_float_value(
            self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_float = "98656.0.0"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidFloatValue
        err = InvalidFloatValue(expected_field_id, expected_float)

        # Act
        response = \
            presenter.raise_exception_for_invalid_float_value(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

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
        response = \
            presenter.raise_exception_for_invalid_dropdown_value(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

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
        response = presenter. \
            raise_exception_for_invalid_name_in_gof_selector_field_value(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

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
        response = presenter. \
            raise_exception_for_invalid_choice_in_radio_group_field(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

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
        response = presenter. \
            raise_exception_for_invalid_checkbox_group_options_selected(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

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
        response = presenter. \
            raise_exception_for_invalid_multi_select_options_selected(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

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
        response = presenter. \
            raise_exception_for_invalid_multi_select_labels_selected(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

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
        response = \
            presenter.raise_exception_for_invalid_date_format(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

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
        response = \
            presenter.raise_exception_for_invalid_time_format(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_exception_for_invalid_image_url(self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_invalid_image_url = "http://google.com"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForImage
        err = InvalidUrlForImage(expected_field_id, expected_invalid_image_url)

        # Act
        response = presenter.raise_exception_for_invalid_image_url(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

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
        response = \
            presenter.raise_exception_for_not_acceptable_image_format(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_exception_for_invalid_file_url(self, snapshot, presenter):
        # Arrange
        expected_field_id = "field_1"
        expected_invalid_file_url = "http://google.com"

        from ib_tasks.exceptions.field_values_custom_exceptions import \
            InvalidUrlForFile
        err = InvalidUrlForFile(
            expected_field_id, expected_invalid_file_url)

        # Act
        response = presenter.raise_exception_for_invalid_file_url(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

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
        response = \
            presenter.raise_exception_for_not_acceptable_file_format(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'json_response')

    def test_raise_invalid_stage_id(self, snapshot, presenter):
        # Arrange
        stage_id = 1
        from ib_tasks.exceptions.stage_custom_exceptions import InvalidStageId
        err = InvalidStageId(stage_id)

        # Act
        response = presenter.raise_invalid_stage_id(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'response')

    def test_raise_transition_template_is_not_related_to_given_stage_action(
            self, snapshot, presenter):
        # Arrange
        stage_id = 1
        action_id = 2
        transition_checklist_template_id = "transition_template_1"
        from ib_tasks.exceptions.stage_custom_exceptions import \
            TransitionTemplateIsNotRelatedToGivenStageAction
        err = TransitionTemplateIsNotRelatedToGivenStageAction(
            transition_checklist_template_id, action_id, stage_id)

        # Act
        response = \
            presenter.raise_transition_template_is_not_related_to_given_stage_action(
                err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'response')

    def test_raise_same_gof_order_for_a_gof(
            self, snapshot, presenter):
        # Arrange
        gof_id = "gof_1"
        duplicate_same_gof_order = [1]
        from ib_tasks.exceptions.gofs_custom_exceptions import \
            DuplicateSameGoFOrderForAGoF
        err = DuplicateSameGoFOrderForAGoF(gof_id, duplicate_same_gof_order)

        # Act
        response = presenter.raise_same_gof_order_for_a_gof(err)

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(json_response['http_status_code'],
                              'http_status_code')
        snapshot.assert_match(json_response['res_status'], 'res_status')
        snapshot.assert_match(json_response['response'], 'response')

    def test_get_create_transition_checklist_response(self, snapshot,
                                                      presenter):
        # Act
        response = presenter.get_create_transition_checklist_response()

        # Assert
        json_response = json.loads(response.content)
        snapshot.assert_match(name="success_message", value=json_response)