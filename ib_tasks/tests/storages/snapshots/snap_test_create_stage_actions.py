# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot


snapshots = Snapshot()

snapshots['TestCreateStageActions.test_with_action_details_creates_action roles'] = GenericRepr("<QuerySet [{'id': 1, 'action_id_id': 1, 'role_id': 'ALL_ROLES'}, {'id': 2, 'action_id_id': 2, 'role_id': 'ALL_ROLES'}, {'id': 3, 'action_id_id': 3, 'role_id': 'ALL_ROLES'}, {'id': 4, 'action_id_id': 4, 'role_id': 'ALL_ROLES'}]>")

snapshots['TestCreateStageActions.test_with_action_details_creates_action stage_actions'] = GenericRepr("<QuerySet [{'id': 1, 'stage_id': 1, 'name': 'name_0', 'button_text': 'text', 'button_color': None, 'logic': 'status_id_0==stage_id', 'py_function_import_path': 'path'}, {'id': 2, 'stage_id': 2, 'name': 'name_1', 'button_text': 'text', 'button_color': None, 'logic': 'status_id_1==stage_id', 'py_function_import_path': 'path'}, {'id': 3, 'stage_id': 3, 'name': 'name_2', 'button_text': 'text', 'button_color': None, 'logic': 'status_id_2==stage_id', 'py_function_import_path': 'path'}, {'id': 4, 'stage_id': 4, 'name': 'name_3', 'button_text': 'text', 'button_color': None, 'logic': 'status_id_3==stage_id', 'py_function_import_path': 'path'}]>")
