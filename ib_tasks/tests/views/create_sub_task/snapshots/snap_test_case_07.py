# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase07CreateSubTaskAPITestCase.test_case status_code'] = '400'

snapshots['TestCase07CreateSubTaskAPITestCase.test_case body'] = {
    'http_status_code': 400,
    'res_status': 'INVALID_PROJECT_TEMPLATE',
    'response': 'template_1 is not valid template for given project project_1'
}
