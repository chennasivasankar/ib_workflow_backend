# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase05GetTaskRpsInGivenStageAPITestCase.test_case status_code'] = '404'

snapshots['TestCase05GetTaskRpsInGivenStageAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'DUE_DATE_IS_NOT_ADDED_TO_TASK',
    'response': 'please add due date to task'
}
