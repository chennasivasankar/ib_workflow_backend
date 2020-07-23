# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetColumnsDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetColumnsDetailsAPITestCase::test_case body'] = {
    'columns': [
        {
            'column_id': 'string',
            'name': 'string',
            'tasks': [
                {
                    'actions': [
                        {
                            'action_id': 'string',
                            'button_color': 'string',
                            'button_text': 'string',
                            'name': 'string'
                        }
                    ],
                    'fields': [
                        {
                            'field_type': 'string',
                            'key': 'string',
                            'value': 'string'
                        }
                    ],
                    'task_id': 'string'
                }
            ],
            'total_tasks_count': 1
        }
    ],
    'total_columns_count': 1
}

snapshots['TestCase01GetColumnsDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '294',
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
