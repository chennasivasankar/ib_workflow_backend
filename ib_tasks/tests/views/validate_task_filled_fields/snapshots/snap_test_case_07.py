# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase07ValidateTaskFilledFieldsAPITestCase.test_case status_code'] = '400'

snapshots['TestCase07ValidateTaskFilledFieldsAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'USER_DID_NOT_FILL_REQUIRED_FIELDS',
    'response': "user did not fill required fields: ['payment requester name']"
}
