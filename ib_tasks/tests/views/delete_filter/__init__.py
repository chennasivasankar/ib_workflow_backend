# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "delete_filter"
REQUEST_METHOD = "delete"
URL_SUFFIX = "filters/{filter_id}/v1/"

from .test_case_01 import TestCase01DeleteFilterAPITestCase

__all__ = [
    "TestCase01DeleteFilterAPITestCase"
]
