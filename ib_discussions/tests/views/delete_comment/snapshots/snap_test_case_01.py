# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01DeleteCommentAPITestCase.test_with_invalid_comment_id status_code'] = '404'

snapshots['TestCase01DeleteCommentAPITestCase.test_with_invalid_comment_id body'] = {
    'http_status_code': 404,
    'res_status': 'COMMENT_ID_NOT_FOUND',
    'response': 'Please send valid comment id to delete comment'
}

snapshots['TestCase01DeleteCommentAPITestCase.test_with_user_id_cannot_edit_the_comment status_code'] = '400'

snapshots['TestCase01DeleteCommentAPITestCase.test_with_user_id_cannot_edit_the_comment body'] = {
    'http_status_code': 400,
    'res_status': 'USER_CANNOT_EDIT_COMMENT',
    'response': 'Please send valid user id to comment id to delete comment'
}
