# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUsersAPITestCase.test_case status_code'] = '500'

snapshots['TestCase01GetUsersAPITestCase.test_case body'] = {
    'response': [
        '"forbidden access, user cannot access" is not a valid choice.'
    ]
}
