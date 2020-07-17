# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "get_todos"
REQUEST_METHOD = "get"
URL_SUFFIX = "todos/"

from .test_case_01 import TestCase01GetTodosAPITestCase

__all__ = [
    "TestCase01GetTodosAPITestCase"
]
