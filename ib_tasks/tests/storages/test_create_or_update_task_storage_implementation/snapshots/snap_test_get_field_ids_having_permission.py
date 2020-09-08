# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestFieldIdsHavingPermission.test_given_field_ids_and_user_roles_returns_field_ids_having_permission_for_roles field_ids_having_permission'] = [
    'FIELD_ID-1',
    'FIELD_ID-11',
    'FIELD_ID-7'
]

snapshots['TestFieldIdsHavingPermission.test_given_field_ids_and_user_roles_not_having_permission_for_field_ids_but_permission_for_all_roles_returns_field_ids field_ids_having_permission'] = [
    'FIELD_ID-22'
]
