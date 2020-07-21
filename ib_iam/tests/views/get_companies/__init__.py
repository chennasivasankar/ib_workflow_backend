# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "get_companies"
REQUEST_METHOD = "get"
URL_SUFFIX = "companies/v1/"

from .test_case_01 import TestCase01GetCompaniesAPITestCase

__all__ = [
    "TestCase01GetCompaniesAPITestCase"
]
