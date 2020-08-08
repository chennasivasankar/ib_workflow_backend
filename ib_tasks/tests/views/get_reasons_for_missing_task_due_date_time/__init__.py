# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_reasons_for_missing_task_due_date_time"
REQUEST_METHOD = "get"
URL_SUFFIX = "task/{task_id}/reasons/v1/"

from .test_case_01 import TestCase01GetReasonsForMissingTaskDueDateTimeAPITestCase

__all__ = [
    "TestCase01GetReasonsForMissingTaskDueDateTimeAPITestCase"
]
