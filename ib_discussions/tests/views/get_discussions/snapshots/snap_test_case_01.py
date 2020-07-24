# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetDiscussionsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetDiscussionsAPITestCase.test_case body'] = {
    'discussions': [
        {
            'author': {
                'name': 'name of user_id is 9cc22e39-2390-4d96-b7ac-6bb27816461f',
                'profile_pic_url': 'https://graph.ib_users.com/9cc22e39-2390-4d96-b7ac-6bb27816461f/picture',
                'user_id': '9cc22e39-2390-4d96-b7ac-6bb27816461f'
            },
            'created_at': '2020-01-20 00:00:00',
            'description': 'description',
            'discussion_id': '802bdcf5-efd2-4227-9c42-df8089712d52',
            'is_clarified': True,
            'title': 'title'
        },
        {
            'author': {
                'name': 'name of user_id is cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a',
                'profile_pic_url': 'https://graph.ib_users.com/cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a/picture',
                'user_id': 'cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a'
            },
            'created_at': '2020-01-20 00:00:00',
            'description': 'description',
            'discussion_id': 'c30ad6d3-50fa-4d79-806a-a8d1b1e1be5e',
            'is_clarified': True,
            'title': 'title'
        }
    ],
    'total_count': 12
}
