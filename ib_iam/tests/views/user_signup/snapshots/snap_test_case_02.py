# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

# snapshots['TestCase02UserSignupAPITestCase.test_with_active_email_then_raise_exception status_code'] = '400'
#
# snapshots['TestCase02UserSignupAPITestCase.test_with_active_email_then_raise_exception body'] = {
#     'http_status_code': 400,
#     'res_status': 'ACCOUNT_ALREADY_EXISTS',
#     'response': 'The given email has already account, try with another email'
# }

snapshots['TestCase02UserSignupAPITestCase.test_with_invalid_email status_code'] = '400'

snapshots['TestCase02UserSignupAPITestCase.test_with_invalid_email body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_EMAIL',
    'response': 'Please send valid email'
}

snapshots['TestCase02UserSignupAPITestCase.test_with_invalid_password status_code'] = '400'

snapshots['TestCase02UserSignupAPITestCase.test_with_invalid_password body'] = {
    'http_status_code': 400,
    'res_status': 'PASSWORD_DOES_NOT_MATCH_CRITERIA',
    'response': 'not a valid password, try with valid password'
}

snapshots['TestCase02UserSignupAPITestCase.test_with_invalid_email_domain status_code'] = '400'

snapshots['TestCase02UserSignupAPITestCase.test_with_invalid_email_domain body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_DOMAIN',
    'response': 'Currently, you can sign up to the portal only with iB Hubs and related companies email IDs'
}
