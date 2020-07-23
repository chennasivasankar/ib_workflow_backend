# pylint: disable=wrong-import-position

APP_NAME = "ib_discussions"
OPERATION_NAME = "get_discussions"
REQUEST_METHOD = "post"
URL_SUFFIX = "get_discussions/v1/"

from .test_case_01 import TestCase01GetDiscussionsAPITestCase

__all__ = [
    "TestCase01GetDiscussionsAPITestCase"
]
