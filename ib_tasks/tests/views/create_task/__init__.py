# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "create_task"
REQUEST_METHOD = "post"
URL_SUFFIX = "task/v1/"

from .test_case_01 import TestCase01CreateTaskAPITestCase
from .test_case_02 import TestCase02CreateTaskAPITestCase
from .test_case_03 import TestCase03CreateTaskAPITestCase
from .test_case_04 import TestCase04CreateTaskAPITestCase
from .test_case_05 import TestCase05CreateTaskAPITestCase
from .test_case_06 import TestCase06CreateTaskAPITestCase
from .test_case_07 import TestCase07CreateTaskAPITestCase
from .test_case_08 import TestCase08CreateTaskAPITestCase
from .test_case_09 import TestCase09CreateTaskAPITestCase
from .test_case_10 import TestCase10CreateTaskAPITestCase

__all__ = [
    "TestCase01CreateTaskAPITestCase",
    "TestCase02CreateTaskAPITestCase",
    "TestCase03CreateTaskAPITestCase",
    "TestCase04CreateTaskAPITestCase",
    "TestCase05CreateTaskAPITestCase",
    "TestCase06CreateTaskAPITestCase",
    "TestCase07CreateTaskAPITestCase",
    "TestCase08CreateTaskAPITestCase",
    "TestCase09CreateTaskAPITestCase",
    "TestCase10CreateTaskAPITestCase"
]
