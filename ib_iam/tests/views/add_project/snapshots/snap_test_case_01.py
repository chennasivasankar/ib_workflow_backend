# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AddProjectAPITestCase.test_case status_code'] = '201'

snapshots['TestCase01AddProjectAPITestCase.test_case body'] = {
}

snapshots['TestCase01AddProjectAPITestCase.test_case project_details'] = [
    {
        'description': 'project_description',
        'display_id': 'display_id 1',
        'logo_url': 'https://logo.com',
        'name': 'project_1',
        'project_id': 'project_7eb737be-810f-4580-83ea-ff4fa67edd22'
    }
]

snapshots['TestCase01AddProjectAPITestCase.test_case project_team_ids'] = [
    'f2c02d98-f311-4ab2-8673-3daa00757003'
]

snapshots['TestCase01AddProjectAPITestCase.test_case project_roles'] = [
    {
        'description': 'description1',
        'name': 'role1',
        'role_id': 'role_7eb737be-810f-4580-83ea-ff4fa67edd22'
    }
]
