# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UserLoginAPITestCase.test_case_user_account_not_exist status_code'] = '404'

snapshots['TestCase02UserLoginAPITestCase.test_case_user_account_not_exist body'] = b'<h1>Not Found</h1><p>The requested resource was not found on this server.</p>'

snapshots['TestCase02UserLoginAPITestCase.test_case_incorrect_password status_code'] = '404'

snapshots['TestCase02UserLoginAPITestCase.test_case_incorrect_password body'] = b'<h1>Not Found</h1><p>The requested resource was not found on this server.</p>'

snapshots['TestCase02UserLoginAPITestCase.test_case_for_invalid_email status_code'] = '404'

snapshots['TestCase02UserLoginAPITestCase.test_case_for_invalid_email body'] = b'<h1>Not Found</h1><p>The requested resource was not found on this server.</p>'
