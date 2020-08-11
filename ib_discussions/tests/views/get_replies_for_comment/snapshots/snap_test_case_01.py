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
                'name': 'name',
                'profile_pic_url': 'https://graph.ib_users.com/',
                'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848'
            },
            'comment_content': 'content',
            'comment_id': '19be920b-7b4c-49e7-8adb-41a0c18da848',
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
            'multimedia': [
                {
                    'format_type': 'IMAGE',
                    'multimedia_id': '97be920b-7b4c-49e7-8adb-41a0c18da848',
                    'thumbnail_url': 'https://picsum.photos/200',
                    'url': 'https://picsum.photos/200'
                },
                {
                    'format_type': 'VIDEO',
                    'multimedia_id': '92be920b-7b4c-49e7-8adb-41a0c18da848',
                    'thumbnail_url': 'https://picsum.photos/200',
                    'url': 'https://picsum.photos/200'
                }
            ]
        },
        {
            'author': {
                'name': 'name',
                'profile_pic_url': 'https://graph.ib_users.com/',
                'user_id': '77be920b-7b4c-49e7-8adb-41a0c18da848'
            },
            'comment_content': 'content',
            'comment_id': '12be920b-7b4c-49e7-8adb-41a0c18da848',
            'created_at': '2020-05-01 00:00:00',
            'is_editable': False,
            'mention_users': [
                {
                    'name': 'name',
                    'profile_pic_url': 'https://graph.ib_users.com/',
                    'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848'
                }
            ],
            'multimedia': [
                {
                    'format_type': 'VIDEO',
                    'multimedia_id': '92be920b-7b4c-49e7-8adb-41a0c18da848',
                    'thumbnail_url': 'https://picsum.photos/200',
                    'url': 'https://picsum.photos/200'
                }
            ]
        }
    ]
}
