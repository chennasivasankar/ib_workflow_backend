# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02DeleteUserAPITestCase.test_with_invalid_admin_user_then_raise_exception status_code'] = '404'

snapshots['TestCase02DeleteUserAPITestCase.test_with_invalid_admin_user_then_raise_exception body'] = b'<h1>Not Found</h1><p>The requested resource was not found on this server.</p>'

snapshots['TestCase02DeleteUserAPITestCase.test_with_invalid_delete_user_and_delete_user_id_not_found_then_raise_exception status_code'] = '404'

snapshots['TestCase02DeleteUserAPITestCase.test_with_invalid_delete_user_and_delete_user_id_not_found_then_raise_exception body'] = b'<h1>Not Found</h1><p>The requested resource was not found on this server.</p>'

snapshots['TestCase02DeleteUserAPITestCase.test_with_invalid_delete_user_and_delete_user_id_is_admin_then_raise_exception status_code'] = '404'

snapshots['TestCase02DeleteUserAPITestCase.test_with_invalid_delete_user_and_delete_user_id_is_admin_then_raise_exception body'] = b'<h1>Not Found</h1><p>The requested resource was not found on this server.</p>'
