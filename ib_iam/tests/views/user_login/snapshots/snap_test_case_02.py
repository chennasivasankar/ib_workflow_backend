# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

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

snapshots['TestCase02UserLoginAPITestCase.test_case_email_is_not_verify_then_raise_email_not_verify status_code'] = '400'

snapshots['TestCase02UserLoginAPITestCase.test_case_email_is_not_verify_then_raise_email_not_verify body'] = {
    'http_status_code': 400,
    'res_status': 'EMAIL_IS_NOT_VERIFY',
    'response': 'Given Email not verify, Please first verify the email'
}

snapshots['TestCase02UserLoginAPITestCase.test_with_not_register_email_then_raise_account_not_found_exception status_code'] = '404'

snapshots['TestCase02UserLoginAPITestCase.test_with_not_register_email_then_raise_account_not_found_exception body'] = {
    'http_status_code': 404,
    'res_status': 'USER_ACCOUNT_DOES_NOT_EXIST',
    'response': 'user account does not exist. please send valid email'
}
