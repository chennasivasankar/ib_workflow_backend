# pylint: disable=wrong-import-position

APP_NAME = "ib_discussions"
OPERATION_NAME = "get_replies_for_comment"
REQUEST_METHOD = "get"
URL_SUFFIX = "comment/{comment_id}/reply/v1/"

from .test_case_01 import TestCase01GetRepliesForCommentAPITestCase

__all__ = [
    "TestCase01GetRepliesForCommentAPITestCase"
]
