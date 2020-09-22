# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetTaskIdsForViewInteractor.test_with_valid_details_return_response group_details_dtos'] = [
    GenericRepr("GroupDetailsDTO(task_ids=[19], total_tasks=1, group_by_value='need to pay debt', group_by_display_name='need to pay debt', child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS', child_group_by_display_name='Payment Request Drafts')"),
    GenericRepr("GroupDetailsDTO(task_ids=[20], total_tasks=1, group_by_value='need to pay friend', group_by_display_name='need to pay friend', child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS', child_group_by_display_name='Payment Request Drafts')"),
    GenericRepr("GroupDetailsDTO(task_ids=[24], total_tasks=1, group_by_value='purpose', group_by_display_name='purpose', child_group_by_value='PR_NEED_CLARIFICATION', child_group_by_display_name='Need Clarification')"),
    GenericRepr("GroupDetailsDTO(task_ids=[21], total_tasks=1, group_by_value='sfsdd', group_by_display_name='sfsdd', child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS', child_group_by_display_name='Payment Request Drafts')"),
    GenericRepr("GroupDetailsDTO(task_ids=[25], total_tasks=1, group_by_value='sfsdfsd', group_by_display_name='sfsdfsd', child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS', child_group_by_display_name='Payment Request Drafts')")
]

snapshots['TestGetTaskIdsForViewInteractor.test_with_valid_details_return_response group_count_dto'] = GenericRepr("GroupCountDTO(group_by_value='FIN_PURPOSE_OF_THE_ORDER', total_groups=5)")

snapshots['TestGetTaskIdsForViewInteractor.test_with_valid_details_return_response child_group_count_dtos'] = [
    GenericRepr("ChildGroupCountDTO(child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS', total_child_groups=1)"),
    GenericRepr("ChildGroupCountDTO(child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS', total_child_groups=1)"),
    GenericRepr("ChildGroupCountDTO(child_group_by_value='PR_NEED_CLARIFICATION', total_child_groups=1)"),
    GenericRepr("ChildGroupCountDTO(child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS', total_child_groups=1)"),
    GenericRepr("ChildGroupCountDTO(child_group_by_value='PR_PAYMENT_REQUEST_DRAFTS', total_child_groups=1)")
]
