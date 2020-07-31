# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "delete_user"
REQUEST_METHOD = "delete"
URL_SUFFIX = "users/{user_id}/v1/"

from .test_case_01 import TestCase01DeleteUserAPITestCase
from .test_case_02 import TestCase02DeleteUserAPITestCase

__all__ = [
    "TestCase01DeleteUserAPITestCase",
    "TestCase02DeleteUserAPITestCase"
]
