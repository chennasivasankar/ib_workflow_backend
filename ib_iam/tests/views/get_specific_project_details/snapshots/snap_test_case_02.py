# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()


snapshots['TestCase02GetSpecificProjectDetailsAPITestCase.test_with_invalid_project_id_return_response status_code'] = '400'

snapshots['TestCase02GetSpecificProjectDetailsAPITestCase.test_with_invalid_project_id_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_PROJECT_ID',
    'response': 'Please send valid project id'
}
