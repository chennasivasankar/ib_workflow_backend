# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetColumnsDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetColumnsDetailsAPITestCase::test_case body'] = {
    'columns': [
        {
            'column_id': 'COLUMN_ID_1',
            'name': 'COLUMN_DISPLAY_NAME_1',
            'tasks': [
                {
                    'actions': [
                        {
                            'action_id': 'action_id_1',
                            'button_color': None,
                            'button_text': 'button_text_1',
                            'name': 'name_1'
                        }
                    ],
                    'fields': [
                        {
                            'field_type': 'field_type_1',
                            'key': 'key_1',
                            'value': 'value_1'
                        }
                    ],
                    'task_id': 'task_id_1'
                }
            ],
            'total_tasks_count': 1
        },
        {
            'column_id': 'COLUMN_ID_2',
            'name': 'COLUMN_DISPLAY_NAME_2',
            'tasks': [
            ],
            'total_tasks_count': 0
        },
        {
            'column_id': 'COLUMN_ID_3',
            'name': 'COLUMN_DISPLAY_NAME_3',
            'tasks': [
            ],
            'total_tasks_count': 0
        },
        {
            'column_id': 'COLUMN_ID_4',
            'name': 'COLUMN_DISPLAY_NAME_4',
            'tasks': [
            ],
            'total_tasks_count': 0
        }
    ],
    'total_columns_count': 4
}

snapshots['TestCase01GetColumnsDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '607',
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

snapshots['TestCase01GetColumnsDetailsAPITestCase::test_case response'] = GenericRepr("<Response status_code=200, "application/json">")
