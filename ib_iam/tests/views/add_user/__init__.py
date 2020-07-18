# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "add_user"
REQUEST_METHOD = "post"
URL_SUFFIX = "add_user/v1/"

from .test_case_01 import TestCase01AddUserAPITestCase

__all__ = [
    "TestCase01AddUserAPITestCase"
]
