# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "update_task"
REQUEST_METHOD = "put"
URL_SUFFIX = "task/v1/"

from .test_case_01 import TestCase01UpdateTaskAPITestCase
from .test_case_013 import TestCase013UpdateTaskAPITestCase
from .test_case_02 import TestCase02UpdateTaskAPITestCase
from .test_case_03 import TestCase03UpdateTaskAPITestCase
from .test_case_05 import TestCase05UpdateTaskAPITestCase
from .test_case_06 import TestCase06UpdateTaskAPITestCase
from .test_case_07 import TestCase07UpdateTaskAPITestCase
from .test_case_08 import TestCase08UpdateTaskAPITestCase
from .test_case_09 import TestCase09UpdateTaskAPITestCase
from .test_case_14 import TestCase14UpdateTaskAPITestCase

__all__ = [
    "TestCase01UpdateTaskAPITestCase",
    "TestCase013UpdateTaskAPITestCase",
    "TestCase02UpdateTaskAPITestCase",
    "TestCase03UpdateTaskAPITestCase",
    "TestCase05UpdateTaskAPITestCase",
    "TestCase06UpdateTaskAPITestCase",
    "TestCase07UpdateTaskAPITestCase",
    "TestCase08UpdateTaskAPITestCase",
    "TestCase09UpdateTaskAPITestCase",
    "TestCase14UpdateTaskAPITestCase"
]
