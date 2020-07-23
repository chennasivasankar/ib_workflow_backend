# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGlobalConstants.test_with_invalid_template_raises_exception message'] = 'The template with template id: FIN_MAN, does not exists'

snapshots['TestGlobalConstants.test_when_given_template_id_is_empty_raises_exception message'] = 'Invalid value for template id!, template id should not be empty'

snapshots['TestGlobalConstants.test_when_given_constant_name_is_empty_raises_exception message'] = 'Invalid value for constant name!, constant name should not be empty'

snapshots['TestGlobalConstants.test_when_given_invalid_value_for_value_field_raises_exception message'] = 'Invalid value for value!, value should not be negative!, but given value is: -1'

snapshots['TestGlobalConstants.test_when_given_duplicate_constant_names_raises_exception message'] = "Given duplicate constant names ['iB_Hubs']"

snapshots['TestGlobalConstants.test_with_valid_data task_template_id_1'] = 'TEMPLATE_ID-0'

snapshots['TestGlobalConstants.test_with_valid_data constant_name_1'] = 'Constant_1'

snapshots['TestGlobalConstants.test_with_valid_data value_1'] = 0

snapshots['TestGlobalConstants.test_with_valid_data task_template_id_2'] = 'TEMPLATE_ID-0'

snapshots['TestGlobalConstants.test_with_valid_data constant_name_2'] = 'Constant_2'

snapshots['TestGlobalConstants.test_with_valid_data value_2'] = 1

snapshots['TestGlobalConstants.test_with_existing_constants_not_in_given_data_raises_exception_after_creating_given_data message'] = "Existing constants with constant names: ['Constant_0'] of template not in given data"

snapshots['TestGlobalConstants.test_with_existing_constants_not_in_given_data_raises_exception_after_creating_given_data task_template_id_1'] = 'TEMPLATE_ID-0'

snapshots['TestGlobalConstants.test_with_existing_constants_not_in_given_data_raises_exception_after_creating_given_data constant_name_1'] = 'Constant_0'

snapshots['TestGlobalConstants.test_with_existing_constants_not_in_given_data_raises_exception_after_creating_given_data value_1'] = 1

snapshots['TestGlobalConstants.test_with_existing_constants_not_in_given_data_raises_exception_after_creating_given_data task_template_id_2'] = 'TEMPLATE_ID-0'

snapshots['TestGlobalConstants.test_with_existing_constants_not_in_given_data_raises_exception_after_creating_given_data constant_name_2'] = 'Constant_1'

snapshots['TestGlobalConstants.test_with_existing_constants_not_in_given_data_raises_exception_after_creating_given_data value_2'] = 0

snapshots['TestGlobalConstants.test_with_existing_constants_not_in_given_data_raises_exception_after_creating_given_data task_template_id_3'] = 'TEMPLATE_ID-0'

snapshots['TestGlobalConstants.test_with_existing_constants_not_in_given_data_raises_exception_after_creating_given_data constant_name_3'] = 'Constant_2'

snapshots['TestGlobalConstants.test_with_existing_constants_not_in_given_data_raises_exception_after_creating_given_data value_3'] = 1

snapshots['TestGlobalConstants.test_with_existing_constant_but_different_configuration_updates_constant task_template_id_1'] = 'TEMPLATE_ID-0'

snapshots['TestGlobalConstants.test_with_existing_constant_but_different_configuration_updates_constant constant_name_1'] = 'Constant_0'

snapshots['TestGlobalConstants.test_with_existing_constant_but_different_configuration_updates_constant value_1'] = 10000
