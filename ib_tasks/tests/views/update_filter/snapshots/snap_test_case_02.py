# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UpdateFilterAPITestCase.test_case status_code'] = '500'

snapshots['TestCase02UpdateFilterAPITestCase.test_case body'] = {
    'res_status': [
        '"INVALID_FILTER_ID" is not a valid choice.'
    ]
}
