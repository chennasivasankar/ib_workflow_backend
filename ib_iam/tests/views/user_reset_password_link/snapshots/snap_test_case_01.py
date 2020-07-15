# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UserResetPasswordLinkAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01UserResetPasswordLinkAPITestCase.test_case body'] = {
    'email': [
        'This field may not be blank.'
    ]
}
