# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestAddLevelsToTeam.test_with_valid_details_create_team_levels add_team_levels'] = [
    {
        'level_hierarchy': 0,
        'level_name': 'Developer'
    },
    {
        'level_hierarchy': 1,
        'level_name': 'Software Developer Lead'
    },
    {
        'level_hierarchy': 2,
        'level_name': 'Engineer Manager'
    },
    {
        'level_hierarchy': 3,
        'level_name': 'Product Owner'
    }
]
