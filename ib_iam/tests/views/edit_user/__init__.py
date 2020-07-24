# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "edit_user"
REQUEST_METHOD = "put"
URL_SUFFIX = "users/{user_id}/v1/"

from .test_case_01 import TestCase01EditUserAPITestCase
from .test_case_02 import TestCase02EditUserAPITestCase
from .test_case_03 import TestCase03EditUserAPITestCase
from .test_case_04 import TestCase04EditUserAPITestCase
from .test_case_05 import TestCase05EditUserAPITestCase
from .test_case_06 import TestCase06EditUserAPITestCase

__all__ = [
    "TestCase01EditUserAPITestCase",
    "TestCase02EditUserAPITestCase",
    "TestCase03EditUserAPITestCase",
    "TestCase04EditUserAPITestCase",
    "TestCase05EditUserAPITestCase",
    "TestCase06EditUserAPITestCase"
]
