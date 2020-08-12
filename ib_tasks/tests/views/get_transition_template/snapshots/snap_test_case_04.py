# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase04GetTransitionTemplateAPITestCase.test_case status_code'] = '200'

snapshots['TestCase04GetTransitionTemplateAPITestCase.test_case body'] = {
    'group_of_fields': [
        {
            'enable_add_another': True,
            'fields': [
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-0',
            'gof_id': 'gof_1',
            'max_columns': 2,
            'order': 0
        },
        {
            'enable_add_another': False,
            'fields': [
            ],
            'gof_display_name': 'GOF_DISPLAY_NAME-1',
            'gof_id': 'gof_2',
            'max_columns': 2,
            'order': 1
        }
    ],
    'transition_template_id': 'template_1',
    'transition_template_name': 'Template 1'
}
