# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr

snapshots = Snapshot()

snapshots['TestCase01GetColumnTasksAPITestCase::test_case status'] = 404

snapshots['TestCase01GetColumnTasksAPITestCase::test_case body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_COLUMN_ID',
    'response': 'column id is invalid'
}

snapshots['TestCase01GetColumnTasksAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '91',
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
    'TestCase01GetColumnTasksAPITestCase::test_case response'] = GenericRepr(
    "<Response status_code=404, "
application / json
">")
