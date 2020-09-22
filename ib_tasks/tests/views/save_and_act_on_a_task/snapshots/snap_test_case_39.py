# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase38SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase38SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_IMAGE_URL',
    'response': 'Invalid url for an image: image_url.com for field: FIELD_ID-1!'
}

snapshots['TestCase39SaveAndActOnATaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase39SaveAndActOnATaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_IMAGE_URL',
    'response': 'Invalid url for an image: image_url.com for field: FIELD_ID-1!'
}
