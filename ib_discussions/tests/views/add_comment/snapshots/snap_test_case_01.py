# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AddCommentAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01AddCommentAPITestCase.test_case body'] = {
    'author': {
        'name': 'name',
        'profile_pic_url': 'https://graph.ib_users.com/',
        'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    'comment_content': 'content',
    'comment_id': '91be920b-7b4c-49e7-8adb-41a0c18da848',
    'created_at': '2008-01-01 00:00:00',
    'is_editable': False,
    'total_replies_count': 0
}
