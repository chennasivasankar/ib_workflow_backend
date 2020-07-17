# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UserLoginAPITestCase.test_case_user_account_not_exist status_code'] = '404'

snapshots['TestCase02UserLoginAPITestCase.test_case_user_account_not_exist body'] = {
    'http_status_code': 404,
    'res_status': 'USER_ACCOUNT_DOES_NOT_EXIST',
    'response': 'user account does not exist. please send valid email'
}

snapshots['TestCase02UserLoginAPITestCase.test_case_incorrect_password status_code'] = '404'

snapshots['TestCase02UserLoginAPITestCase.test_case_incorrect_password body'] = {
    'http_status_code': 404,
    'res_status': 'INCORRECT_PASSWORD',
    'response': 'Please send valid password with you registered'
}

snapshots['TestCase02UserLoginAPITestCase.test_case_for_invalid_email status_code'] = '400'

snapshots['TestCase02UserLoginAPITestCase.test_case_for_invalid_email body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_EMAIL',
    'response': 'Please send valid email'
}
