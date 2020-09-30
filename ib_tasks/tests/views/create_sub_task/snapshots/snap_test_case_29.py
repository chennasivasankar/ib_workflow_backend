# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase29CreateSubTaskAPITestCase.test_case[viserys] status_code'] = '400'

snapshots['TestCase29CreateSubTaskAPITestCase.test_case[viserys] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_VALUE_FOR_DROPDOWN',
    'response': "Invalid dropdown value: viserys for field: DISPLAY_NAME-0! Try with these dropdown values: ['Drogon', 'Big Drogon']"
}

snapshots['TestCase29CreateSubTaskAPITestCase.test_case[aegon] status_code'] = '400'

snapshots['TestCase29CreateSubTaskAPITestCase.test_case[aegon] body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_VALUE_FOR_DROPDOWN',
    'response': "Invalid dropdown value: aegon for field: DISPLAY_NAME-0! Try with these dropdown values: ['Drogon', 'Big Drogon']"
}
