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
            'created_at': '2008-01-01 00:00:00',
            'description': 'description',
            'discussion_id': '78a8927c-6732-4f91-a97f-810214a47663',
            'is_clarified': True,
            'title': 'title'
        },
        {
            'author': {
                'name': 'name of user_id is e597ab2f-a10c-4164-930e-23af375741cb',
                'profile_pic_url': 'https://graph.ib_users.com/e597ab2f-a10c-4164-930e-23af375741cb/picture',
                'user_id': 'e597ab2f-a10c-4164-930e-23af375741cb'
            },
            'created_at': '2008-01-01 00:00:00',
            'description': 'description',
            'discussion_id': '802bdcf5-efd2-4227-9c42-df8089712d52',
            'is_clarified': True,
            'title': 'title'
        }
    ],
    'total_count': 6
}
