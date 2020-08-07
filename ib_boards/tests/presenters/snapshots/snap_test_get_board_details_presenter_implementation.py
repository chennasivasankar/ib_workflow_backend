# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    'TestGetBoardsDetailsPresenterImplementation.test_get_response_for_board_details board_details'] = [
    {
        'board_id': 'BOARD_ID_1',
        'name': 'BOARD_DISPLAY_NAME'
    },
    {
        'board_id': 'BOARD_ID_2',
        'name': 'BOARD_DISPLAY_NAME'
    },
    {
        'board_id': 'BOARD_ID_3',
        'name': 'BOARD_DISPLAY_NAME'
    }
]
