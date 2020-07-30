# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_all_tasks_overview"
REQUEST_METHOD = "get"
URL_SUFFIX = "tasks_overview/v1/"

from .test_case_01 import TestCase01GetAllTasksOverviewAPITestCase
from .test_case_02 import TestCase02GetAllTasksOverviewAPITestCase
from .test_case_03 import TestCase03GetAllTasksOverviewAPITestCase

__all__ = [
    "TestCase01GetAllTasksOverviewAPITestCase",
    "TestCase02GetAllTasksOverviewAPITestCase",
    "TestCase03GetAllTasksOverviewAPITestCase"
]
