# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "create_todo"
REQUEST_METHOD = "post"
URL_SUFFIX = "todos/"

from .test_case_01 import TestCase01CreateTodoAPITestCase

__all__ = [
    "TestCase01CreateTodoAPITestCase"
]
