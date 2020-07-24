# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetTaskPresenterImplementation.test_raise_exception_for_invalid_task_id exception_object'] = b'{"response": "invalid task id is: -1, please send valid task id", "http_status_code": 404, "res_status": "INVALID_TASK_ID"}'

snapshots['TestGetTaskPresenterImplementation.test_given_task_complete_details_dto_returns_task_details task_details = '] = b'{"task_id": "task0", "template_id": "template0", "gofs": [[{"field_id": "field0", "field_response": "response0"}], [{"field_id": "field2", "field_response": "response2"}, {"field_id": "field3", "field_response": "response3"}]]}'
