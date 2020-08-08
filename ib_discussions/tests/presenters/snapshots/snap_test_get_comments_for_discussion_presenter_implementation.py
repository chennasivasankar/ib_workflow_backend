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
                'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848'
            },
            'comment_content': 'content',
            'comment_id': '11be920b-7b4c-49e7-8adb-41a0c18da848',
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
                    'multi_media_id': 'f26c1802-d996-4e89-9644-23ebaf02713a',
                    'url': 'https://picsum.photos/200'
                },
                {
                    'format_type': 'VIDEO',
                    'multi_media_id': 'a5f52868-8065-403c-abe5-24c09e42bafe',
                    'url': 'https://picsum.photos/200'
                }
            ],
            'total_replies_count': 0
        },
        {
            'author': {
                'name': 'name ',
                'profile_pic_url': 'https://graph.ib_users.com/',
                'user_id': '91be920b-7b4c-49e7-8adb-41a0c18da848'
            },
            'comment_content': 'content',
            'comment_id': '12be920b-7b4c-49e7-8adb-41a0c18da848',
            'created_at': '2008-01-01 00:00:00',
            'is_editable': False,
            'mention_users': [
            ],
            'multi_media': [
            ],
            'total_replies_count': 2
        }
    ]
}
