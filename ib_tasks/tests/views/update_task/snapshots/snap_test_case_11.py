# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'USER_NEEDS_GOF_WRITABLE_PERMISSION',
    'response': "user d90ef535-fcc4-4e2b-9ea3-99ab0a8b3e87 needs write access on gof GOF-1, because user does not have ['FIN_GOF_CREATOR'] roles"
}