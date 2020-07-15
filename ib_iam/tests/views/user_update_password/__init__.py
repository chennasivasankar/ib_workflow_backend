# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "user_update_password"
REQUEST_METHOD = "post"
URL_SUFFIX = "update_password/v1/"

from .test_case_01 import TestCase01UserUpdatePasswordAPITestCase

__all__ = [
    "TestCase01UserUpdatePasswordAPITestCase"
]
