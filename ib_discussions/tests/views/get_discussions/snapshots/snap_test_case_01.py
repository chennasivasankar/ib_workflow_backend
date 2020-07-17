# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetDiscussionsAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01GetDiscussionsAPITestCase.test_case body'] = {
    'entity_id': [
        'This field is required.'
    ],
    'entity_type': [
        'This field is required.'
    ]
}
