# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetCommentsForDiscussionAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetCommentsForDiscussionAPITestCase.test_case body'] = {
    'comments': [
        {
            'author': {
                'name': 'name',
                'profile_pic_url': 'https://graph.ib_users.com/',
                'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848'
            },
            'comment_content': 'content',
            'comment_id': '91be920b-7b4c-49e7-8adb-41a0c18da848',
            'created_at': '2008-01-01 00:00:00',
            'is_editable': False,
            'mention_users': [
                {
                    'name': 'name',
                    'profile_pic_url': 'https://graph.ib_users.com/',
                    'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848'
                },
                {
                    'name': 'name',
                    'profile_pic_url': 'https://graph.ib_users.com/',
                    'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848'
                }
            ],
            'multi_media': [
                {
                    'format_type': 'IMAGE',
                    'multi_media_id': '97be920b-7b4c-49e7-8adb-41a0c18da848',
                    'url': 'https://picsum.photos/200'
                },
                {
                    'format_type': 'VIDEO',
                    'multi_media_id': '92be920b-7b4c-49e7-8adb-41a0c18da848',
                    'url': 'https://picsum.photos/200'
                }
            ],
            'total_replies_count': 0
        },
        {
            'author': {
                'name': 'name',
                'profile_pic_url': 'https://graph.ib_users.com/',
                'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848'
            },
            'comment_content': 'content',
            'comment_id': '11be920b-7b4c-49e7-8adb-41a0c18da848',
            'created_at': '2020-05-01 00:00:00',
            'is_editable': False,
            'mention_users': [
                {
                    'name': 'name',
                    'profile_pic_url': 'https://graph.ib_users.com/',
                    'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848'
                }
            ],
            'multi_media': [
                {
                    'format_type': 'VIDEO',
                    'multi_media_id': '92be920b-7b4c-49e7-8adb-41a0c18da848',
                    'url': 'https://picsum.photos/200'
                }
            ],
            'total_replies_count': 0
        },
        {
            'author': {
                'name': 'name',
                'profile_pic_url': 'https://graph.ib_users.com/',
                'user_id': '77be920b-7b4c-49e7-8adb-41a0c18da848'
            },
            'comment_content': 'content',
            'comment_id': '21be920b-7b4c-49e7-8adb-41a0c18da848',
            'created_at': '2020-01-20 00:00:00',
            'is_editable': False,
            'mention_users': [
            ],
            'multi_media': [
            ],
            'total_replies_count': 0
        }
    ]
}
