# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetReasonsForMissingTaskDueDateTimeAPITestCase.test_case status_code'] = '200'

snapshots['TestCase02GetReasonsForMissingTaskDueDateTimeAPITestCase.test_case body'] = [
    {
        'due_date_time': '2020-08-11 14:19:33',
        'due_missed_count': 1,
        'reason': 'Missed reiterating objective',
        'task_id': '1',
        'user': {
            'name': 'name_0',
            'profile_pic': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM',
            'user_id': 'c02fccac-aac9-4045-b03e-5f1e4d06f38b'
        }
    },
    {
        'due_date_time': '2020-08-11 14:19:33',
        'due_missed_count': 2,
        'reason': 'wrong estimation of time',
        'task_id': '1',
        'user': {
            'name': 'name_1',
            'profile_pic': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM',
            'user_id': '123e4567-e89b-12d3-a456-426614174001'
        }
    },
    {
        'due_date_time': '2020-08-11 14:19:33',
        'due_missed_count': 3,
        'reason': 'wrong estimation of time',
        'task_id': '1',
        'user': {
            'name': 'name_2',
            'profile_pic': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM',
            'user_id': '123e4567-e89b-12d3-a456-426614174002'
        }
    },
    {
        'due_date_time': '2020-08-11 14:19:33',
        'due_missed_count': 4,
        'reason': 'wrong estimation of time',
        'task_id': '1',
        'user': {
            'name': 'name_3',
            'profile_pic': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM',
            'user_id': '123e4567-e89b-12d3-a456-426614174003'
        }
    }
]
