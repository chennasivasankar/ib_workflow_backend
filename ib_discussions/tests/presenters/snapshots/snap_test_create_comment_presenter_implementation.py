# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCreateCommentPresenterImplementation.test_prepare_response_for_create_comment create_comment'] = {
    'author': {
        'name': 'name ',
        'profile_pic_url': 'https://graph.ib_users.com/',
        'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    'comment_content': 'content',
    'comment_id': '91be920b-7b4c-49e7-8adb-41a0c18da848',
    'created_at': '2008-01-01 00:00:00',
    'is_editable': True,
    'mention_users': [
        {
            'name': 'name ',
            'profile_pic_url': 'https://graph.ib_users.com/',
            'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848'
        },
        {
            'name': 'name ',
            'profile_pic_url': 'https://graph.ib_users.com/',
            'user_id': '91be920b-7b4c-49e7-8adb-41a0c18da848'
        }
    ],
    'multi_media': [
        {
            'format_type': 'IMAGE',
            'url': 'https://picsum.photos/200'
        },
        {
            'format_type': 'VIDEO',
            'url': 'https://picsum.photos/200'
        }
    ],
    'total_replies_count': 0
}
