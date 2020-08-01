# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02DeleteUserAPITestCase.test_with_invalid_admin_user_then_raise_exception status_code'] = '403'

snapshots['TestCase02DeleteUserAPITestCase.test_with_invalid_admin_user_then_raise_exception body'] = {
    'http_status_code': 403,
    'res_status': 'USER_DOES_NOT_HAVE_PERMISSION',
    'response': 'forbidden access, user cannot access'
}

snapshots['TestCase02DeleteUserAPITestCase.test_with_invalid_delete_user_and_delete_user_id_not_found_then_raise_exception status_code'] = '404'

snapshots['TestCase02DeleteUserAPITestCase.test_with_invalid_delete_user_and_delete_user_id_not_found_then_raise_exception body'] = {
    'http_status_code': 404,
    'res_status': 'USER_DOES_NOT_EXIST',
    'response': 'user is not exist'
}

snapshots['TestCase02DeleteUserAPITestCase.test_with_invalid_delete_user_and_delete_user_id_is_admin_then_raise_exception status_code'] = '403'

snapshots['TestCase02DeleteUserAPITestCase.test_with_invalid_delete_user_and_delete_user_id_is_admin_then_raise_exception body'] = {
    'http_status_code': 403,
    'res_status': 'USER_DOES_NOT_HAVE_DELETE_PERMISSION',
    'response': 'User does not have delete permission'
}
