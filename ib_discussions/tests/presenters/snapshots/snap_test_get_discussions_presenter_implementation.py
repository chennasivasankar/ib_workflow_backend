# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetDiscussionsPresenterImplementation.test_prepare_response_for_discussions_details_dto discussion details response'] = {
    'discussions': [
        {
            'author': {
                'name': 'name of user_id is fc4c3c81-ebc3-4957-8c62-e1cbb6238b27',
                'profile_pic_url': 'https://graph.ib_users.com/fc4c3c81-ebc3-4957-8c62-e1cbb6238b27/picture',
                'user_id': 'fc4c3c81-ebc3-4957-8c62-e1cbb6238b27'
            },
            'created_at': '2008-01-01 00:00:00',
            'description': 'description',
            'discussion_id': 'c5a444ea-589a-4e8f-b006-cfac3c1c0b78',
            'is_clarified': True,
            'title': 'title'
        },
        {
            'author': {
                'name': 'name of user_id is 458813d7-9954-44fd-a014-a9faafce5948',
                'profile_pic_url': 'https://graph.ib_users.com/458813d7-9954-44fd-a014-a9faafce5948/picture',
                'user_id': '458813d7-9954-44fd-a014-a9faafce5948'
            },
            'created_at': '2008-01-01 00:00:00',
            'description': 'description',
            'discussion_id': '5ce6581b-86ce-4246-8551-2c8a8ed4df87',
            'is_clarified': False,
            'title': 'title'
        },
        {
            'author': {
                'name': 'name of user_id is 06b0bdc4-76ac-4a01-a4da-68156f0527f5',
                'profile_pic_url': 'https://graph.ib_users.com/06b0bdc4-76ac-4a01-a4da-68156f0527f5/picture',
                'user_id': '06b0bdc4-76ac-4a01-a4da-68156f0527f5'
            },
            'created_at': '2008-01-01 00:00:00',
            'description': 'description',
            'discussion_id': 'ed10c17c-8995-4d84-9807-189a54a2049d',
            'is_clarified': True,
            'title': 'title'
        }
    ],
    'total_count': 3
}
