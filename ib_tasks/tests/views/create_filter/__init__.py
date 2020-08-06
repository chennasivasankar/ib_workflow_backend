# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "create_filter"
REQUEST_METHOD = "post"
URL_SUFFIX = "filters/v1/"

from .test_case_01 import TestCase01CreateFilterAPITestCase

__all__ = [
    "TestCase01CreateFilterAPITestCase"
]
