# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01ReplyToCommentAPITestCase.test_create_reply_to_comment_return_response status_code'] = '200'

snapshots['TestCase01ReplyToCommentAPITestCase.test_create_reply_to_comment_return_response body'] = {
    'author': {
        'name': 'name',
        'profile_pic_url': 'https://graph.ib_users.com/',
        'user_id': 'c8939223-79a0-4566-ba13-b4fbf7db6f93'
    },
    'comment_content': 'content',
    'comment_id': '01be920b-7b4c-49e7-8adb-41a0c18da848',
    'created_at': '2020-05-01 00:00:00',
    'is_editable': True,
    'mention_users': [
        {
            'name': 'name',
            'profile_pic_url': 'https://graph.ib_users.com/',
            'user_id': '10be920b-7b4c-49e7-8adb-41a0c18da848'
        },
        {
            'name': 'name',
            'profile_pic_url': 'https://graph.ib_users.com/',
            'user_id': '20be920b-7b4c-49e7-8adb-41a0c18da848'
        }
    ],
    'multimedia': [
        {
            'format_type': 'IMAGE',
            'multimedia_id': '97be920b-7b4c-49e7-8adb-41a0c18da848',
            'url': 'https://picsum.photos/200'
        },
        {
            'format_type': 'VIDEO',
            'multimedia_id': '92be920b-7b4c-49e7-8adb-41a0c18da848',
            'url': 'https://picsum.photos/200'
        }
    ]
}
