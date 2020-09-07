# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase25CreateTransitionChecklistAPITestCase.test_case status_code'] = '400'

snapshots['TestCase25CreateTransitionChecklistAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INCORRECT_MULTI_SELECT_OPTIONS_SELECTED',
    'response': "Invalid multi select options selected: ['Other'] for field: field_1! Try with these valid options: ['Mr', 'Mrs']"
}
