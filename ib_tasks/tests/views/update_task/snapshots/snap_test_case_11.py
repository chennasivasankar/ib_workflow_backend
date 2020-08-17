# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase01UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'USER_NEEDS_GOF_WRITABLE_PERMISSION',
    'response': "user b913daae-e562-4267-bf38-c8d0b5df6d6f needs write "
                "access on gof GOF-1, because user does not have ["
                "'FIN_GOF_CREATOR'] roles"
}
