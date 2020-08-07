# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetChecklistAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetChecklistAPITestCase.test_case body'] = {
    'checklist': [
        {
            'checklist_item_id': 1,
            'is_checked': True,
            'text': 'string'
        }
    ],
    'entity_id': 'string',
    'entity_type': 'TASK'
}
