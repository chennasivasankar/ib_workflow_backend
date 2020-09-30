# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestUpdateTaskPresenterImplementation.test_with_invalid_task_display_id http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_with_invalid_task_display_id res_status'] = 'INVALID_TASK_ID'

snapshots['TestUpdateTaskPresenterImplementation.test_with_invalid_task_display_id json_response'] = 'task_display_id is invalid task_id send valid task_id'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_due_date_has_expired http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_due_date_has_expired res_status'] = 'DUE_DATE_TIME_HAS_EXPIRED'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_due_date_has_expired json_response'] = 'given due date time 2020-03-05 has expired, please give a valid due date time'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_start_date_is_ahead_of_due_date http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_start_date_is_ahead_of_due_date res_status'] = 'START_DATE_IS_AHEAD_OF_DUE_DATE'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_start_date_is_ahead_of_due_date json_response'] = 'given start date 2020-05-04 is ahead of given due date 2020-04-04 '

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_gof_ids http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_gof_ids res_status'] = 'INVALID_GOF_IDS'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_gof_ids json_response'] = "invalid gof ids: ['gof_1', 'gof_2']"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_field_ids http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_field_ids res_status'] = 'INVALID_FIELD_IDS'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_field_ids json_response'] = "invalid field ids: ['field_1', 'field_2']"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_gofs_given_to_a_task_template http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_gofs_given_to_a_task_template res_status'] = 'INVALID_GOFS_OF_TASK_TEMPLATE'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_gofs_given_to_a_task_template json_response'] = "invalid gofs ['gof_1', 'gof_2']  given to the task template template_1"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_duplicate_field_ids_to_a_gof http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_duplicate_field_ids_to_a_gof res_status'] = 'DUPLICATE_FIELD_IDS_GIVEN_TO_A_GOF'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_duplicate_field_ids_to_a_gof json_response'] = "gof id gof_1 has duplicate field ids ['field_1', 'field_2']"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_fields_given_to_a_gof http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_fields_given_to_a_gof res_status'] = 'INVALID_FIELDS_OF_GOF'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_fields_given_to_a_gof json_response'] = "invalid fields ['field_1', 'field_2']  given to the gof gof_1"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_task_id http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_task_id res_status'] = 'INVALID_TASK_ID'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_task_id json_response'] = 'invalid task id is: 1, please send valid task id'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_stage_id http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_stage_id res_status'] = 'INVALID_STAGE_ID'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_stage_id json_response'] = 'please give a valid stage id, 1 is invalid stage id'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_duplicate_same_gof_orders_for_a_gof http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_duplicate_same_gof_orders_for_a_gof res_status'] = 'DUPLICATE_SAME_GOF_ORDERS_FOR_A_GOF'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_duplicate_same_gof_orders_for_a_gof response'] = 'duplicate same gof orders given for gof gof_1, duplicates are [1, 2]'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_priority_is_required http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_priority_is_required res_status'] = 'PRIORITY_IS_REQUIRED'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_priority_is_required response'] = 'task priority is required if action type is not no validations'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_due_date_time_without_start_datetime http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_due_date_time_without_start_datetime res_status'] = 'DUE_DATE_TIME_WITHOUT_START_DATE_TIME'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_due_date_time_without_start_datetime response'] = 'due date time 2020-05-06 04:03:01 is given with out start datetime'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_start_date_time_is_required http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_start_date_time_is_required res_status'] = 'START_DATE_TIME_IS_REQUIRED'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_start_date_time_is_required response'] = 'start datetime is required if action type is not no validations'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_task_delay_reason_not_updated http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_task_delay_reason_not_updated res_status'] = 'TASK_DELAY_REASON_NOT_UPDATED'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_task_delay_reason_not_updated json_response'] = 'you are trying to update task due date to 2020-03-05 without updating the delay reason for task task_1 in stage stage_1'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_stage_permitted_gofs http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_stage_permitted_gofs res_status'] = 'INVALID_STAGE_PERMITTED_GOFS'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_stage_permitted_gofs response'] = "['gof_1', 'gof_2'] gof ids are not permitted for the stage 1"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_user_needs_gof_writable_permission http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_user_needs_gof_writable_permission res_status'] = 'USER_NEEDS_GOF_WRITABLE_PERMISSION'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_user_needs_gof_writable_permission response'] = "user needs write access on gof gof_1, because user does not have at least one role in ['role_1', 'role_2'] roles"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_user_needs_field_writable_permission http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_user_needs_field_writable_permission res_status'] = 'USER_NEEDS_FILED_WRITABLE_PERMISSION'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_user_needs_field_writable_permission response'] = "user needs write access on field field_1, because user does not have at least one role in ['role_1', 'role_2'] roles"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_empty_value_in_required_field http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_empty_value_in_required_field res_status'] = 'EMPTY_VALUE_FOR_REQUIRED_FIELD'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_empty_value_in_required_field response'] = 'Given Empty value for the required field of field_id: field_1! Required field should not be empty'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_phone_number_value http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_phone_number_value res_status'] = 'INVALID_PHONE_NUMBER_VALUE'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_phone_number_value response'] = 'Invalid value for phone number: 99987272 for field: field_1'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_email_address http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_email_address res_status'] = 'INVALID_EMAIL'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_email_address response'] = 'Invalid value for email: google@google.mail for field: field_1'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_url_address http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_url_address res_status'] = 'INVALID_URL'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_url_address response'] = 'Invalid value for url: http://google.mail for field: field_1'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_weak_password http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_weak_password res_status'] = 'NOT_A_STRONG_PASSWORD'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_weak_password response'] = 'Given a weak password: admin123 for field: field_1! Try with at least 6 characters including special characters'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_number_value http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_number_value res_status'] = 'INVALID_NUMBER_VALUE'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_number_value response'] = 'Invalid number: 98656 for field: field_1! Number should only consists digits'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_float_value http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_float_value res_status'] = 'INVALID_FLOAT_VALUE'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_float_value response'] = 'Invalid float value: 98656.0.0 for field: field_1!'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_dropdown_value http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_dropdown_value res_status'] = 'INVALID_VALUE_FOR_DROPDOWN'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_dropdown_value response'] = "Invalid dropdown value: city for field: field_1! Try with these dropdown values: ['Mr', 'Mrs']"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_name_in_gof_selector_field_value http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_name_in_gof_selector_field_value res_status'] = 'INCORRECT_NAME_IN_GOF_SELECTOR_FIELD'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_name_in_gof_selector_field_value response'] = "Invalid gof selector name: city for field: field_1! Try with these gof selector names: ['Mr', 'Mrs'] "

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_choice_in_radio_group_field http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_choice_in_radio_group_field res_status'] = 'INCORRECT_RADIO_GROUP_CHOICE'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_choice_in_radio_group_field response'] = "Invalid radio group choice: city for field: field_1! Try with these valid options: ['Mr', 'Mrs']"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_checkbox_group_options_selected http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_checkbox_group_options_selected res_status'] = 'INCORRECT_CHECK_BOX_OPTIONS_SELECTED'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_checkbox_group_options_selected response'] = "Invalid check box options selected: ['city', 'town'] for field: field_1! Try with these valid options: ['Mr', 'Mrs']"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_options_selected http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_options_selected res_status'] = 'INCORRECT_MULTI_SELECT_OPTIONS_SELECTED'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_options_selected response'] = "Invalid multi select options selected: ['city', 'town'] for field: field_1! Try with these valid options: ['Mr', 'Mrs']"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_labels_selected http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_labels_selected res_status'] = 'INCORRECT_MULTI_SELECT_LABELS_SELECTED'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_labels_selected response'] = "Invalid multi select labels selected: ['city', 'town'] for field: field_1! Try with these valid options: ['Mr', 'Mrs']"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_date_format http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_date_format res_status'] = 'INVALID_DATE_FORMAT'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_date_format response'] = 'given invalid format for date: 03-05-2020 for field: field_1! Try with this format: YYYY-MM-DD'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_time_format http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_time_format res_status'] = 'INVALID_TIME_FORMAT'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_time_format response'] = 'given invalid format for time: 55:04:03 for field: field_1! Try with this format: HH:MM:SS'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_image_url http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_image_url res_status'] = 'INVALID_IMAGE_URL'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_image_url response'] = 'Invalid url for an image: http://google.com for field: field_1!'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_not_acceptable_image_format http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_not_acceptable_image_format res_status'] = 'INVALID_IMAGE_FORMAT'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_not_acceptable_image_format response'] = "Invalid format for an image: .png for field: field_1! Try with these formats: ['.jpg', '.jpeg']"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_file_url http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_file_url res_status'] = 'INVALID_FILE_URL'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_file_url response'] = 'Invalid url for a file: http://google.com for field: field_1!'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_not_acceptable_file_format http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_not_acceptable_file_format res_status'] = 'INVALID_FILE_FORMAT'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_exception_for_not_acceptable_file_format response'] = "Invalid format for a file: .png for field: field_1! Try with these formats: ['.pdf', '.txt']"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_stage_ids_with_invalid_permission_for_assignee_exception http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_stage_ids_with_invalid_permission_for_assignee_exception res_status'] = 'STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_stage_ids_with_invalid_permission_for_assignee_exception json_response'] = 'Stage ids with invalid permission of assignees that you have sent are: [1, 2],please assign valid assignees for stages'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_stage_ids_list_empty http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_stage_ids_list_empty res_status'] = 'EMPTY_STAGE_IDS_ARE_INVALID'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_stage_ids_list_empty response'] = 'Stage Ids list should not be empty'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_stage_ids_list http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_stage_ids_list res_status'] = 'INVALID_STAGE_IDS'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_invalid_stage_ids_list response'] = "Invalid stage ids that you have sent are: ['stage_1', 'stage_2'],please send valid stage ids"

snapshots['TestUpdateTaskPresenterImplementation.test_raise_due_date_time_is_required http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_due_date_time_is_required res_status'] = 'DUE_DATE_TIME_IS_REQUIRED'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_due_date_time_is_required json_response'] = 'due datetime is required if action type is not no validations'

snapshots['TestUpdateTaskPresenterImplementation.test_get_update_task_response success_response'] = {
    'task_details': {
        'due_date': '2020-04-15 04:50:40',
        'priority': 'HIGH',
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
        'start_date': '2020-04-05 04:50:40',
        'task_id': 'iBWF-1',
        'task_overview_fields': [
        ],
        'title': 'title_0'
    }
}

snapshots['TestUpdateTaskPresenterImplementation.test_raise_user_did_not_fill_required_fields http_status_code'] = 400

snapshots['TestUpdateTaskPresenterImplementation.test_raise_user_did_not_fill_required_fields res_status'] = 'USER_DID_NOT_FILL_REQUIRED_FIELDS'

snapshots['TestUpdateTaskPresenterImplementation.test_raise_user_did_not_fill_required_fields response'] = "user did not fill required fields: ['field_display_name_0', 'field_display_name_1']"
