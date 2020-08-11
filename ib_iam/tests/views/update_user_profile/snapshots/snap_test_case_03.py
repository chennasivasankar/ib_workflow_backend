# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03UpdateUserProfileAPITestCase.test_case status_code'] = '400'

snapshots['TestCase03UpdateUserProfileAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS',
    'response': 'name should not contains special characters and numbers'
}
