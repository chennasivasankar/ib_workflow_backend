# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02SendVerifyEmailLinkAPITestCase.test_case_invalid_email_then_raise_account_not_found_exception status_code'] = '404'

snapshots['TestCase02SendVerifyEmailLinkAPITestCase.test_case_invalid_email_then_raise_account_not_found_exception body'] = {
    'http_status_code': 404,
    'res_status': 'ACCOUNT_DOES_NOT_EXISTS',
    'response': "account doesn't exist with the given email id"
}

snapshots['TestCase02SendVerifyEmailLinkAPITestCase.test_case_already_active_email_and_email_verified_then_raise_account_is_already_verifys_exception status_code'] = '400'

snapshots['TestCase02SendVerifyEmailLinkAPITestCase.test_case_already_active_email_and_email_verified_then_raise_account_is_already_verifys_exception body'] = {
    'http_status_code': 400,
    'res_status': 'EMAIL_ALREADY_VERIFIED',
    'response': 'The given email is already verified, now you can login'
}
