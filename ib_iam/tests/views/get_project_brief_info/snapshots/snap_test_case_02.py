# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetProjectBriefInfoAPITestCase.test_with_user_does_not_exist_return_response status_code'] = '400'

snapshots['TestCase01GetProjectBriefInfoAPITestCase.test_with_user_does_not_exist_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'USER_DOES_NOT_EXIST',
    'response': 'Please access with valid user, to get access for project'
}
