# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase02GetTransitionTemplateAPITestCase.test_case status_code'] = '404'

snapshots['TestCase02GetTransitionTemplateAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'TRANSITION_TEMPLATE_DOES_NOT_EXISTS',
    'response': 'Given invalid transition template Id: template_1, that does not exists'
}
