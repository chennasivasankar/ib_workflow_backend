# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestUpdateCommentPresenterImplementation.test_prepare_response_for_update_comment update_comment'] = {
    'author': {
        'name': 'name',
        'profile_pic_url': 'https://graph.ib_users.com/',
        'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    'comment_content': 'content',
    'comment_id': '91be920b-7b4c-49e7-8adb-41a0c18da848',
    'created_at': '2008-01-01 00:00:00',
    'is_editable': True,
    'mention_users': [
        {
            'name': 'name',
            'profile_pic_url': 'https://graph.ib_users.com/',
            'user_id': '01be920b-7b4c-49e7-8adb-41a0c18da848'
        },
        {
            'name': 'name',
            'profile_pic_url': 'https://graph.ib_users.com/',
            'user_id': '91be920b-7b4c-49e7-8adb-41a0c18da848'
        }
    ],
    'multimedia': [
        {
            'format_type': 'IMAGE',
            'multimedia_id': 'f26c1802-d996-4e89-9644-23ebaf02713a',
            'thumbnail_url': 'https://picsum.photos/200',
            'url': 'https://picsum.photos/200'
        },
        {
            'format_type': 'VIDEO',
            'multimedia_id': 'a5f52868-8065-403c-abe5-24c09e42bafe',
            'thumbnail_url': 'https://picsum.photos/200',
            'url': 'https://picsum.photos/200'
        }
    ],
    'total_replies_count': 0
}
