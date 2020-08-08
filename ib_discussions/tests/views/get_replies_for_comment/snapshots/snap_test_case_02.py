# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetRepliesForCommentAPITestCase.test_comment_id_not_found_return_response status_code'] = '404'

snapshots['TestCase01GetRepliesForCommentAPITestCase.test_comment_id_not_found_return_response body'] = {
    'http_status_code': 404,
    'res_status': 'COMMENT_ID_NOT_FOUND',
    'response': 'Please send valid comment id to get replies for comment'
}
