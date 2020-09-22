# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetGroupByPresenterImplementation.test_get_response_for_get_group_by_gives_response_dict group_by_response_dict'] = [
    {
        'display_name': 'ASSIGNEE',
        'group_by_id': 0,
        'group_by_key': 'STAGE',
        'order': 1
    },
    {
        'display_name': 'STAGE',
        'group_by_id': 1,
        'group_by_key': 'ASSIGNEE',
        'order': 2
    }
]
