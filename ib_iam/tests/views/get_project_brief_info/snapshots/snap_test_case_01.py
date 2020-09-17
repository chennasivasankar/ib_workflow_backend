# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase01GetProjectBriefInfoAPITestCase.test_with_valid_details_return_response status_code'] = '200'

snapshots['TestCase01GetProjectBriefInfoAPITestCase.test_with_valid_details_return_response body'] = {
    'projects': [
        {
            'logo_url': 'http://sample.com',
            'name': 'name 1',
            'project_display_id': 'display_id 1',
            'project_id': '641bfcc5-e1ea-4231-b482-f7f34fb5c7c4'
        },
        {
            'logo_url': 'http://sample.com',
            'name': 'name 2',
            'project_display_id': 'display_id 2',
            'project_id': '641bfcc5-e1ea-4231-b482-f7f34fb5c7c5'
        }
    ]
}
