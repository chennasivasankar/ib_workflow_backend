# pylint: disable=wrong-import-position

APP_NAME = "ib_discussions"
OPERATION_NAME = "delete_discussion"
REQUEST_METHOD = "delete"
URL_SUFFIX = "discussion/{discussion_id}/v1/"

from .test_case_01 import TestCase01DeleteDiscussionAPITestCase
from .test_case_02 import TestCase02DeleteDiscussionAPITestCase

__all__ = [
    "TestCase01DeleteDiscussionAPITestCase",
    "TestCase02DeleteDiscussionAPITestCase"
]
