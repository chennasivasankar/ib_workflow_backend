# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetRepliesForCommentPresenterImplementation.test_prepare_response_for_reply get replies'] = {
    'replies': [
        {
            'author': {
                'name': 'name',
                'profile_pic_url': 'https://graph.ib_users.com/',
                'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848'
            },
            'comment_content': 'content',
            'comment_id': '91be920b-7b4c-49e7-8adb-41a0c18da848',
            'created_at': '2008-01-01 00:00:00',
            'is_editable': True
        },
        {
            'author': {
                'name': 'name',
                'profile_pic_url': 'https://graph.ib_users.com/',
                'user_id': '41be920b-7b4c-49e7-8adb-41a0c18da848'
            },
            'comment_content': 'content',
            'comment_id': '00be920b-7b4c-49e7-8adb-41a0c18da848',
            'created_at': '2008-01-01 00:00:00',
            'is_editable': False
        }
    ]
}
