# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetGroupByPresenterImplementation.test_get_response_for_get_adhoc_task_template_fields_returns_response_dict response_dict'] = [
    {
        'display_name': 'field_display_name0',
        'group_by_key': 'field_0'
    },
    {
        'display_name': 'field_display_name1',
        'group_by_key': 'field_1'
    }
]
