# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetChecklistPresenterImplementation.test_whether_it_returns_checklist_items_and_entity_http_response response'] = {
    'checklist': [
        {
            'checklist_item_id': 'aacb164b-343e-4a8a-990a-f67a0c3f1f39',
            'is_checked': False,
            'text': 'text7'
        },
        {
            'checklist_item_id': 'd59ffc8d-e530-4e2e-95b2-d0f5ee3f5485',
            'is_checked': False,
            'text': 'text8'
        },
        {
            'checklist_item_id': 'c9414ad0-aa48-423f-adcf-31ef96dd4e8a',
            'is_checked': False,
            'text': 'text9'
        }
    ],
    'entity_id': '29aa0d0b-75ce-433a-87a7-f14ab71738d6',
    'entity_type': 'TASK'
}
