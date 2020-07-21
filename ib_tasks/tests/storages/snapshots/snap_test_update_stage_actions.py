# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestUpdateStageActions.test_with_action_details_Updates_action roles'] = GenericRepr("<QuerySet [{'id': 1, 'action_id': 1, 'role_id': 'Role_1'}, {'id': 2, 'action_id': 2, 'role_id': 'Role_1'}, {'id': 3, 'action_id': 3, 'role_id': 'Role_1'}, {'id': 4, 'action_id': 4, 'role_id': 'Role_1'}]>")

snapshots['TestUpdateStageActions.test_with_action_details_Updates_action stage_actions'] = GenericRepr("<QuerySet [{'id': 1, 'stage_id': 5, 'name': 'name_0', 'button_text': 'hey', 'button_color': '#fafafa', 'logic': 'Status1 = PR_PAYMENT_REQUEST_DRAFTS', 'py_function_import_path': 'path'}, {'id': 2, 'stage_id': 6, 'name': 'name_1', 'button_text': 'hey', 'button_color': '#fafafa', 'logic': 'Status1 = PR_PAYMENT_REQUEST_DRAFTS', 'py_function_import_path': 'path'}, {'id': 3, 'stage_id': 7, 'name': 'name_2', 'button_text': 'hey', 'button_color': '#fafafa', 'logic': 'Status1 = PR_PAYMENT_REQUEST_DRAFTS', 'py_function_import_path': 'path'}, {'id': 4, 'stage_id': 8, 'name': 'name_3', 'button_text': 'hey', 'button_color': '#fafafa', 'logic': 'Status1 = PR_PAYMENT_REQUEST_DRAFTS', 'py_function_import_path': 'path'}]>")
