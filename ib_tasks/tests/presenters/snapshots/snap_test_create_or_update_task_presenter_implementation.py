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
