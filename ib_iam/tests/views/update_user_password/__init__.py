# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "update_user_password"
REQUEST_METHOD = "post"
URL_SUFFIX = "update_password/v1/"

from .test_case_01 import TestCase01UpdateUserPasswordAPITestCase
from .test_case_02 import TestCase02UpdateUserPasswordAPITestCase

__all__ = [
    "TestCase01UpdateUserPasswordAPITestCase",
    "TestCase02UpdateUserPasswordAPITestCase"
]
