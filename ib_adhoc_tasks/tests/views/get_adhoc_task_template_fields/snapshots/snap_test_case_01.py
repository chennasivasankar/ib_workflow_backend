# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAdhocTaskTemplateFieldsAPITestCase.test_given_valid_data_returns_group_by_key_and_display_names status_code'] = '200'

snapshots['TestCase01GetAdhocTaskTemplateFieldsAPITestCase.test_given_valid_data_returns_group_by_key_and_display_names body'] = [
    {
        'display_name': 'field_display_name1',
        'group_by_key': 'field_1'
    },
    {
        'display_name': 'Stage',
        'group_by_key': 'STAGE'
    },
    {
        'display_name': 'Assignee',
        'group_by_key': 'ASSIGNEE'
    }
]
