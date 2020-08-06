# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01ReplyToCommentAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01ReplyToCommentAPITestCase.test_case body'] = {
    'author': {
        'name': 'string',
        'profile_pic_url': 'string',
        'user_id': '49a9f26b-93e7-4636-8cd1-39b606dc56da'
    },
    'comment_content': 'string',
    'comment_id': 1,
    'created_at': '2099-12-31 00:00:00',
    'is_editable': True
}
