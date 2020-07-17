# pylint: disable=wrong-import-position

APP_NAME = "ib_discussions"
OPERATION_NAME = "get_discussions"
REQUEST_METHOD = "get"
URL_SUFFIX = "discussions/v1/"

from .test_case_01 import TestCase01GetDiscussionsAPITestCase

__all__ = [
    "TestCase01GetDiscussionsAPITestCase"
]
