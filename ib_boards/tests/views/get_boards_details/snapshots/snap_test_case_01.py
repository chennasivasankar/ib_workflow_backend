# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetBoardsDetailsAPITestCase.test_case status_code'] = '200'

snapshots['TestCase01GetBoardsDetailsAPITestCase.test_case body'] = {
    'boards_details': [
        {
            'board_id': 'BOARD_ID_11',
            'name': 'BOARD_DISPLAY_NAME'
        },
        {
            'board_id': 'BOARD_ID_2',
            'name': 'BOARD_DISPLAY_NAME'
        },
        {
            'board_id': 'BOARD_ID_3',
            'name': 'BOARD_DISPLAY_NAME'
        },
        {
            'board_id': 'BOARD_ID_4',
            'name': 'BOARD_DISPLAY_NAME'
        },
        {
            'board_id': 'BOARD_ID_5',
            'name': 'BOARD_DISPLAY_NAME'
        },
        {
            'board_id': 'BOARD_ID_6',
            'name': 'BOARD_DISPLAY_NAME'
        }
    ],
    'total_boards_count': 11
}
