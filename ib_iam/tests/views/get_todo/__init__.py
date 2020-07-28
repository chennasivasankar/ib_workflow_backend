# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "get_todo"
REQUEST_METHOD = "get"
URL_SUFFIX = "todos/{id}/"

from .test_case_01 import TestCase01GetTodoAPITestCase

__all__ = [
    "TestCase01GetTodoAPITestCase"
]
