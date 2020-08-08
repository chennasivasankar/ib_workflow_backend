# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "select_filter"
REQUEST_METHOD = "put"
URL_SUFFIX = "filter/select/v1/"

from .test_case_01 import TestCase01SelectFilterAPITestCase

__all__ = [
    "TestCase01SelectFilterAPITestCase"
]
