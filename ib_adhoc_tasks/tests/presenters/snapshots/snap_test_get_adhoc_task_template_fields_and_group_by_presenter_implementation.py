# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetAdhocTaskTemplateFieldsAndGroupByPresenterImplementation.test_given_valid_data_returns_success_response response_dict'] = {
    'all_fields': [
        {
            'display_name': 'field_display_name0',
            'group_by_key': 'field_0'
        },
        {
            'display_name': 'field_display_name1',
            'group_by_key': 'field_1'
        }
    ],
    'group_by_fields': [
        {
            'display_name': 'Assignee',
            'group_by_key': 'ASSIGNEE',
            'order': 1
        },
        {
            'display_name': 'Stage',
            'group_by_key': 'STAGE',
            'order': 2
        }
    ]
}
