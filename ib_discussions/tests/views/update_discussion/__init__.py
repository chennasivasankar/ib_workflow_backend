# pylint: disable=wrong-import-position

APP_NAME = "ib_discussions"
OPERATION_NAME = "update_discussion"
REQUEST_METHOD = "post"
URL_SUFFIX = "discussion/{discussion_id}/update/v1/"

from .test_case_01 import TestCase01UpdateDiscussionAPITestCase
from .test_case_02 import TestCase02UpdateDiscussionAPITestCase

__all__ = [
    "TestCase01UpdateDiscussionAPITestCase",
    "TestCase02UpdateDiscussionAPITestCase"
]
