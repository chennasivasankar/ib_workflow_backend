# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UpdateCommentAPITestCase.test_with_invalid_user_ids status_code'] = '400'

snapshots['TestCase02UpdateCommentAPITestCase.test_with_invalid_user_ids body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_USER_IDS',
    'response': "Please send valid user ids to update comment, invalid user ids are [UUID('00be920b-7b4c-49e7-8adb-41a0c18da848'), UUID('20be920b-7b4c-49e7-8adb-41a0c18da848')]"
}
