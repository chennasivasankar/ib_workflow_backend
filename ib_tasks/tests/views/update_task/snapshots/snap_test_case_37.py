# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase37UpdateTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase37UpdateTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_IMAGE_URL',
    'response': 'Invalid url for an image: image_url.com for field: FIELD-1!'
}
