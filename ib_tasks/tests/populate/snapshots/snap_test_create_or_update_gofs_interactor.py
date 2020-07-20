# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_empty_gof_ids[None] empty_gof_id_message'] = 'GoF id should not be empty'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_empty_gof_ids[] empty_gof_id_message'] = 'GoF id should not be empty'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_empty_gof_ids[  ] empty_gof_id_message'] = 'GoF id should not be empty'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_empty_gof_display_names[None] empty_gof_display_name_message'] = 'GoF name should not be empty'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_empty_gof_display_names[] empty_gof_display_name_message'] = 'GoF name should not be empty'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_empty_gof_display_names[  ] empty_gof_display_name_message'] = 'GoF name should not be empty'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_empty_gof_max_columns[None] empty_gof_max_columns_message'] = 'GoF max columns should not be empty'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_empty_gof_max_columns[] empty_gof_max_columns_message'] = 'GoF max columns should not be empty'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_empty_gof_max_columns[  ] empty_gof_max_columns_message'] = 'GoF max columns should not be empty'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_a_string_as_max_columns_value max_columns_as_string_error_message'] = 'Max columns should not be a string: two'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_invalid_max_columns_value[0] invalid_max_columns_message'] = 'Max columns value must be greater than zero: 0'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_invalid_max_columns_value[-1] invalid_max_columns_message'] = 'Max columns value must be greater than zero: -1'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_empty_read_permissions[None] empty_gof_read_permission_roles_message'] = 'GoF read permissions should not be empty'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_empty_read_permissions[read_permissions1] empty_gof_read_permission_roles_message'] = 'GoF read permissions should not be empty'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_empty_write_permissions[None] empty_gof_write_permission_roles_message'] = 'GoF write permissions should not be empty'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_empty_write_permissions[write_permissions1] empty_gof_write_permission_roles_message'] = 'GoF write permissions should not be empty'

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_invalid_read_permission_roles invalid_gof_read_permission_roles_message'] = "['Payment Requestor']"

snapshots['TestCreateOrUpdateGoFsInteractor.test_create_or_update_gofs_interactor_with_invalid_write_permission_roles invalid_gof_write_permission_roles_message'] = "['Payment Requestor']"
