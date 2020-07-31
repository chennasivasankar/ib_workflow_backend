# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "get_users"
REQUEST_METHOD = "get"
URL_SUFFIX = "users/v1/"

from .test_case_01 import TestCase01GetUsersAPITestCase
from .test_case_03 import TestCase03GetUsersAPITestCase

__all__ = [
    "TestCase01GetUsersAPITestCase",
    "TestCase03GetUsersAPITestCase"
]
