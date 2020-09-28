# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_parent_task_id http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_parent_task_id res_status'] = 'INVALID_PARENT_TASK_ID'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_parent_task_id response'] = 'IBWF-1 is an invalid parent task id, please give a valid parent task id'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_project_id http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_project_id res_status'] = 'INVALID_PROJECT_ID'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_project_id response'] = 'project_1 is invalid project id, please send valid project id'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_task_template_id http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_task_template_id res_status'] = 'INVALID_TASK_TEMPLATE_DB_ID'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_task_template_id response'] = 'template_1 invalid task template id, please give a valid task template id'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_task_template_of_project http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_task_template_of_project res_status'] = 'INVALID_PROJECT_TEMPLATE'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_task_template_of_project response'] = 'template_1 is not valid template for given project project_1'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_action_id http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_action_id res_status'] = 'INVALID_ACTION_ID'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_action_id response'] = 'invalid action id is: 1, please send valid action id'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_duplicate_same_gof_orders_for_a_gof http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_duplicate_same_gof_orders_for_a_gof res_status'] = 'DUPLICATE_SAME_GOF_ORDERS_FOR_A_GOF'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_duplicate_same_gof_orders_for_a_gof response'] = 'duplicate same gof orders given for gof gof_1, duplicates are [1, 2]'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_priority_is_required http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_priority_is_required res_status'] = 'PRIORITY_IS_REQUIRED'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_priority_is_required response'] = 'task priority is required if action type is not no validations'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_due_date_time_without_start_datetime http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_due_date_time_without_start_datetime res_status'] = 'DUE_DATE_TIME_WITHOUT_START_DATE_TIME'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_due_date_time_without_start_datetime response'] = 'due date time 2020-05-06 04:03:01 is given with out start datetime'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_start_date_time_is_required http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_start_date_time_is_required res_status'] = 'START_DATE_TIME_IS_REQUIRED'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_start_date_time_is_required response'] = 'start datetime is required if action type is not no validations'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_due_date_time_is_required http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_due_date_time_is_required res_status'] = 'DUE_DATE_TIME_IS_REQUIRED'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_due_date_time_is_required response'] = 'due datetime is required if action type is not no validations'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_start_date_is_ahead_of_due_date http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_start_date_is_ahead_of_due_date res_status'] = 'START_DATE_IS_AHEAD_OF_DUE_DATE'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_start_date_is_ahead_of_due_date response'] = 'given start date 2020-05-04 is ahead of given due date 2020-04-04 '

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_due_date_time_has_expired http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_due_date_time_has_expired res_status'] = 'DUE_DATE_TIME_HAS_EXPIRED'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_due_date_time_has_expired response'] = 'given due date time 2020-04-04 02:03:01 has expired, please give a valid due date time'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_gof_ids http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_gof_ids res_status'] = 'INVALID_GOF_IDS'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_gof_ids response'] = "invalid gof ids: ['gof_1', 'gof_2']"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_gofs_given_to_a_task_template http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_gofs_given_to_a_task_template res_status'] = 'INVALID_GOFS_OF_TASK_TEMPLATE'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_gofs_given_to_a_task_template response'] = "invalid gofs ['gof_1', 'gof_2']  given to the task template template_1"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_field_ids http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_field_ids res_status'] = 'INVALID_FIELD_IDS'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_field_ids response'] = "invalid field ids: ['field_1', 'field_2']"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_duplicate_field_ids_to_a_gof http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_duplicate_field_ids_to_a_gof res_status'] = 'DUPLICATE_FIELD_IDS_GIVEN_TO_A_GOF'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_duplicate_field_ids_to_a_gof response'] = "gof id gof_1 has duplicate field ids ['field_1', 'field_2']"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_fields_given_to_a_gof http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_fields_given_to_a_gof res_status'] = 'INVALID_FIELDS_OF_GOF'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_fields_given_to_a_gof response'] = "invalid fields ['field_1', 'field_2']  given to the gof gof_1"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_stage_permitted_gofs http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_stage_permitted_gofs res_status'] = 'INVALID_STAGE_PERMITTED_GOFS'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_stage_permitted_gofs response'] = "['gof_1', 'gof_2'] gof ids are not permitted for the stage 1"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_user_needs_gof_writable_permission http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_user_needs_gof_writable_permission res_status'] = 'USER_NEEDS_GOF_WRITABLE_PERMISSION'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_user_needs_gof_writable_permission response'] = "user needs write access on gof gof_1, because user does not have at least one role in ['role_1', 'role_2'] roles"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_user_needs_field_writable_permission http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_user_needs_field_writable_permission res_status'] = 'USER_NEEDS_FILED_WRITABLE_PERMISSION'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_user_needs_field_writable_permission response'] = "user needs write access on field field_1, because user does not have at least one role in ['role_1', 'role_2'] roles"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_user_did_not_fill_required_fields http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_user_did_not_fill_required_fields res_status'] = 'USER_DID_NOT_FILL_REQUIRED_FIELDS'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_user_did_not_fill_required_fields response'] = "user did not fill required fields: ['field_display_name_0', 'field_display_name_1']"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_empty_value_in_required_field http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_empty_value_in_required_field res_status'] = 'EMPTY_VALUE_FOR_REQUIRED_FIELD'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_empty_value_in_required_field response'] = 'Given Empty value for the required field of field_id: field_1! Required field should not be empty'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_phone_number_value http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_phone_number_value res_status'] = 'INVALID_PHONE_NUMBER_VALUE'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_phone_number_value response'] = 'Invalid value for phone number: 99987272 for field: field_1'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_email_address http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_email_address res_status'] = 'INVALID_EMAIL'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_email_address response'] = 'Invalid value for email: google@google.mail for field: field_1'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_url_address http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_url_address res_status'] = 'INVALID_URL'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_url_address response'] = 'Invalid value for url: http://google.mail for field: field_1'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_weak_password http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_weak_password res_status'] = 'NOT_A_STRONG_PASSWORD'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_weak_password response'] = 'Given a weak password: admin123 for field: field_1! Try with at least 6 characters including special characters'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_number_value http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_number_value res_status'] = 'INVALID_NUMBER_VALUE'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_number_value response'] = 'Invalid number: 98656 for field: field_1! Number should only consists digits'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_float_value http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_float_value res_status'] = 'INVALID_FLOAT_VALUE'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_float_value response'] = 'Invalid float value: 98656.0.0 for field: field_1!'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_dropdown_value http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_dropdown_value res_status'] = 'INVALID_VALUE_FOR_DROPDOWN'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_dropdown_value response'] = "Invalid dropdown value: city for field: field_1! Try with these dropdown values: ['Mr', 'Mrs']"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_name_in_gof_selector_field_value http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_name_in_gof_selector_field_value res_status'] = 'INCORRECT_NAME_IN_GOF_SELECTOR_FIELD'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_name_in_gof_selector_field_value response'] = "Invalid gof selector name: city for field: field_1! Try with these gof selector names: ['Mr', 'Mrs'] "

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_choice_in_radio_group_field http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_choice_in_radio_group_field res_status'] = 'INCORRECT_RADIO_GROUP_CHOICE'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_choice_in_radio_group_field response'] = "Invalid radio group choice: city for field: field_1! Try with these valid options: ['Mr', 'Mrs']"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_checkbox_group_options_selected http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_checkbox_group_options_selected res_status'] = 'INCORRECT_CHECK_BOX_OPTIONS_SELECTED'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_checkbox_group_options_selected response'] = "Invalid check box options selected: ['city', 'town'] for field: field_1! Try with these valid options: ['Mr', 'Mrs']"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_options_selected http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_options_selected res_status'] = 'INCORRECT_MULTI_SELECT_OPTIONS_SELECTED'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_options_selected response'] = "Invalid multi select options selected: ['city', 'town'] for field: field_1! Try with these valid options: ['Mr', 'Mrs']"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_labels_selected http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_labels_selected res_status'] = 'INCORRECT_MULTI_SELECT_LABELS_SELECTED'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_labels_selected response'] = "Invalid multi select labels selected: ['city', 'town'] for field: field_1! Try with these valid options: ['Mr', 'Mrs']"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_date_format http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_date_format res_status'] = 'INVALID_DATE_FORMAT'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_date_format response'] = 'given invalid format for date: 03-05-2020 for field: field_1! Try with this format: YYYY-MM-DD'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_time_format http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_time_format res_status'] = 'INVALID_TIME_FORMAT'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_time_format response'] = 'given invalid format for time: 55:04:03 for field: field_1! Try with this format: HH:MM:SS'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_image_url http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_image_url res_status'] = 'INVALID_IMAGE_URL'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_image_url response'] = 'Invalid url for an image: http://google.com for field: field_1!'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_not_acceptable_image_format http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_not_acceptable_image_format res_status'] = 'INVALID_IMAGE_FORMAT'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_not_acceptable_image_format response'] = "Invalid format for an image: .png for field: field_1! Try with these formats: ['.jpg', '.jpeg']"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_file_url http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_file_url res_status'] = 'INVALID_FILE_URL'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_file_url response'] = 'Invalid url for a file: http://google.com for field: field_1!'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_not_acceptable_file_format http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_not_acceptable_file_format res_status'] = 'INVALID_FILE_FORMAT'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_not_acceptable_file_format response'] = "Invalid format for a file: .png for field: field_1! Try with these formats: ['.pdf', '.txt']"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_user_action_permission_denied http_status_code'] = 403

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_user_action_permission_denied res_status'] = 'USER_DO_NOT_HAVE_ACCESS'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_user_action_permission_denied response'] = 'User do not have access to the action: 1'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_present_stage_actions http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_present_stage_actions res_status'] = 'INVALID_PRESENT_STAGE_ACTION'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_exception_for_invalid_present_stage_actions response'] = '1 is invalid present stage action'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_key_error http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_key_error res_status'] = 'INVALID_KEY_ERROR'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_key_error response'] = 'invalid key error'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_path_not_found_exception http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_path_not_found_exception res_status'] = 'PATH_NOT_FOUND'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_path_not_found_exception response'] = 'path not found'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_method_not_found_exception http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_method_not_found_exception res_status'] = 'METHOD_NOT_FOUND'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_method_not_found_exception response'] = 'method not found'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_duplicate_stage_ids_not_valid http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_duplicate_stage_ids_not_valid res_status'] = 'DUPLICATE_STAGE_IDS'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_duplicate_stage_ids_not_valid response'] = 'Duplicate stage ids that you have sent are: [1, 2, 3],please send unique stage ids'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_stage_ids_exception http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_stage_ids_exception res_status'] = 'INVALID_STAGE_IDS'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_stage_ids_exception response'] = 'Invalid stage ids that you have sent are: [1, 2],please send valid stage ids'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_stage_ids_with_invalid_permission_for_assignee_exception http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_stage_ids_with_invalid_permission_for_assignee_exception res_status'] = 'STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_stage_ids_with_invalid_permission_for_assignee_exception response'] = 'Stage ids with invalid permission of assignees that you have sent are: [1, 2],please assign valid assignees for stages'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_stage_ids_list_empty http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_stage_ids_list_empty res_status'] = 'EMPTY_STAGE_IDS_ARE_INVALID'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_stage_ids_list_empty response'] = 'Stage Ids list should not be empty'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_stage_ids_list http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_stage_ids_list res_status'] = 'INVALID_STAGE_IDS'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_stage_ids_list response'] = "Invalid stage ids that you have sent are: ['stage_1', 'stage_2'],please send valid stage ids"

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_task_json http_status_code'] = 400

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_task_json res_status'] = 'INVALID_TASK_JSON'

snapshots['TestCreateSubTaskPresenterImplementation.test_raise_invalid_task_json response'] = 'Invalid task json object received'

snapshots['TestCreateSubTaskPresenterImplementation.test_get_create_sub_task_response create_sub_task_response'] = {
    'created_task_id': 'IBWF-1',
    'task_current_stages_details': {
        'stages': [
            {
                'stage_display_name': 'stage_display_name_0',
                'stage_id': 'stage_0'
            },
            {
                'stage_display_name': 'stage_display_name_1',
                'stage_id': 'stage_1'
            }
        ],
        'task_id': 'task_display_0',
        'user_has_permission': True
    },
    'task_details': {
        'stage_with_actions': {
            'actions': [
            ],
            'assignee': {
                'assignee_id': '123e4567-e89b-12d3-a456-426614174000',
                'name': 'name_0',
                'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM',
                'team_info': {
                    'team_id': 'team_0',
                    'team_name': 'team_name0'
                }
            },
            'stage_color': 'color_1',
            'stage_display_name': 'stage_display_1',
            'stage_id': 1
        },
        'task_id': 'iBWF-1',
        'task_overview_fields': [
        ]
    }
}