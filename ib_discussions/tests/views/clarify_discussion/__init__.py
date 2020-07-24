# pylint: disable=wrong-import-position

APP_NAME = "ib_discussions"
OPERATION_NAME = "clarify_discussion"
REQUEST_METHOD = "post"
URL_SUFFIX = "discussion/{discussion_id}/mark_as_clarified/v1/"

from .test_case_01 import TestCase01ClarifyDiscussionAPITestCase

__all__ = [
    "TestCase01ClarifyDiscussionAPITestCase"
]
