# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCreateStages.test_create_stages_create_stage_details roles'] = [
    {
        'role_id': 'role_id_0',
        'stage__stage_id': 'stage_id_1'
    },
    {
        'role_id': 'role_id_1',
        'stage__stage_id': 'stage_id_1'
    },
    {
        'role_id': 'role_id_0',
        'stage__stage_id': 'stage_id_2'
    },
    {
        'role_id': 'role_id_2',
        'stage__stage_id': 'stage_id_2'
    },
    {
        'role_id': 'role_id_0',
        'stage__stage_id': 'stage_id_3'
    },
    {
        'role_id': 'role_id_3',
        'stage__stage_id': 'stage_id_3'
    }
]
