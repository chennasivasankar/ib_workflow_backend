# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UserLoginAPITestCase.test_case status_code'] = '500'

snapshots['TestCase02UserLoginAPITestCase.test_case body'] = {
    'res_status': [
        '"INVALID_EMAIL" is not a valid choice.'
    ]
}
