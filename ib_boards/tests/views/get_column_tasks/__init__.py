# pylint: disable=wrong-import-position

APP_NAME = "ib_boards"
OPERATION_NAME = "get_column_tasks"
REQUEST_METHOD = "post"
URL_SUFFIX = "columns/{column_id}/tasks/v1/"

from .test_case_01 import TestCase01GetColumnTasksAPITestCase

__all__ = [
    "TestCase01GetColumnTasksAPITestCase"
]
