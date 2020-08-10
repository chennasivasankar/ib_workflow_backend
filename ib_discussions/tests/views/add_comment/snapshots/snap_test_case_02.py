# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02AddCommentAPITestCase.test_discussion_id_not_found_return_response status_code'] = '404'

snapshots['TestCase02AddCommentAPITestCase.test_discussion_id_not_found_return_response body'] = {
    'http_status_code': 404,
    'res_status': 'DISCUSSION_ID_NOT_FOUND',
    'response': 'Please send valid discussion id to create comment for discussion'
}
