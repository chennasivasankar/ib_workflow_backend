# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "perform_task_action"
REQUEST_METHOD = "post"
URL_SUFFIX = "boards/{board_id}/tasks/{task_id}/actions/{action_id}/v1/"

from .test_case_01 import TestCase01PerformTaskActionAPITestCase
from .test_case_02 import TestCase02PerformTaskActionAPITestCase
from .test_case_03 import TestCase03PerformTaskActionAPITestCase

__all__ = [
    "TestCase01PerformTaskActionAPITestCase",
    "TestCase02PerformTaskActionAPITestCase",
    "TestCase03PerformTaskActionAPITestCase"
]
