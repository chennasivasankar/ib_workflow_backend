# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetRepliesForCommentAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetRepliesForCommentAPITestCase.test_case body'] = {
    'replies': [
        {
            'author': {
                'name': 'string',
                'profile_pic_url': 'string',
                'user_id': '063cf768-a69f-4eb3-a68d-941a4b6d2984'
            },
            'comment_content': 'string',
            'comment_id': 1,
            'created_at': '2099-12-31 00:00:00',
            'is_editable': True
        }
    ]
}
