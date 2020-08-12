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
                'name': 'name',
                'profile_pic_url': 'https://graph.ib_users.com/',
                'user_id': 'e597ab2f-a10c-4164-930e-23af375741cb'
            },
            'created_at': '2008-01-01 00:00:00',
            'description': 'description',
            'discussion_id': '75e86ce9-337b-4720-9edb-ff9e7d006be1',
            'is_clarified': True,
            'is_editable': True,
            'title': 'title',
            'total_comments_count': 0
        },
        {
            'author': {
                'name': 'name',
                'profile_pic_url': 'https://graph.ib_users.com/',
                'user_id': 'cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a'
            },
            'created_at': '2008-01-01 00:00:00',
            'description': 'description',
            'discussion_id': '7b9486ac-7eb6-424b-bc85-71598d000654',
            'is_clarified': True,
            'is_editable': False,
            'title': 'title',
            'total_comments_count': 0
        }
    ],
    'total_count': 6
}
