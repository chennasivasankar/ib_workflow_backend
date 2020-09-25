# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase42UpdateTaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase42UpdateTaskAPITestCase.test_case body'] = {
    'task_details': {
        'stage_with_actions': {
            'actions': [
            ],
            'assignee': {
                'assignee_id': 'assignee_id_1',
                'name': 'name_0',
                'profile_pic_url': 'https://www.google.com/search?q=ibhubs&client=ubuntu&hs=DI7&channel=fs&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjZqYjthYfrAhUF4zgGHevjDZUQ_AUoA3oECAsQBQ&biw=1848&bih=913#imgrc=Kg3TRY0jmx3udM',
                'team_info': None
            },
            'stage_color': '#fff2f0',
            'stage_display_name': 'display_name_0',
            'stage_id': 1
        },
        'task_id': 'IBWF-1',
        'task_overview_fields': [
        ]
    }
}

snapshots['TestCase42UpdateTaskAPITestCase.test_case task_title'] = 'updated_title'

snapshots['TestCase42UpdateTaskAPITestCase.test_case task_description'] = 'updated_description'

snapshots['TestCase42UpdateTaskAPITestCase.test_case task_start_date'] = '2020-09-20 00:00:00'

snapshots['TestCase42UpdateTaskAPITestCase.test_case task_due_date'] = '2020-10-31 00:00:00'

snapshots['TestCase42UpdateTaskAPITestCase.test_case task_priority'] = 'HIGH'

snapshots['TestCase42UpdateTaskAPITestCase.test_case FIELD-1'] = 'https://www.url.com/file.zip'

snapshots['TestCase42UpdateTaskAPITestCase.test_case FIELD-1 response'] = 'https://www.url.com/file.zip'

snapshots['TestCase42UpdateTaskAPITestCase.test_case task_stage_id'] = 1

snapshots['TestCase42UpdateTaskAPITestCase.test_case task_stage_assignee_id'] = 'assignee_id_1'
