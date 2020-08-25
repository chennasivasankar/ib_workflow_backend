# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetTaskRpsInGivenStageAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetTaskRpsInGivenStageAPITestCase.test_case body'] = [
    {
        'name': 'user_name_1',
        'profile_pic_url': None,
        'user_id': '123e4567-e89b-12d3-a456-426614174001'
    },
    {
        'name': 'user_name_2',
        'profile_pic_url': None,
        'user_id': '123e4567-e89b-12d3-a456-426614174002'
    }
]
