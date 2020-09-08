# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetGoFIdsHavingPermission.test_given_gof_ids_and_user_roles_returns_gof_ids_having_permission_for_roles gof_ids_having_permission'] = [
    'gof_40',
    'gof_42',
    'gof_48',
    'gof_49'
]

snapshots['TestGetGoFIdsHavingPermission.test_given_gof_ids_and_user_roles_not_having_permission_for_gof_ids_but_permission_for_all_roles_returns_gof_ids gof_ids_having_permission'] = [
    'gof_60'
]
