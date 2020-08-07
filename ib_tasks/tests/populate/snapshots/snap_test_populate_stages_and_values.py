# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestPopulateStagesAndValues.test_with_valid_keys_returns_list_of_stage_dtos populated_stages'] = [
    {
        'card_info_kanban': '["field_id_1", "field_id_2"]',
        'card_info_list': '["field_id_1", "field_id_2"]',
        'display_logic': 'status_id_1==stage_id',
        'display_name': 'name_1',
        'id': 2,
        'stage_color': 'blue',
        'stage_id': 'stage_id_2',
        'task_template_id': 'task_template_id_1',
        'value': 1
    },
    {
        'card_info_kanban': '["field_id_1", "field_id_2"]',
        'card_info_list': '["field_id_1", "field_id_2"]',
        'display_logic': 'status_id_2==stage_id',
        'display_name': 'name_2',
        'id': 3,
        'stage_color': 'blue',
        'stage_id': 'stage_id_3',
        'task_template_id': 'task_template_id_2',
        'value': 2
    }
]
