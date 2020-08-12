# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetStagesHistoryToTaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetStagesHistoryToTaskAPITestCase.test_case body'] = {
    'stages_details': [
        {
            'color': 'blue',
            'name': 'name_0',
            'stage_id': 1
        },
        {
            'color': 'orange',
            'name': 'name_1',
            'stage_id': 2
        }
    ],
    'stages_history': [
        {
            'created_at': '2012-10-10 00:00:00',
            'log_id': 1,
            'stage_id': 1,
            'stage_time': 86400,
            'time_spent_by_user': 86400,
            'user_details': {
                'name': 'name_1',
                'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM',
                'user_id': '1'
            }
        },
        {
            'created_at': '2012-10-10 00:00:00',
            'log_id': 2,
            'stage_id': 2,
            'stage_time': 0,
            'time_spent_by_user': 86400,
            'user_details': {
                'name': 'name_2',
                'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM',
                'user_id': '2'
            }
        }
    ]
}
