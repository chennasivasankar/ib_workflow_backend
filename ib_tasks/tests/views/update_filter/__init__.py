# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "update_filter"
REQUEST_METHOD = "put"
URL_SUFFIX = "filters/{filter_id}/v1/"

from .test_case_01 import TestCase01UpdateFilterAPITestCase

__all__ = [
    "TestCase01UpdateFilterAPITestCase"
]
