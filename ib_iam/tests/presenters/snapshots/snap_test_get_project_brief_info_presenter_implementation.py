# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetProjectBriefInfoPresenterImplementation.test_success_response_for_get_project_brief_info_return_response get_project_brief_info'] = {
    'projects': [
        {
            'logo_url': 'http://sample.com',
            'name': 'name 1',
            'project_display_id': 'display_id 1',
            'project_id': 'project_1'
        },
        {
            'logo_url': 'http://sample.com',
            'name': 'name 2',
            'project_display_id': 'display_id 2',
            'project_id': 'project_2'
        }
    ]
}
