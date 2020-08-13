# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03GetTransitionTemplateAPITestCase.test_case status_code'] = '200'

snapshots['TestCase03GetTransitionTemplateAPITestCase.test_case body'] = {
    'group_of_fields': [
    ],
    'transition_template_id': 'template_1',
    'transition_template_name': 'Template 1'
}
