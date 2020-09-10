# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01DeleteFilterAPITestCase.test_case status_code'] = '403'

snapshots['TestCase01DeleteFilterAPITestCase.test_case body'] = {
    'http_status_code': 403,
    'res_status': 'USER_NOT_HAVE_PERMISSIONS_TO_DELETE',
    'response': 'user not have access to delete the filter'
}
