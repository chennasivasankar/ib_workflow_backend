# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02AddOrEditGroupByAPITestCase.test_one_group_by_already_exists_in_list_view_retuens_usser_not_allowed_to_create_more_than_one_group_by_in_list_view status_code'] = '200'

snapshots['TestCase02AddOrEditGroupByAPITestCase.test_one_group_by_already_exists_in_list_view_retuens_usser_not_allowed_to_create_more_than_one_group_by_in_list_view body'] = {
    'display_name': 'STAGE',
    'group_by_id': 2,
    'group_by_key': 'STAGE',
    'order': 1
}

snapshots['TestCase02AddOrEditGroupByAPITestCase.test_two_group_by_already_exists_in_kaban_view_retuens_usser_not_allowed_to_create_more_than_two_group_by_in_kanban_view status_code'] = '501'

snapshots['TestCase02AddOrEditGroupByAPITestCase.test_two_group_by_already_exists_in_kaban_view_retuens_usser_not_allowed_to_create_more_than_two_group_by_in_kanban_view body'] = b'Response for Status Code: 400, Not Defined'
