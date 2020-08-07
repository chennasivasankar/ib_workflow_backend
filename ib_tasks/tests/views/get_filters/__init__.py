# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_filters"
REQUEST_METHOD = "get"
URL_SUFFIX = "filters/v1/"

from .test_case_01 import TestCase01GetFiltersAPITestCase

__all__ = [
    "TestCase01GetFiltersAPITestCase"
]
