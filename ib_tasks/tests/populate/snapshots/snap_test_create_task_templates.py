# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCreateTaskTemplate.test_with_invalid_template_id_raises_exception err_msg'] = 'Invalid value for field: template_id'

snapshots['TestCreateTaskTemplate.test_with_invalid_template_name_raises_exception err_msg'] = 'Invalid value for field: template_name'

snapshots['TestCreateTaskTemplate.test_with_valid_data template_id'] = 'template_1'

snapshots['TestCreateTaskTemplate.test_with_valid_data template_name'] = 'Template 1'

snapshots['TestCreateTaskTemplate.test_with_existing_template_id_but_different_name_updates_template template_id'] = 'template_1'

snapshots['TestCreateTaskTemplate.test_with_existing_template_id_but_different_name_updates_template template_name'] = 'iBHubs 1'
