# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetChecklistAPITestCase.test_given_valid_entity_details_returns_checklist_items status_code'] = '200'

snapshots['TestCase01GetChecklistAPITestCase.test_given_valid_entity_details_returns_checklist_items body'] = {
    'checklist': [
        {
            'checklist_item_id': '7ee2c7b4-34c8-4d65-a83a-f87da75db24e',
            'is_checked': False,
            'text': 'text2'
        },
        {
            'checklist_item_id': '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5c',
            'is_checked': False,
            'text': 'text1'
        },
        {
            'checklist_item_id': '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a',
            'is_checked': False,
            'text': 'text3'
        }
    ]
}

snapshots['TestCase01GetChecklistAPITestCase.test_given_entity_details_not_have_checklist_returns_empty_list status_code'] = '200'

snapshots['TestCase01GetChecklistAPITestCase.test_given_entity_details_not_have_checklist_returns_empty_list body'] = {
    'checklist': [
    ]
}
