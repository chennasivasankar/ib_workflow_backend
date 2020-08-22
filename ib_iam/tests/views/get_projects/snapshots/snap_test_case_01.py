# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetProjectsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetProjectsAPITestCase.test_case body'] = [
    {
        'description': 'string',
        'logo_url': 'string',
        'name': 'string',
        'project_id': 'string'
    }
]
