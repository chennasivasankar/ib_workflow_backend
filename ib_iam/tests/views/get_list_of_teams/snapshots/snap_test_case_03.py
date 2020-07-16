# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetListOfTeamsAPITestCase.test_case status_code'] = '400'

snapshots['TestCase01GetListOfTeamsAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_LIMIT',
    'response': 'Given limit is not valid, please check it'
}

snapshots['TestCase03GetListOfTeamsAPITestCase.test_case status_code'] = '400'

snapshots['TestCase03GetListOfTeamsAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_LIMIT',
    'response': 'Given limit is not valid, please check it'
}
