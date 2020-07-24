# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "add_user"
REQUEST_METHOD = "post"
URL_SUFFIX = "users/create/v1/"

from .test_case_01 import TestCase01AddUserAPITestCase
from .test_case_02 import TestCase02AddUserAPITestCase
from .test_case_03 import TestCase03AddUserAPITestCase

__all__ = [
    "TestCase01AddUserAPITestCase",
    "TestCase02AddUserAPITestCase",
    "TestCase03AddUserAPITestCase"
]
