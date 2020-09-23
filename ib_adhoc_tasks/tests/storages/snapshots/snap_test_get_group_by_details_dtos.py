# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestStorageImplementation.test_given_user_id_returns_group_by_details_dtos group_by_details_dtos'] = [
    GenericRepr("GroupByDetailsDTO(group_by='ASSIGNEE', order=1)"),
    GenericRepr("GroupByDetailsDTO(group_by='STAGE', order=2)")
]
