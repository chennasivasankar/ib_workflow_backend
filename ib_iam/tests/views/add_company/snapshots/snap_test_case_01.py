# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AddCompanyAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01AddCompanyAPITestCase.test_case body'] = {
    'company_id': 'f2c02d98-f311-4ab2-8673-3daa00757002'
}
