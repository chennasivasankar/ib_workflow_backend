# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots[
    'TestGetBoardsPresenterImplementation.test_get_response_for_get_boards boards'] = {
    'boards_details': [
        {
            'board_id': 'BOARD_ID_7',
            'name': 'BOARD_DISPLAY_NAME'
        },
        {
            'board_id': 'BOARD_ID_8',
            'name': 'BOARD_DISPLAY_NAME'
        },
        {
            'board_id': 'BOARD_ID_9',
            'name': 'BOARD_DISPLAY_NAME'
        }
    ],
    'total_boards_count': 3
}
