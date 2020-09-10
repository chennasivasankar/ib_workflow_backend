# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase12GetTaskAPITestCase.test_case status_code'] = '404'

snapshots['TestCase12GetTaskAPITestCase.test_case body'] = {
    'http_status_code': 404,
    'res_status': 'USERS_NOT_EXISTS_FOR_TEAMS',
    'response': "users = ['user1', 'user2'] not exists for teams"
}
