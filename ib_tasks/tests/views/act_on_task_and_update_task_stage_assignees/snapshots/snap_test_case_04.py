# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case status_code'] = '404'

snapshots['TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_BOARD_ID',
    'response': 'invalid board id is: board_1, please send valid board id'
}