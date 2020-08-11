# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03UpdateTaskAPITestCase.test_case status_code'] = '500'

snapshots['TestCase03UpdateTaskAPITestCase.test_case body'] = {
    'res_status': [
        '"START_DATE_IS_AHEAD_OF_DUE_DATE" is not a valid choice.'
    ]
}
