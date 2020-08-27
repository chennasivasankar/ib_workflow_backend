# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02AddSpecificProjectDetailsAPITestCase.test_with_invalid_user_ids_for_project status_code'] = '400'

snapshots['TestCase02AddSpecificProjectDetailsAPITestCase.test_with_invalid_user_ids_for_project body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_USER_IDS_FOR_PROJECT',
    'response': "Please send valid user ids for project, invalid user ids are [UUID('11be920b-7b4c-49e7-8adb-41a0c18da848'), UUID('01be920b-7b4c-49e7-8adb-41a0c18da848'), UUID('77be920b-7b4c-49e7-8adb-41a0c18da848')]"
}
