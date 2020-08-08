# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots['TestCreateStageActions.test_with_action_details_creates_action roles'] = GenericRepr("<QuerySet [{'id': 1, 'action_id': 1, 'role_id': 'Role_1'}, {'id': 2, 'action_id': 1, 'role_id': 'Role_2'}, {'id': 3, 'action_id': 2, 'role_id': 'Role_1'}, {'id': 4, 'action_id': 2, 'role_id': 'Role_2'}, {'id': 5, 'action_id': 3, 'role_id': 'Role_1'}, {'id': 6, 'action_id': 3, 'role_id': 'Role_2'}, {'id': 7, 'action_id': 4, 'role_id': 'Role_1'}, {'id': 8, 'action_id': 4, 'role_id': 'Role_2'}]>")
