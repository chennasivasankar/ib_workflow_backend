# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_token_doed_not_exist status_code'] = '200'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_token_doed_not_exist body'] = b''

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_token_has_expired status_code'] = '200'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_token_has_expired body'] = b''

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_with_weak_password status_code'] = '200'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_with_weak_password body'] = b''
