# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestGetTeamMemberIdsDtos.test_whether_it_returns_list_of_team_members_dtos result'] = [
    GenericRepr("TeamMembersDTO(team_id='f2c02d98-f311-4ab2-8673-3daa00757002', member_ids=['2bdb417e-4632-419a-8ddd-085ea272c6eb', '548a803c-7b48-47ba-a700-24f2ea0d1280', '4b8fb6eb-fa7d-47c1-8726-cd917901104e'])"),
    GenericRepr("TeamMembersDTO(team_id='aa66c40f-6d93-484a-b418-984716514c7b', member_ids=['7ee2c7b4-34c8-4d65-a83a-f87da75db24e', '2bdb417e-4632-419a-8ddd-085ea272c6eb'])"),
    GenericRepr("TeamMembersDTO(team_id='c982032b-53a7-4dfa-a627-4701a5230765', member_ids=['548a803c-7b48-47ba-a700-24f2ea0d1280', '4b8fb6eb-fa7d-47c1-8726-cd917901104e', '7ee2c7b4-34c8-4d65-a83a-f87da75db24e'])")
]
