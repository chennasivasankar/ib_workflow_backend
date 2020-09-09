# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01CreateChecklistItemAPITestCase.test_given_entity_details_not_exists_returns_checklist_item_id status_code'] = '201'

snapshots['TestCase01CreateChecklistItemAPITestCase.test_given_entity_details_not_exists_returns_checklist_item_id body'] = {
    'checklist_item_id': 'f2c02d98-f311-4ab2-8673-3daa00757002'
}

snapshots['TestCase01CreateChecklistItemAPITestCase.test_given_entity_details_not_exists_returns_checklist_item_id checklist_item_text'] = 'As a developer I should create a checklist item1'

snapshots['TestCase01CreateChecklistItemAPITestCase.test_given_entity_details_exists_returns_checklist_item_id status_code'] = '201'

snapshots['TestCase01CreateChecklistItemAPITestCase.test_given_entity_details_exists_returns_checklist_item_id body'] = {
    'checklist_item_id': 'f2c02d98-f311-4ab2-8673-3daa00757003'
}

snapshots['TestCase01CreateChecklistItemAPITestCase.test_given_entity_details_exists_returns_checklist_item_id checklist_item_text'] = 'As a developer I should create a checklist item2'
