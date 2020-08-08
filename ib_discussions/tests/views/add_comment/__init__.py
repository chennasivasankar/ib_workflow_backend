# pylint: disable=wrong-import-position

APP_NAME = "ib_discussions"
OPERATION_NAME = "add_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "discussion/{discussion_id}/comment/v1/"

from .test_case_01 import TestCase01AddCommentAPITestCase
from .test_case_02 import TestCase02AddCommentAPITestCase

__all__ = [
    "TestCase01AddCommentAPITestCase",
    "TestCase02AddCommentAPITestCase"
]
