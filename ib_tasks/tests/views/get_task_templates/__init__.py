# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_task_templates"
REQUEST_METHOD = "get"
URL_SUFFIX = "task_templates/v1/"

from .test_case_01 import TestCase01GetTaskTemplatesAPITestCase
from .test_case_02 import TestCase02GetTaskTemplatesAPITestCase
from .test_case_03 import TestCase03GetTaskTemplatesAPITestCase
from .test_case_04 import TestCase04GetTaskTemplatesAPITestCase
from .test_case_05 import TestCase05GetTaskTemplatesAPITestCase
from .test_case_06 import TestCase06GetTaskTemplatesAPITestCase
from .test_case_07 import TestCase07GetTaskTemplatesAPITestCase
from .test_case_08 import TestCase08GetTaskTemplatesAPITestCase
from .test_case_09 import TestCase09GetTaskTemplatesAPITestCase

__all__ = [
    "TestCase01GetTaskTemplatesAPITestCase",
    "TestCase02GetTaskTemplatesAPITestCase",
    "TestCase03GetTaskTemplatesAPITestCase",
    "TestCase04GetTaskTemplatesAPITestCase",
    "TestCase05GetTaskTemplatesAPITestCase",
    "TestCase06GetTaskTemplatesAPITestCase",
    "TestCase07GetTaskTemplatesAPITestCase",
    "TestCase08GetTaskTemplatesAPITestCase",
    "TestCase09GetTaskTemplatesAPITestCase"
]
