# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetProjectsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetProjectsAPITestCase.test_case body'] = [
    {
        'description': 'description 1',
        'logo_url': 'logo 1',
        'name': 'name 1',
        'project_id': '641bfcc5-e1ea-4231-b482-f7f34fb5c7c4'
    },
    {
        'description': 'description 2',
        'logo_url': 'logo 2',
        'name': 'name 2',
        'project_id': '641bfcc5-e1ea-4231-b482-f7f34fb5c7c5'
    }
]
