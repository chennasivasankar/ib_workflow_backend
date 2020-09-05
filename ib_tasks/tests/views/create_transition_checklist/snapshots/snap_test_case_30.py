# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase30CreateTransitionChecklistAPITestCase.test_case status_code'] = '400'

snapshots['TestCase30CreateTransitionChecklistAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_IMAGE_FORMAT',
    'response': "Invalid format for an image: .mp4 for field: field_1! Try with these formats: ['.jpg', '.jpeg']"
}
