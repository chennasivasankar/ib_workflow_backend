# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_with_invalid_task_display_id http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_with_invalid_task_display_id res_status'] = 'INVALID_TASK_ID'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_with_invalid_task_display_id json_response'] = 'task_display_id is invalid task_id send valid task_id'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_action_id http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_action_id res_status'] = 'INVALID_ACTION_ID'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_action_id json_response'] = 'invalid action id is: 1, please send valid action id'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_task_id http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_task_id res_status'] = 'INVALID_TASK_ID'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_task_id json_response'] = 'invalid task id is: 1, please send valid task id'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_due_date_has_expired http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_due_date_has_expired res_status'] = 'DUE_DATE_HAS_EXPIRED'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_due_date_has_expired json_response'] = 'given due date 2020-03-05 has expired'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_due_time_format http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_due_time_format res_status'] = 'INVALID_DUE_TIME_FORMAT'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_due_time_format json_response'] = '55:55:03 has invalid due time format, time format should be HH:MM:SS'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_start_date_is_ahead_of_due_date http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_start_date_is_ahead_of_due_date res_status'] = 'START_DATE_IS_AHEAD_OF_DUE_DATE'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_start_date_is_ahead_of_due_date json_response'] = 'given start date 2020-05-04 is ahead of given due date 2020-04-04 '

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_due_time_has_expired_for_today http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_due_time_has_expired_for_today res_status'] = 'DUE_TIME_HAS_EXPIRED_FOR_TODAY'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_due_time_has_expired_for_today json_response'] = 'give due time 05:08:55 has expired for today date'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_task_template_ids http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_task_template_ids res_status'] = 'INVALID_TASK_TEMPLATE_IDS'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_task_template_ids json_response'] = "invalid task template ids: ['template_1', 'template_2']"

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_gof_ids http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_gof_ids res_status'] = 'INVALID_GOF_IDS'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_gof_ids json_response'] = "invalid gof ids: ['gof_1', 'gof_2']"

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_field_ids http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_field_ids res_status'] = 'INVALID_FIELD_IDS'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_field_ids json_response'] = "invalid field ids: ['field_1', 'field_2']"

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_gofs_given_to_a_task_template http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_gofs_given_to_a_task_template res_status'] = 'INVALID_GOFS_OF_TASK_TEMPLATE'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_gofs_given_to_a_task_template json_response'] = "invalid gofs ['gof_1', 'gof_2']  given to the task template template_1"

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_duplicate_field_ids_to_a_gof http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_duplicate_field_ids_to_a_gof res_status'] = 'DUPLICATE_FIELD_IDS_GIVEN_TO_A_GOF'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_duplicate_field_ids_to_a_gof json_response'] = "gof id gof_1 has duplicate field ids ['field_1', 'field_2']"

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_fields_given_to_a_gof http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_fields_given_to_a_gof res_status'] = 'INVALID_FIELDS_OF_GOF'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_fields_given_to_a_gof json_response'] = "invalid fields ['field_1', 'field_2']  given to the gof gof_1"

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_user_needs_gof_writable_permission http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_user_needs_gof_writable_permission res_status'] = 'USER_NEEDS_GOF_WRITABLE_PERMISSION'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_user_needs_field_writable_permission http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_user_needs_field_writable_permission res_status'] = 'USER_NEEDS_FILED_WRITABLE_PERMISSION'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_empty_value_in_required_field http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_empty_value_in_required_field res_status'] = 'EMPTY_VALUE_FOR_REQUIRED_FIELD'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_empty_value_in_required_field json_response'] = 'Given Empty value for the required field of field_id: field_1! Required field should not be empty'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_phone_number_value http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_phone_number_value res_status'] = 'INVALID_PHONE_NUMBER_VALUE'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_phone_number_value json_response'] = 'Invalid value for phone number: 99987272 for field: field_1'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_email_address http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_email_address res_status'] = 'INVALID_EMAIL'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_email_address json_response'] = 'Invalid value for email: google@google.mail for field: field_1'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_url_address http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_url_address res_status'] = 'INVALID_URL'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_url_address json_response'] = 'Invalid value for url: http://google.mail for field: field_1'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_weak_password http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_weak_password res_status'] = 'NOT_A_STRONG_PASSWORD'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_weak_password json_response'] = 'Given a weak password: admin123 for field: field_1! Try with atleast 8 characters including special characters'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_number_value http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_number_value res_status'] = 'INVALID_NUMBER_VALUE'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_number_value json_response'] = 'Invalid number: 98656 for field: field_1! Number should only consists digits'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_float_value http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_float_value res_status'] = 'INVALID_FLOAT_VALUE'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_float_value json_response'] = 'Invalid float value: 98656.0.0 for field: field_1!'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_dropdown_value http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_dropdown_value res_status'] = 'INVALID_VALUE_FOR_DROPDOWN'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_dropdown_value json_response'] = "Invalid dropdown value: city for field: field_1! Try with these dropdown values: ['Mr', 'Mrs']"

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_name_in_gof_selector_field_value http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_name_in_gof_selector_field_value res_status'] = 'INCORRECT_NAME_IN_GOF_SELECTOR_FIELD'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_choice_in_radio_group_field http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_choice_in_radio_group_field res_status'] = 'INCORRECT_RADIO_GROUP_CHOICE'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_choice_in_radio_group_field json_response'] = "Invalid radio group choice: city for field: field_1! Try with these valid options: ['Mr', 'Mrs']"

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_checkbox_group_options_selected http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_checkbox_group_options_selected res_status'] = 'INCORRECT_CHECK_BOX_OPTIONS_SELECTED'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_checkbox_group_options_selected json_response'] = "Invalid check box options selected: ['city', 'town'] for field: field_1! Try with these valid options: ['Mr', 'Mrs']"

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_options_selected http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_options_selected res_status'] = 'INCORRECT_MULTI_SELECT_OPTIONS_SELECTED'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_options_selected json_response'] = "Invalid multi select options selected: ['city', 'town'] for field: field_1! Try with these valid options: ['Mr', 'Mrs']"

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_labels_selected http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_labels_selected res_status'] = 'INCORRECT_MULTI_SELECT_LABELS_SELECTED'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_labels_selected json_response'] = "Invalid multi select labels selected: ['city', 'town'] for field: field_1! Try with these valid options: ['Mr', 'Mrs']"

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_date_format http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_date_format res_status'] = 'INVALID_DATE_FORMAT'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_date_format json_response'] = 'given invalid format for date: 03-05-2020 for field: field_1! Try with this format: YYYY-MM-DD'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_time_format http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_time_format res_status'] = 'INVALID_TIME_FORMAT'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_time_format json_response'] = 'given invalid format for time: 55:04:03 for field: field_1! Try with this format: HH:MM:SS'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_image_url http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_image_url res_status'] = 'INVALID_IMAGE_URL'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_image_url json_response'] = 'Invalid url for an image: http://google.com for field: field_1!'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_not_acceptable_image_format http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_not_acceptable_image_format res_status'] = 'INVALID_IMAGE_FORMAT'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_not_acceptable_image_format json_response'] = "Invalid format for an image: .png for field: field_1! Try with these formats: ['.jpg', '.jpeg']"

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_file_url http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_file_url res_status'] = 'INVALID_FILE_URL'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_file_url json_response'] = 'Invalid url for a file: http://google.com for field: field_1!'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_not_acceptable_file_format http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_not_acceptable_file_format res_status'] = 'INVALID_FILE_FORMAT'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_not_acceptable_file_format json_response'] = "Invalid format for a file: .png for field: field_1! Try with these formats: ['.pdf', '.txt']"

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_user_action_permission_denied http_status_code'] = 403

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_user_action_permission_denied res_status'] = 'USER_DO_NOT_HAVE_ACCESS'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_user_action_permission_denied response'] = 'User do not have access to the action: 1'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_present_actions http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_present_actions res_status'] = 'INVALID_PRESENT_STAGE_ACTION'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_present_actions response'] = '1 is invalid present stage action'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_key_error http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_key_error res_status'] = 'INVALID_KEY_ERROR'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_key_error response'] = 'invalid key error'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_custom_logic_function_exception http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_custom_logic_function_exception res_status'] = 'INVALID_CUSTOM_LOGIC'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_custom_logic_function_exception response'] = 'invalid custom logic'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_path_not_found_exception http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_path_not_found_exception res_status'] = 'PATH_NOT_FOUND'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_path_not_found_exception response'] = 'path not found'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_method_not_found_exception http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_method_not_found_exception res_status'] = 'METHOD_NOT_FOUND'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_method_not_found_exception response'] = 'method not found'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_duplicate_stage_ids_not_valid http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_duplicate_stage_ids_not_valid res_status'] = 'DUPLICATE_STAGE_IDS'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_duplicate_stage_ids_not_valid response'] = 'Duplicate stage ids that you have sent are: [1, 2, 3],please send unique stage ids'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_stage_ids_exception http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_stage_ids_exception res_status'] = 'INVALID_STAGE_IDS'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_invalid_stage_ids_exception response'] = 'Invalid stage ids that you have sent are: [1, 2],please send valid stage ids'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_stage_ids_with_invalid_permission_for_assignee_exception http_status_code'] = 400

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_stage_ids_with_invalid_permission_for_assignee_exception res_status'] = 'STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_stage_ids_with_invalid_permission_for_assignee_exception response'] = 'Stage ids with invalid permission of assignees that you have sent are: [1, 2],please assign valid assignees for stages'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_get_save_and_act_on_task_response task_current_stage_details'] = {
    'stages': [
        {
            'stage_display_name': 'stage_display_name_2',
            'stage_id': 'stage_2'
        },
        {
            'stage_display_name': 'stage_display_name_3',
            'stage_id': 'stage_3'
        }
    ],
    'task_id': 'task_display_0',
    'user_has_permission': True
}

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_user_needs_gof_writable_permission json_response'] = 'user needs write access on gof user_1, because user does not have at least one role in gof_1 roles'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_user_needs_field_writable_permission json_response'] = 'user needs write access on field user_1, because user does not have at least one role in field_1 roles'

snapshots['TestSaveAndActOnATaskPresenterImplementation.test_raise_exception_for_invalid_name_in_gof_selector_field_value json_response'] = "Invalid gof selector name: city for field: field_1! Try with these gof selector names: ['Mr', 'Mrs'] "
