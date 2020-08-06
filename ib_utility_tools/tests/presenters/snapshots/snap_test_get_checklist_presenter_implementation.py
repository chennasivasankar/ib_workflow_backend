# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetChecklistPresenterImplementation.test_whether_it_returns_checklist_items_and_entity_http_response response'] = {
    'checklist': [
        {
            'checklist_item_id': '7ee2c7b4-34c8-4d65-a83a-f87da75db24e',
            'is_checked': False,
            'text': 'text1'
        },
        {
            'checklist_item_id': '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a',
            'is_checked': False,
            'text': 'text2'
        }
    ],
    'entity_id': 'bb3e538e-a18a-4268-b2d6-0b6dba669ba0',
    'entity_type': 'TASK'
}
