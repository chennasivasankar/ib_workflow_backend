# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03CreateTransitionChecklistAPITestCase.test_case status_code'] = '400'

snapshots['TestCase03CreateTransitionChecklistAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_TRANSITION_CHECKLIST_TEMPLATE_ID',
    'response': 'please give a valid transition checklist template id, transition_template_100 is invalid transition checklist template id'
}
