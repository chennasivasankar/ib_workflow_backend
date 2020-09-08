# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestUpdateStageActions.test_with_action_details_updates_action roles'] = GenericRepr("<QuerySet [{'id': 1, 'action_id': 2, 'role_id': 'ROLE_1'}, {'id': 2, 'action_id': 2, 'role_id': 'ROLE_2'}, {'id': 3, 'action_id': 3, 'role_id': 'ROLE_2'}, {'id': 4, 'action_id': 3, 'role_id': 'ROLE_3'}, {'id': 5, 'action_id': 4, 'role_id': 'ROLE_3'}, {'id': 6, 'action_id': 4, 'role_id': 'ROLE_4'}, {'id': 7, 'action_id': 5, 'role_id': 'ROLE_4'}, {'id': 8, 'action_id': 5, 'role_id': 'ROLE_5'}]>")
