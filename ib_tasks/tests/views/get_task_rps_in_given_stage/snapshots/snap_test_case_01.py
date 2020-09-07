# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetTaskRpsInGivenStageAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetTaskRpsInGivenStageAPITestCase.test_case body'] = [
    {
        'name': 'user_name_51',
        'profile_pic_url': 'profile_pic_51',
        'user_id': '123e4567-e89b-12d3-a456-4266141740051'
    },
    {
        'name': 'user_name_52',
        'profile_pic_url': 'profile_pic_52',
        'user_id': '123e4567-e89b-12d3-a456-4266141740052'
    }
]
