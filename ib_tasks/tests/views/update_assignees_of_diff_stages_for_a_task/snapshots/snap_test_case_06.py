# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase06UpdateAssigneesOfDiffStagesForATaskAPITestCase.test_case status_code'] = '404'

snapshots['TestCase06UpdateAssigneesOfDiffStagesForATaskAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'USER_NOT_IN_PROJECT',
    'response': 'User Not a part of the Project'
}
