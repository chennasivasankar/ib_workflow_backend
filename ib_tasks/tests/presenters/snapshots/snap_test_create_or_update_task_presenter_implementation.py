# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_duplicate_field_ids response_object'] = b'{"response": "duplicate field ids: [\'FIELD_ID-1\', \'FIELD_ID-2\']", "http_status_code": 400, "res_status": "DUPLICATE_FIELD_IDS"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_task_template_id response_object'] = b'{"response": "duplicate task template ids: [\'TASK_TEMPLATE_ID-0\']", "http_status_code": 400, "res_status": "INVALID_TASK_TEMPLATE_IDS"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_gof_ids response_object'] = b'{"response": "invalid gof ids: [\'GOF_ID-0\', \'GOF_ID-1\']", "http_status_code": 400, "res_status": "INVALID_GOF_IDS"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_field_ids response_object'] = b'{"response": "invalid field ids: [\'FIELD_ID-1\', \'FIELD_ID-2\']", "http_status_code": 400, "res_status": "INVALID_FIELD_IDS"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_empty_value_in_plain_text_field response_object'] = b'{"response": "got empty value in plain text field for field id: FIELD_ID-1", "http_status_code": 400, "res_status": "EMPTY_VALUE_FOR_PLAIN_TEXT_FIELD"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_phone_number_value response_object'] = b'{"response": "Invalid value for phone number: 73247832 for field: FIELD_ID-1", "http_status_code": 400, "res_status": "INVALID_PHONE_NUMBER_VALUE"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_email_address response_object'] = b'{"response": "Invalid value for email: ibhubs@gmail.com for field: FIELD_ID-1", "http_status_code": 400, "res_status": "INVALID_EMAIL"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_url_address response_object'] = b'{"response": "Invalid value for url: https://eiiuwe.com for field: FIELD_ID-1", "http_status_code": 400, "res_status": "INVALID_URL"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_weak_password response_object'] = b'{"response": "Given a weak password: admin123 for field: FIELD_ID-1! Try with atleast 8 characters including special characters", "http_status_code": 400, "res_status": "NOT_A_STRONG_PASSWORD"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_number_value response_object'] = b'{"response": "Invalid number: 123a for field: FIELD_ID-1! Number should only consists digits", "http_status_code": 400, "res_status": "INVALID_NUMBER_VALUE"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_float_value response_object'] = b'{"response": "Invalid float value: 123a.0 for field: FIELD_ID-1!", "http_status_code": 400, "res_status": "INVALID_FLOAT_VALUE"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_dropdown_value response_object'] = b'{"response": "Invalid dropdown value: 32684902319 for field: FIELD_ID-1! Try with these dropdown values: [\'DROPDOWN_1\', \'DROPDOWN_2\']", "http_status_code": 400, "res_status": "INVALID_VALUE_FOR_DROPDOWN"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_choice_in_radio_group_field response_object'] = b'{"response": "Invalid radio group choice: 32684902319 for field: FIELD_ID-1! Try with these valid options: [\'RADIO_1\', \'RADIO_2\']", "http_status_code": 400, "res_status": "INCORRECT_RADIO_GROUP_CHOICE"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_checkbox_group_options_selected response_object'] = b'{"response": "Invalid check box options selected: [\'CHECK_BOX_3\', \'CHECK_BOX_4\'] for field: FIELD_ID-1! Try with these valid options: [\'CHECK_BOX_1\', \'CHECK_BOX_2\']", "http_status_code": 400, "res_status": "INCORRECT_CHECK_BOX_OPTIONS_SELECTED"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_options_selected response_object'] = b'{"response": "Invalid multi select options selected: [\'MULTI_SELECT_3\', \'MULTI_SELECT_4\'] for field: FIELD_ID-1! Try with these valid options: [\'MULTI_SELECT_1\', \'MULTI_SELECT_2\']", "http_status_code": 400, "res_status": "INCORRECT_MULTI_SELECT_OPTIONS_SELECTED"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_multi_select_labels_selected response_object'] = b'{"response": "Invalid multi select labels selected: [\'MULTI_SELECT_LABEL_3\', \'MULTI_SELECT_LABEL_4\'] for field: FIELD_ID-1! Try with these valid options: [\'MULTI_SELECT_LABEL_1\', \'MULTI_SELECT_LABEL_2\']", "http_status_code": 400, "res_status": "INCORRECT_MULTI_SELECT_LABELS_SELECTED"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_date_format response_object'] = b'{"response": "given invalid format for date: 02-04-2002 for field: FIELD_ID-1! Try with this format: YYYY/MM/DD", "http_status_code": 400, "res_status": "INVALID_DATE_FORMAT"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_time_format response_object'] = b'{"response": "given invalid format for time: 04/50 for field: FIELD_ID-1! Try with this format: HH:SS", "http_status_code": 400, "res_status": "INVALID_TIME_FORMAT"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_not_acceptable_image_format response_object'] = b'{"response": "Invalid format for an image: ib_hubs.pdf for field: FIELD_ID-1! Try with these formats: [\'jpeg\', \'jpg\', \'png\']", "http_status_code": 400, "res_status": "INVALID_IMAGE_FORMAT"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_image_url response_object'] = b'{"response": "Invalid url for an image: https://google.com/ib.pdf for field: FIELD_ID-1!", "http_status_code": 400, "res_status": "INVALID_IMAGE_URL"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_invalid_file_url response_object'] = b'{"response": "Invalid url for a file: https://google.com/ib.pdf for field: FIELD_ID-1!", "http_status_code": 400, "res_status": "INVALID_FILE_URL"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_gof_ids_in_gof_selector_field_value response_object'] = b'{"response": "Invalid gof selector name: [\'gof_1\', \'gof_2\'] in gof_selector_field!", "http_status_code": 400, "res_status": "INVALID_NAME_IN_GOF_SELECTOR_FIELD"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_not_acceptable_file_format response_object'] = b'{"response": "Invalid format for a file: .mp4 for field: FIELD_1! Try with these formats: [\'pdf\']", "http_status_code": 400, "res_status": "INVALID_FILE_FORMAT"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exception_for_empty_value_in_required_field response_object'] = b'{"response": "Given Empty value for the required field of field_id: FIELD_1! Required field should not be empty", "http_status_code": 400, "res_status": "EMPTY_VALUE_FOR_REQUIRED_FIELD"}'

snapshots['TestCreateOrUpdateTaskPresenterImplementation.test_raise_exceptions_for_invalid_gof_id_selected_in_gof_selector response_object'] = b'{"response": "Invalid gof_id: 32684902319 for field: FIELD_ID-1! Try with these gof_id values: [\'industry\', \'individual\']", "http_status_code": 400, "res_status": "INCORRECT_GOF_ID_IN_GOF_SELECTOR_FIELD"}'
