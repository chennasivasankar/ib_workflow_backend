# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase24CreateTransitionChecklistAPITestCase.test_case status_code'] = '400'

snapshots['TestCase24CreateTransitionChecklistAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INCORRECT_CHECK_BOX_OPTIONS_SELECTED',
    'response': "Invalid check box options selected: ['Other'] for field: DISPLAY_NAME-0! Try with these valid options: ['Mr', 'Mrs']"
}
