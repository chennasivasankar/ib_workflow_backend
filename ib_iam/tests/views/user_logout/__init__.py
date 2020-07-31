# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "user_logout"
REQUEST_METHOD = "post"
URL_SUFFIX = "logout/v1/"

from .test_case_01 import TestCase01UserLogoutAPITestCase

__all__ = [
    "TestCase01UserLogoutAPITestCase"
]
