# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase01EditUserAPITestCase.test_given_user_not_admin_returns_user_does_not_have_permission_response status_code'] = '403'

snapshots['TestCase01EditUserAPITestCase.test_given_user_not_admin_returns_user_does_not_have_permission_response body'] = {
    'http_status_code': 403,
    'res_status': 'USER_DOES_NOT_HAVE_PERMISSION',
    'response': 'forbidden access, user cannot access'
}
