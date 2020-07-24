# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_searchable_values"
REQUEST_METHOD = "get"
URL_SUFFIX = "field_search/v1/"

from .test_case_01 import TestCase01GetSearchableValuesAPITestCase

__all__ = [
    "TestCase01GetSearchableValuesAPITestCase"
]
