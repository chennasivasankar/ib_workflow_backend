# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase08ValidateTaskFilledFieldsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase08ValidateTaskFilledFieldsAPITestCase.test_case body'] = {
    'http_status_code': 200,
    'res_status': 'TASK_FIELDS_VALIDATED_SUCCESSFULLY',
    'response': 'all task required fields are filled'
}
