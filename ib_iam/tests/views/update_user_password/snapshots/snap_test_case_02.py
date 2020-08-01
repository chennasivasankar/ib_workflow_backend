# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_token_has_expired status_code'] = '404'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_token_has_expired body'] = b'<h1>Not Found</h1><p>The requested resource was not found on this server.</p>'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_token_does_not_exist status_code'] = '404'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_token_does_not_exist body'] = b'<h1>Not Found</h1><p>The requested resource was not found on this server.</p>'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_case_for_required_password_min_length status_code'] = '404'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_case_for_required_password_min_length body'] = b'<h1>Not Found</h1><p>The requested resource was not found on this server.</p>'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_case_for_required_password_one_special_character status_code'] = '404'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_case_for_required_password_one_special_character body'] = b'<h1>Not Found</h1><p>The requested resource was not found on this server.</p>'
