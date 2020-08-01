# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_token_has_expired status_code'] = '400'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_token_has_expired body'] = {
    'http_status_code': 400,
    'res_status': 'TOKEN_HAS_EXPIRED',
    'response': 'Please send valid token which is not expired'
}

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_token_does_not_exist status_code'] = '404'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_token_does_not_exist body'] = {
    'http_status_code': 404,
    'res_status': 'TOKEN_DOES_NOT_EXIST',
    'response': 'Please send valid token'
}

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_case_for_required_password_min_length status_code'] = '400'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_case_for_required_password_min_length body'] = {
    'http_status_code': 400,
    'res_status': 'PASSWORD_MIN_LENGTH',
    'response': 'Please send the password with minimum required length is 8'
}

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_case_for_required_password_one_special_character status_code'] = '400'

snapshots['TestCase02UpdateUserPasswordAPITestCase.test_case_for_required_password_one_special_character body'] = {
    'http_status_code': 400,
    'res_status': 'PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER',
    'response': 'Please send the password at least with one special character'
}
