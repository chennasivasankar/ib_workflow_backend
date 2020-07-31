# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "update_todo"
REQUEST_METHOD = "put"
URL_SUFFIX = "todos/{id}/"

from .test_case_01 import TestCase01UpdateTodoAPITestCase

__all__ = [
    "TestCase01UpdateTodoAPITestCase"
]
