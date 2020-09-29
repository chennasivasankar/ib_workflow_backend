# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase33SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase33SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INCORRECT_MULTI_SELECT_LABELS_SELECTED',
    'response': "Invalid multi select labels selected: ['views'] for field: DISPLAY_NAME-0! Try with these valid options: ['interactors', 'storages']"
}
