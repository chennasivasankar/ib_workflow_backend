# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_task"
REQUEST_METHOD = "get"
URL_SUFFIX = "task/v1/"

from .test_case_01 import TestCase01GetTaskAPITestCase
from .test_case_02 import TestCase02GetTaskAPITestCase
from .test_case_03 import TestCase03GetTaskAPITestCase
from .test_case_04 import TestCase04GetTaskAPITestCase
from .test_case_05 import TestCase05GetTaskAPITestCase

__all__ = [
    "TestCase01GetTaskAPITestCase",
    "TestCase02GetTaskAPITestCase",
    "TestCase03GetTaskAPITestCase",
    "TestCase04GetTaskAPITestCase",
    "TestCase05GetTaskAPITestCase"
]
