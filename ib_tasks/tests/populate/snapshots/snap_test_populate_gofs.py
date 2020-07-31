# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestPopulateGoFs.test_populate_gofs_with_empty_gof_ids[None] empty_gof_id_message'] = 'GoF id should not be empty'

snapshots['TestPopulateGoFs.test_populate_gofs_with_empty_gof_ids[] empty_gof_id_message'] = 'GoF id should not be empty'

snapshots['TestPopulateGoFs.test_populate_gofs_with_empty_gof_display_names[None] empty_gof_display_name_message'] = 'GoF name should not be empty'

snapshots['TestPopulateGoFs.test_populate_gofs_with_empty_gof_display_names[] empty_gof_display_name_message'] = 'GoF name should not be empty'

snapshots['TestPopulateGoFs.test_populate_gofs_with_invalid_max_columns_value[0] invalid_max_columns_message'] = 'Max columns value must be greater than zero: 0'

snapshots['TestPopulateGoFs.test_populate_gofs_with_invalid_max_columns_value[-1] invalid_max_columns_message'] = 'Max columns value must be greater than zero: -1'

snapshots['TestPopulateGoFs.test_populate_gofs_with_empty_read_permissions[None] empty_gof_read_permission_roles_message'] = 'GoF read permissions should not be empty'

snapshots['TestPopulateGoFs.test_populate_gofs_with_empty_read_permissions[read_permissions1] empty_gof_read_permission_roles_message'] = 'GoF read permissions should not be empty'

snapshots['TestPopulateGoFs.test_populate_gofs_with_empty_write_permissions[None] empty_gof_write_permission_roles_message'] = 'GoF write permissions should not be empty'

snapshots['TestPopulateGoFs.test_populate_gofs_with_empty_write_permissions[write_permissions1] empty_gof_write_permission_roles_message'] = 'GoF write permissions should not be empty'

snapshots['TestPopulateGoFs.test_populate_gofs_with_invalid_read_permission_roles invalid_gof_read_permission_roles_message'] = "Invalid Read Permission roles:['Payment Requestor']"

snapshots['TestPopulateGoFs.test_populate_gofs_with_invalid_write_permission_roles invalid_gof_write_permission_roles_message'] = "Invalid Write Permission roles:['Payment Requestor']"

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_id 1'] = 'gof_1'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_display_name 1'] = 'GOF_DISPLAY_NAME-1'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_max_columns 1'] = 2

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_id 2'] = 'gof_2'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_display_name 2'] = 'GOF_DISPLAY_NAME-2'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_max_columns 2'] = 2

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_id 3'] = 'gof_3'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_display_name 3'] = 'GOF_DISPLAY_NAME-3'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_max_columns 3'] = 2

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_id_in_gof_role 1'] = 'gof_1'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_read_permission_role 1'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details read_role_permission_type 1'] = 'READ'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_write_permission_role 1'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details write_role_permission_type 1'] = 'WRITE'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_id_in_gof_role 2'] = 'gof_2'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_read_permission_role 2'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details read_role_permission_type 2'] = 'READ'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_write_permission_role 2'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details write_role_permission_type 2'] = 'WRITE'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_id_in_gof_role 3'] = 'gof_3'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_read_permission_role 3'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details read_role_permission_type 3'] = 'READ'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details gof_write_permission_role 3'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_valid_details write_role_permission_type 3'] = 'WRITE'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_id 1'] = 'gof_1'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_display_name 1'] = 'GOF_DISPLAY_NAME-1'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_max_columns 1'] = 2

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_id 2'] = 'gof_2'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_display_name 2'] = 'GOF_DISPLAY_NAME-2'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_max_columns 2'] = 2

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_id 3'] = 'gof_3'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_display_name 3'] = 'GOF_DISPLAY_NAME-3'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_max_columns 3'] = 2

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_id 4'] = 'gof_4'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_display_name 4'] = 'GOF_DISPLAY_NAME-4'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_max_columns 4'] = 2

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_id_in_gof_role 1'] = 'gof_1'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_read_permission_role 1'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs read_role_permission_type 1'] = 'READ'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_write_permission_role 1'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs write_role_permission_type 1'] = 'WRITE'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_id_in_gof_role 2'] = 'gof_2'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_read_permission_role 2'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs read_role_permission_type 2'] = 'READ'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_write_permission_role 2'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs write_role_permission_type 2'] = 'WRITE'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_id_in_gof_role 3'] = 'gof_3'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_read_permission_role 3'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs read_role_permission_type 3'] = 'READ'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_write_permission_role 3'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs write_role_permission_type 3'] = 'WRITE'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_id_in_gof_role 4'] = 'gof_4'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_read_permission_role 4'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs read_role_permission_type 4'] = 'READ'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs gof_write_permission_role 4'] = 'ALL_ROLES'

snapshots['TestPopulateGoFs.test_populate_gofs_with_already_existing_gofs_updates_gofs write_role_permission_type 4'] = 'WRITE'

snapshots['TestPopulateGoFs.test_populate_gofs_with_empty_gof_ids[ ] empty_gof_id_message'] = 'GoF id should not be empty'

snapshots['TestPopulateGoFs.test_populate_gofs_with_empty_gof_display_names[ ] empty_gof_display_name_message'] = 'GoF name should not be empty'

snapshots['TestPopulateGoFs.test_populate_gofs_with_empty_gof_ids[  ] empty_gof_id_message'] = 'GoF id should not be empty'

snapshots['TestPopulateGoFs.test_populate_gofs_with_empty_gof_display_names[  ] empty_gof_display_name_message'] = 'GoF name should not be empty'
