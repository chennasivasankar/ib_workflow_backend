# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestAddProjectToTaskTemplatesInteractor.test_when_no_existing_task_templates_to_project_in_given_ids_then_adds_all_given_templates project_task_template_id_of_project_task_template_1'] = 1

snapshots['TestAddProjectToTaskTemplatesInteractor.test_when_no_existing_task_templates_to_project_in_given_ids_then_adds_all_given_templates project_id_of_project_task_template_1'] = 'CCBP'

snapshots['TestAddProjectToTaskTemplatesInteractor.test_when_no_existing_task_templates_to_project_in_given_ids_then_adds_all_given_templates task_template_id_of_project_task_template_1'] = 'template_1'

snapshots['TestAddProjectToTaskTemplatesInteractor.test_when_no_existing_task_templates_to_project_in_given_ids_then_adds_all_given_templates project_task_template_id_of_project_task_template_2'] = 2

snapshots['TestAddProjectToTaskTemplatesInteractor.test_when_no_existing_task_templates_to_project_in_given_ids_then_adds_all_given_templates project_id_of_project_task_template_2'] = 'CCBP'

snapshots['TestAddProjectToTaskTemplatesInteractor.test_when_no_existing_task_templates_to_project_in_given_ids_then_adds_all_given_templates task_template_id_of_project_task_template_2'] = 'template_2'

snapshots['TestAddProjectToTaskTemplatesInteractor.test_when_existing_task_templates_to_project_in_given_ids_then_adds_remaining_templates project_task_template_id_of_new_project_task_template'] = 2

snapshots['TestAddProjectToTaskTemplatesInteractor.test_when_existing_task_templates_to_project_in_given_ids_then_adds_remaining_templates project_id_of_new_project_task_template'] = 'CCBP'

snapshots['TestAddProjectToTaskTemplatesInteractor.test_when_existing_task_templates_to_project_in_given_ids_then_adds_remaining_templates task_template_id_of_new_project_task_template_1'] = 'template_2'
