# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02VerifyEmailAPITestCase.test_with_already_verified_email_then_raise_exception status_code'] = '400'

snapshots['TestCase02VerifyEmailAPITestCase.test_with_already_verified_email_then_raise_exception body'] = {
    'http_status_code': 400,
    'res_status': 'EMAIL_ALREADY_VERIFIED',
    'response': 'The given email is already verified, now you can login'
}
