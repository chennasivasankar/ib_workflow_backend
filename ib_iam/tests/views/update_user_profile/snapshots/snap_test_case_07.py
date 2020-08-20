# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateUserProfileAPITestCase.test_duplicate_role_ids status_code'] = '400'

snapshots['TestCase01UpdateUserProfileAPITestCase.test_duplicate_role_ids body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_ROLE_IDS',
    'response': "can't create roles with duplicate role_ids"
}

snapshots['TestCase01UpdateUserProfileAPITestCase.test_invalid_role_ids status_code'] = '404'

snapshots['TestCase01UpdateUserProfileAPITestCase.test_invalid_role_ids body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_ROLE_IDS',
    'response': 'given role ids are invalid'
}
