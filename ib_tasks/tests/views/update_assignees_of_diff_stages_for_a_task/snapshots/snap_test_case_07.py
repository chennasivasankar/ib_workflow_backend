# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase07UpdateAssigneesOfDiffStagesForATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase07UpdateAssigneesOfDiffStagesForATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'STAGE_IDS_WITH_INVALID_PERMISSION_OF_ASSIGNEE',
    'response': 'Stage ids with invalid permission of assignees that you have sent are: [1, 2, 3],please assign valid assignees for stages'
}
