# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02AddOrEditGroupByAPITestCase.test_one_group_by_already_exists_in_list_view_retuens_usser_not_allowed_to_create_more_than_one_group_by_in_list_view status_code'] = '400'

snapshots['TestCase02AddOrEditGroupByAPITestCase.test_one_group_by_already_exists_in_list_view_retuens_usser_not_allowed_to_create_more_than_one_group_by_in_list_view body'] = {
    'http_status_code': 400,
    'res_status': 'USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_ONE_GROUP_BY_IN_LIST_VIEW',
    'response': 'user is not allowed to create more than one group_by in list view'
}

snapshots['TestCase02AddOrEditGroupByAPITestCase.test_two_group_by_already_exists_in_kaban_view_retuens_usser_not_allowed_to_create_more_than_two_group_by_in_kanban_view status_code'] = '400'

snapshots['TestCase02AddOrEditGroupByAPITestCase.test_two_group_by_already_exists_in_kaban_view_retuens_usser_not_allowed_to_create_more_than_two_group_by_in_kanban_view body'] = {
    'http_status_code': 400,
    'res_status': 'USER_NOT_ALLOWED_TO_CREATE_MORE_THAN_TWO_GROUP_BY_IN_KANBAN_VIEW',
    'response': 'user is not allowed to create more than two group_by in kanban view'
}
