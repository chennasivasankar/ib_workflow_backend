# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01UpdateChecklistItemAPITestCase.test_given_valid_details_updates_checklist_item status_code'] = '200'

snapshots['TestCase01UpdateChecklistItemAPITestCase.test_given_valid_details_updates_checklist_item body'] = {
}

snapshots['TestCase01UpdateChecklistItemAPITestCase.test_given_valid_details_updates_checklist_item checklist_item_text'] = 'As a developer I should be able to update checklist item'

snapshots['TestCase01UpdateChecklistItemAPITestCase.test_given_invalid_checklist_item_id_returns_invalid_checklist_item_response status_code'] = '404'

snapshots['TestCase01UpdateChecklistItemAPITestCase.test_given_invalid_checklist_item_id_returns_invalid_checklist_item_response body'] = {
    'http_status_code': 400,
    'res_status': 'CHECKLIST_ITEM_ID_NOT_FOUND',
    'response': 'Given checklist item id is not found(invalid)'
}
