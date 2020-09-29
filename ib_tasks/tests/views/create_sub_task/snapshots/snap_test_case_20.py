# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase20CreateSubTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase20CreateSubTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'USER_NEEDS_FILED_WRITABLE_PERMISSION',
    'response': 'user needs write access on field DISPLAY_NAME-0, because user does not have at least one role in [] roles'
}
