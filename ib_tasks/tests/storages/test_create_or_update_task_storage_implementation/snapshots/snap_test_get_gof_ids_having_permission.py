# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetGoFIdsHavingPermission.test_given_gof_ids_and_user_roles_returns_gof_ids_having_permission_for_roles gof_ids_having_permission'] = [
    'gof_2',
    'gof_4',
    'gof_10',
    'gof_11'
]

snapshots['TestGetGoFIdsHavingPermission.test_given_gof_ids_and_user_roles_not_having_permission_for_gof_ids_but_permission_for_all_roles_returns_gof_ids gof_ids_having_permission'] = [
    'gof_11'
]
