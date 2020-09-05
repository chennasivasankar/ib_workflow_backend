# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase06CreateTransitionChecklistAPITestCase.test_case status_code'] = '400'

snapshots['TestCase06CreateTransitionChecklistAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'TRANSITION_TEMPLATE_IS_NOT_RELATED_TO_GIVEN_STAGE_ACTION',
    'response': 'given transition template id transition_template_1 is not linked to given stage id 1 and action id 1'
}
