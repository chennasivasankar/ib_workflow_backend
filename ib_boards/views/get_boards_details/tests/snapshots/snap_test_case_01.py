# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot

snapshots = Snapshot()

snapshots['TestCase01GetBoardsDetailsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetBoardsDetailsAPITestCase::test_case body'] = {
    'boards_details': [
    ],
    'total_boards_count': 10
}

snapshots['TestCase01GetBoardsDetailsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '45',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'application/json'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}

snapshots[
    'TestCase01GetBoardsDetailsAPITestCase::test_case response'] = b'{"total_boards_count":10,"boards_details":[]}'
