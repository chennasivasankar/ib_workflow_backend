# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_tasks_to_search"
REQUEST_METHOD = "get"
URL_SUFFIX = "tasks/search/v1/"

from .test_case_01 import TestCase01GetTasksToSearchAPITestCase

__all__ = [
    "TestCase01GetTasksToSearchAPITestCase"
]
