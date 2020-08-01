# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetTaskAPITestCase::test_case status'] = 200

snapshots['TestCase01GetTaskAPITestCase::test_case body'] = {
    'gofs': [
        {
            'gof_fields': [
                {
                    'field_id': 'string',
                    'field_response': 'string'
                }
            ],
            'gof_id': 'string',
            'same_gof_order': 1.1
        }
    ],
    'stages_with_actions': [
        {
            'actions': [
                {
                    'action_id': 'string',
                    'button_color': 'string',
                    'button_text': 'string'
                }
            ],
            'stage_display_name': 'string',
            'stage_id': 'string'
        }
    ],
    'task_id': 'string',
    'template_id': 'string'
}

snapshots['TestCase01GetTaskAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '314',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}
