# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase31CreateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase31CreateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_IMAGE_FORMAT',
    'response': "Invalid format for an image: .mp4 for field: DISPLAY_NAME-0! Try with these formats: ['.jpg', '.png']"
}
