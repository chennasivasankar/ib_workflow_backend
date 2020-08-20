# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01DeleteChecklistItemsAPITestCase.test_success_case_for_delete_checklist_items status_code'] = '200'

snapshots['TestCase01DeleteChecklistItemsAPITestCase.test_success_case_for_delete_checklist_items body'] = {
}

snapshots['TestCase01DeleteChecklistItemsAPITestCase.test_duplicate_items_response status_code'] = '400'

snapshots['TestCase01DeleteChecklistItemsAPITestCase.test_duplicate_items_response body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_CHECKLIST_ITEM_IDS',
    'response': 'Given checklist item ids are duplicated'
}

snapshots['TestCase01DeleteChecklistItemsAPITestCase.test_invalid_checklist_item_ids_response status_code'] = '404'

snapshots['TestCase01DeleteChecklistItemsAPITestCase.test_invalid_checklist_item_ids_response body'] = {
    'http_status_code': 404,
    'res_status': 'CHECKLIST_ITEM_IDS_NOT_FOUND',
    'response': 'Given Checklist item ids not found'
}
