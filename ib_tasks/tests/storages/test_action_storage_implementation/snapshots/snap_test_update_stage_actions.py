# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots['TestUpdateStageActions.test_with_action_details_updates_action roles'] = GenericRepr("<QuerySet [{'id': 41, 'action_id': 2, 'role_id': 'ROLE_1'}, {'id': 42, 'action_id': 2, 'role_id': 'ROLE_2'}, {'id': 43, 'action_id': 3, 'role_id': 'ROLE_2'}, {'id': 44, 'action_id': 3, 'role_id': 'ROLE_3'}, {'id': 45, 'action_id': 4, 'role_id': 'ROLE_3'}, {'id': 46, 'action_id': 4, 'role_id': 'ROLE_4'}, {'id': 47, 'action_id': 5, 'role_id': 'ROLE_4'}, {'id': 48, 'action_id': 5, 'role_id': 'ROLE_5'}]>")
