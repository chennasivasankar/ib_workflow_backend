# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase30SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase30SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INCORRECT_RADIO_GROUP_CHOICE',
    'response': "Invalid radio group choice: radio_group_choice for field: FIELD_ID-1! Try with these valid options: ['interactors', 'storages']"
}
