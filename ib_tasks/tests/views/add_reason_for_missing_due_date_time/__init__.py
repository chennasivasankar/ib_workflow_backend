# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "add_reason_for_missing_due_date_time"
REQUEST_METHOD = "post"
URL_SUFFIX = "task/{task_id}/reasons/v1/"

from .test_case_01 import TestCase01AddReasonForMissingDueDateTimeAPITestCase

__all__ = [
    "TestCase01AddReasonForMissingDueDateTimeAPITestCase"
]
