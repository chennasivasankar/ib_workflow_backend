# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetStageSearchablePossibleAssigneesOfATaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetStageSearchablePossibleAssigneesOfATaskAPITestCase.test_case body'] = [
    {
        'id': 'user_id_0',
        'name': 'name_0',
        'profile_pic_url': 'pic_url'
    },
    {
        'id': 'user_id_1',
        'name': 'name_1',
        'profile_pic_url': 'pic_url'
    },
    {
        'id': 'user_id_2',
        'name': 'name_2',
        'profile_pic_url': 'pic_url'
    },
    {
        'id': 'user_id_3',
        'name': 'name_3',
        'profile_pic_url': 'pic_url'
    }
]
