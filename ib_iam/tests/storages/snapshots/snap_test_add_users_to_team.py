# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots['TestAddUsersToTeam.test_given_valid_details_return_nothing team_users'] = GenericRepr("<QuerySet [{'id': 1, 'user_id': '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a', 'team_member_level_id': None, 'immediate_superior_team_user_id': None, 'team_id': UUID('f2c02d98-f311-4ab2-8673-3daa00757002')}, {'id': 2, 'user_id': '8bcf545d-4573-4bc2-b037-16c856d37287', 'team_member_level_id': None, 'immediate_superior_team_user_id': None, 'team_id': UUID('f2c02d98-f311-4ab2-8673-3daa00757002')}]>")
