# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase13SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase13SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'DUPLICATE_SAME_GOF_ORDERS_FOR_A_GOF',
    'response': 'duplicate same gof orders given for gof gof_2, duplicates are [0]'
}