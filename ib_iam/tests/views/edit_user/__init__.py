# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "edit_user"
REQUEST_METHOD = "put"
URL_SUFFIX = "users/{user_id}/v1/"

from .test_case_01 import TestCase01EditUserAPITestCase
from .test_case_02 import TestCase02EditUserAPITestCase

__all__ = [
    "TestCase01EditUserAPITestCase",
    "TestCase02EditUserAPITestCase"
]
