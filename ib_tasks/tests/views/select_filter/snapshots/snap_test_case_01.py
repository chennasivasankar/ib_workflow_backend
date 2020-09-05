# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01SelectFilterAPITestCase.test_case status_code'] = '500'

snapshots['TestCase01SelectFilterAPITestCase.test_case body'] = {
    'res_status': [
        '"USER_DO_NOT_ACCESS_TO_UPDATE_FILTER_STATUS" is not a valid choice.'
    ]
}
