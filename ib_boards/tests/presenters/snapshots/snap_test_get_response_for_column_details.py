# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    'TestGetColumnDetails.test_get_response_for_column_details list_of_column_details'] = {
    'columns': [
        {
            'column_id': 'COLUMN_ID_1',
            'name': 'COLUMN_DISPLAY_NAME_1',
            'tasks': [
            ],
            'total_tasks_count': 0
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
        }
    ],
    'total_columns_count': 3
}
