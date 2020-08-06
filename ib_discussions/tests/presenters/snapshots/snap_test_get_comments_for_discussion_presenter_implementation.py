# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetCommentsForDiscussionPresenterImplementation.test_response_for_comments_with_users_dtos get_comments_for_discussion'] = {
    'comments': [
        {
            'author': {
                'name': 'name ',
                'profile_pic_url': 'https://graph.ib_users.com/',
                'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848'
            },
            'comment_content': 'content',
            'comment_id': '91be920b-7b4c-49e7-8adb-41a0c18da848',
            'created_at': '2008-01-01 00:00:00',
            'is_editable': True,
            'replies_count': 0
        },
        {
            'author': {
                'name': 'name ',
                'profile_pic_url': 'https://graph.ib_users.com/',
                'user_id': '41be920b-7b4c-49e7-8adb-41a0c18da848'
            },
            'comment_content': 'content',
            'comment_id': '11be920b-7b4c-49e7-8adb-41a0c18da848',
            'created_at': '2008-01-01 00:00:00',
            'is_editable': False,
            'replies_count': 2
        }
    ]
}
