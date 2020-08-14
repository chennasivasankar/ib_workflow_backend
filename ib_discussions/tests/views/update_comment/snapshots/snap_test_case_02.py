# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UpdateCommentAPITestCase.test_with_user_cannot_edit_for_given_comment_id status_code'] = '400'

snapshots['TestCase02UpdateCommentAPITestCase.test_with_user_cannot_edit_for_given_comment_id body'] = {
    'http_status_code': 400,
    'res_status': 'USER_CANNOT_UPDATE_COMMENT',
    'response': 'Please send valid user id to comment id to update comment'
}

snapshots['TestCase02UpdateCommentAPITestCase.test_with_comment_id_not_found status_code'] = '404'

snapshots['TestCase02UpdateCommentAPITestCase.test_with_comment_id_not_found body'] = {
    'http_status_code': 404,
    'res_status': 'COMMENT_ID_NOT_FOUND',
    'response': 'Please send valid comment id to update comment'
}
