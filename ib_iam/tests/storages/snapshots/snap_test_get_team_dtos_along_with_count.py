# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetTeamsDtosAlongWithCount.test_given_admin_returns_list_of_teams result'] = (
    [
        GenericRepr("BasicTeamDTO(team_id='f2c02d98-f311-4ab2-8673-3daa00757002', name='team_name1', description='team_desc1')"),
        GenericRepr("BasicTeamDTO(team_id='aa66c40f-6d93-484a-b418-984716514c7b', name='team_name2', description='team_desc2')"),
        GenericRepr("BasicTeamDTO(team_id='c982032b-53a7-4dfa-a627-4701a5230765', name='team_name3', description='team_desc3')")
    ],
    3
)
