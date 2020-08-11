# pylint: disable=wrong-import-position

APP_NAME = "ib_tasks"
OPERATION_NAME = "get_searchable_values"
REQUEST_METHOD = "get"
URL_SUFFIX = "field_search/v1/"

from .test_case_01 import TestCase01GetSearchableValuesAPITestCase
from .test_case_02 import TestCase02GetSearchableValuesAPITestCase
from .test_case_03 import TestCase03GetSearchableValuesAPITestCase

__all__ = [
    "TestCase01GetSearchableValuesAPITestCase",
    "TestCase02GetSearchableValuesAPITestCase",
    "TestCase03GetSearchableValuesAPITestCase"
]
