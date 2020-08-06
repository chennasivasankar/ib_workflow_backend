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
                'name': 'string',
                'profile_pic_url': 'string',
                'user_id': '6e41a6b0-d8ae-4324-959e-ec4786974624'
            },
            'comment_content': 'string',
            'comment_id': 'aafb9eaf-8653-434d-9421-ee060166da85',
            'created_at': '2099-12-31 00:00:00',
            'is_editable': True,
            'replies_count': 1
        }
    ]
}
