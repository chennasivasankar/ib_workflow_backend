# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "user_login"
REQUEST_METHOD = "post"
URL_SUFFIX = "login/v1/"

from .test_case_01 import TestCase01UserLoginAPITestCase
from .test_case_02 import TestCase02UserLoginAPITestCase
from .test_case_03 import TestCase03UserLoginAPITestCase

__all__ = [
    "TestCase01UserLoginAPITestCase",
    "TestCase02UserLoginAPITestCase",
    "TestCase03UserLoginAPITestCase"
]
