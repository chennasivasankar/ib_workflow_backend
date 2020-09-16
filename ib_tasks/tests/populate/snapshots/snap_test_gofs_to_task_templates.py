# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGoFsToTaskTemplate.test_with_invalid_template_raises_exception message'] = 'The template with template id: FIN_MAN, does not exists'

snapshots['TestGoFsToTaskTemplate.test_when_given_template_id_is_empty_raises_exception message'] = 'Invalid value for template id!, template id should not be empty'

snapshots['TestGoFsToTaskTemplate.test_when_given_gof_id_is_empty_raises_exception message'] = 'Invalid value for gof_ids, got empty string'

snapshots['TestGoFsToTaskTemplate.test_when_given_invalid_value_for_order_raises_exception message'] = "Value for order should not be less than -1, got invalid values for these gof_ids: ['gof_1', 'gof_2']"

snapshots['TestGoFsToTaskTemplate.test_with_duplicate_values_for_orders_of_gof_ids_raises_exception message'] = 'Given duplicate order values [1]! Gof orders of a template should be unique'

snapshots['TestGoFsToTaskTemplate.test_when_given_invalid_gofs_raises_exception message'] = "The gofs with gof_ids: ['gof_1', 'gof_2'], does not exists"

snapshots['TestGoFsToTaskTemplate.test_with_valid_data task_template_id_1'] = 'template_1'

snapshots['TestGoFsToTaskTemplate.test_with_valid_data gof_id_1'] = 'gof_1'

snapshots['TestGoFsToTaskTemplate.test_with_valid_data order_1'] = 0

snapshots['TestGoFsToTaskTemplate.test_with_valid_data enable_add_another_gof_1'] = True

snapshots['TestGoFsToTaskTemplate.test_with_valid_data task_template_id_2'] = 'template_1'

snapshots['TestGoFsToTaskTemplate.test_with_valid_data gof_id_2'] = 'gof_2'

snapshots['TestGoFsToTaskTemplate.test_with_valid_data order_2'] = 1

snapshots['TestGoFsToTaskTemplate.test_with_valid_data enable_add_another_gof_2'] = False

snapshots['TestGoFsToTaskTemplate.test_with_existing_gofs_of_template_but_different_configuration_updates_gofs_to_template task_template_id_1'] = 'template_1'

snapshots['TestGoFsToTaskTemplate.test_with_existing_gofs_of_template_but_different_configuration_updates_gofs_to_template gof_id_1'] = 'gof_1'

snapshots['TestGoFsToTaskTemplate.test_with_existing_gofs_of_template_but_different_configuration_updates_gofs_to_template order_1'] = 4

snapshots['TestGoFsToTaskTemplate.test_with_existing_gofs_of_template_but_different_configuration_updates_gofs_to_template enable_add_another_gof_1'] = True

snapshots['TestGoFsToTaskTemplate.test_with_existing_gofs_of_template_but_different_configuration_updates_gofs_to_template task_template_id_2'] = 'template_1'

snapshots['TestGoFsToTaskTemplate.test_with_existing_gofs_of_template_but_different_configuration_updates_gofs_to_template gof_id_2'] = 'gof_2'

snapshots['TestGoFsToTaskTemplate.test_with_existing_gofs_of_template_but_different_configuration_updates_gofs_to_template order_2'] = 5

snapshots['TestGoFsToTaskTemplate.test_with_existing_gofs_of_template_but_different_configuration_updates_gofs_to_template enable_add_another_gof_2'] = True

snapshots['TestGoFsToTaskTemplate.test_when_exsting_gofs_not_in_given_data_adds_gofs_to_task_template_and_raises_exception message'] = "Existing GoFs of template with gof_ids: ['gof_2'] are not in given data"

snapshots['TestGoFsToTaskTemplate.test_when_exsting_gofs_not_in_given_data_adds_gofs_to_task_template_and_raises_exception task_template_id_1'] = 'template_1'

snapshots['TestGoFsToTaskTemplate.test_when_exsting_gofs_not_in_given_data_adds_gofs_to_task_template_and_raises_exception gof_id_1'] = 'gof_1'

snapshots['TestGoFsToTaskTemplate.test_when_exsting_gofs_not_in_given_data_adds_gofs_to_task_template_and_raises_exception order_1'] = 2

snapshots['TestGoFsToTaskTemplate.test_when_exsting_gofs_not_in_given_data_adds_gofs_to_task_template_and_raises_exception enable_add_another_gof_1'] = True

snapshots['TestGoFsToTaskTemplate.test_when_exsting_gofs_not_in_given_data_adds_gofs_to_task_template_and_raises_exception task_template_id_2'] = 'template_1'

snapshots['TestGoFsToTaskTemplate.test_when_exsting_gofs_not_in_given_data_adds_gofs_to_task_template_and_raises_exception gof_id_2'] = 'gof_2'

snapshots['TestGoFsToTaskTemplate.test_when_exsting_gofs_not_in_given_data_adds_gofs_to_task_template_and_raises_exception order_2'] = 3

snapshots['TestGoFsToTaskTemplate.test_when_exsting_gofs_not_in_given_data_adds_gofs_to_task_template_and_raises_exception enable_add_another_gof_2'] = False

snapshots['TestGoFsToTaskTemplate.test_with_duplicate_gof_ids_raises_exception duplicate_gof_ids'] = [
    'gof_1'
]
