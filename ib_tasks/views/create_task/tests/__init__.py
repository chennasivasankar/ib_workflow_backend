# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "create_task"
REQUEST_METHOD = "post"
URL_SUFFIX = "task/v1/"

from .test_case_01 import TestCase01CreateTaskAPITestCase

__all__ = [
    "TestCase01CreateTaskAPITestCase"
]
