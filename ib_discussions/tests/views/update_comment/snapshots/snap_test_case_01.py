# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateCommentAPITestCase.test_with_valid_details_update_comment status_code'] = '200'

snapshots['TestCase01UpdateCommentAPITestCase.test_with_valid_details_update_comment body'] = {
    'author': {
        'name': 'name',
        'profile_pic_url': 'https://graph.ib_users.com/',
        'user_id': '31be920b-7b4c-49e7-8adb-41a0c18da848'
    },
    'comment_content': 'Hai, How are you?',
    'comment_id': '91be920b-7b4c-49e7-8adb-41a0c18da848',
    'created_at': '2008-01-01 00:00:00',
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
            'thumbnail_url': 'https://picsum.photos/200',
            'url': 'https://picsum.photos/200'
        },
        {
            'format_type': 'VIDEO',
            'multimedia_id': '92be920b-7b4c-49e7-8adb-41a0c18da848',
            'thumbnail_url': 'https://picsum.photos/200',
            'url': 'https://picsum.photos/200'
        }
    ],
    'total_replies_count': 0
}
