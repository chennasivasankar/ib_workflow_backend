# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02SendUserResetPasswordLinkAPITestCase.test_case status_code'] = '404'

snapshots['TestCase02SendUserResetPasswordLinkAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'USER_ACCOUNT_DOES_NOT_EXIST',
    'response': 'user account does not exist. please send valid email'
}