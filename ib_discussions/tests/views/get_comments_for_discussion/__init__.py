# pylint: disable=wrong-import-position

APP_NAME = "ib_discussions"
OPERATION_NAME = "get_comments_for_discussion"
REQUEST_METHOD = "get"
URL_SUFFIX = "discussion/{discussion_id}/comment/v1/"

from .test_case_01 import TestCase01GetCommentsForDiscussionAPITestCase

__all__ = [
    "TestCase01GetCommentsForDiscussionAPITestCase"
]
