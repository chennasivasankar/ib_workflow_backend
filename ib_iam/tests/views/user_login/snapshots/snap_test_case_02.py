# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UserLoginAPITestCase.test_case_user_account_not_exist status_code'] = '404'

snapshots['TestCase02UserLoginAPITestCase.test_case_user_account_not_exist body'] = {
    'http_status_code': 404,
    'res_status': 'USER_ACCOUNT_DOES_NOT_EXIST',
    'response': 'Please send valid email which is already exist'
}

snapshots['TestCase02UserLoginAPITestCase.test_case_for_invalid_email status_code'] = '400'

snapshots['TestCase02UserLoginAPITestCase.test_case_for_invalid_email body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_EMAIL',
    'response': 'Please send valid email'
}

snapshots['TestCase02UserLoginAPITestCase.test_case_for_required_password_min_length status_code'] = '400'

snapshots['TestCase02UserLoginAPITestCase.test_case_for_required_password_min_length body'] = {
    'http_status_code': 400,
    'res_status': 'PASSWORD_MIN_LENGTH',
    'response': 'Please send the password with minimum required length is 8'
}

snapshots['TestCase02UserLoginAPITestCase.test_case_incorrect_password status_code'] = '404'

snapshots['TestCase02UserLoginAPITestCase.test_case_incorrect_password body'] = {
    'http_status_code': 404,
    'res_status': 'INCORRECT_PASSWORD',
    'response': 'Please send valid password with you registered'
}

snapshots['TestCase02UserLoginAPITestCase.test_case_for_required_password_one_special_character status_code'] = '400'

snapshots['TestCase02UserLoginAPITestCase.test_case_for_required_password_one_special_character body'] = {
    'http_status_code': 400,
    'res_status': 'PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER',
    'response': 'Please send the password at least with one special character'
}
