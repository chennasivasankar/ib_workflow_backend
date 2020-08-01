# pylint: disable=wrong-import-position

APP_NAME = "ib_discussions"
OPERATION_NAME = "clarify_discussion"
REQUEST_METHOD = "post"
URL_SUFFIX = "discussion/{discussion_id}/mark_as_clarified/v1/"

from .test_case_01 import TestCase01ClarifyDiscussionAPITestCase
from .test_case_02 import TestCase02ClarifyDiscussionAPITestCase

__all__ = [
    "TestCase01ClarifyDiscussionAPITestCase",
    "TestCase02ClarifyDiscussionAPITestCase"
]
