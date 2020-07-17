# pylint: disable=wrong-import-position

APP_NAME = "ib_discussions"
OPERATION_NAME = "create_discussion"
REQUEST_METHOD = "post"
URL_SUFFIX = "discussions/v1/"

from .test_case_01 import TestCase01CreateDiscussionAPITestCase

__all__ = [
    "TestCase01CreateDiscussionAPITestCase"
]
