# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "delete_todo"
REQUEST_METHOD = "delete"
URL_SUFFIX = "todos/{id}/"

from .test_case_01 import TestCase01DeleteTodoAPITestCase

__all__ = [
    "TestCase01DeleteTodoAPITestCase"
]
