# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestGetProjectsPresenterImplementation.test_get_response_for_get_projects_returns_projects projects'] = {
    'projects': [
        {
            'description': 'description 1',
            'logo_url': 'logo 1',
            'name': 'name 1',
            'project_id': 'f2c02d98-f311-4ab2-8673-3daa00757002',
            'roles': [
                {
                    'role_id': 'f2c02d98-f311-4ab2-8673-3daa00757002',
                    'role_name': 'role 1'
                }
            ],
            'teams': [
                {
                    'team_id': 'f2c02d98-f311-4ab2-8673-3daa00757002',
                    'team_name': 'team 1'
                }
            ]
        }
    ],
    'total_projects_count': 1
}
