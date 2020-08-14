# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UpdateFilterAPITestCase.test_case status_code'] = '403'

snapshots['TestCase02UpdateFilterAPITestCase.test_case body'] = {
    'http_status_code': 403,
    'res_status': 'USER_NOT_HAVE_PERMISSIONS_TO_UPDATE',
    'response': 'user not have access to update the filter'
}
