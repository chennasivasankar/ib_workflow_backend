# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "update_task"
REQUEST_METHOD = "put"
URL_SUFFIX = "task/v1/"

from .test_case_01 import TestCase01UpdateTaskAPITestCase

__all__ = [
    "TestCase01UpdateTaskAPITestCase"
]
