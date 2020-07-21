# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "get_list_of_companies"
REQUEST_METHOD = "get"
URL_SUFFIX = "companies/"

from .test_case_01 import TestCase01GetListOfCompaniesAPITestCase

__all__ = [
    "TestCase01GetListOfCompaniesAPITestCase"
]
