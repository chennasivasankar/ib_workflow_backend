# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetChecklistAPITestCase.test_case status_code'] = '200'

snapshots['TestCase02GetChecklistAPITestCase.test_case body'] = {
    'checklist': [
    ],
    'entity_id': '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a',
    'entity_type': 'TASK'
}
