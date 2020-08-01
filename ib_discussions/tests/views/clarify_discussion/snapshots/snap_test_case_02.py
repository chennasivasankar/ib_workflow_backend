# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02ClarifyDiscussionAPITestCase.test_discussion_id_not_found status_code'] = '404'

snapshots['TestCase02ClarifyDiscussionAPITestCase.test_discussion_id_not_found body'] = {
    'http_status_code': 404,
    'res_status': 'DISCUSSION_ID_NOT_FOUND',
    'response': 'Please send valid discussion id'
}

snapshots['TestCase02ClarifyDiscussionAPITestCase.test_user_cannot_mark_discussion status_code'] = '400'

snapshots['TestCase02ClarifyDiscussionAPITestCase.test_user_cannot_mark_discussion body'] = {
    'http_status_code': 400,
    'res_status': 'USER_CANNOT_MARK_AS_CLARIFIED',
    'response': 'Please send access with valid user id'
}
