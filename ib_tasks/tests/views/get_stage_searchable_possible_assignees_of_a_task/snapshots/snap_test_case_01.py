# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetStageSearchablePossibleAssigneesOfATaskAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetStageSearchablePossibleAssigneesOfATaskAPITestCase.test_case body'] = [
    {
        'id': 'user_id_1',
        'name': 'user_name_1',
        'profile_pic': 'profile_pic_1'
    },
    {
        'id': 'user_id_2',
        'name': 'user_name_2',
        'profile_pic': 'profile_pic_2'
    },
    {
        'id': 'user_id_3',
        'name': 'user_name_3',
        'profile_pic': 'profile_pic_3'
    },
    {
        'id': 'user_id_4',
        'name': 'user_name_4',
        'profile_pic': 'profile_pic_4'
    }
]
