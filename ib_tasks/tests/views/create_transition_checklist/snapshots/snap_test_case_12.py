# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase12CreateTransitionChecklistAPITestCase.test_case status_code'] = '400'

snapshots['TestCase12CreateTransitionChecklistAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'USER_NEEDS_GOF_WRITABLE_PERMISSION',
    'response': "user needs write access on gof gof_1, because user does not have at least one role in ['FIN_EXAMPLE_ROLE'] roles"
}