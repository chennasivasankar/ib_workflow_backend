# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "delete_company"
REQUEST_METHOD = "delete"
URL_SUFFIX = "company/{company_id}/v1/"

from .test_case_01 import TestCase01DeleteCompanyAPITestCase
from .test_case_02 import TestCase02DeleteCompanyAPITestCase
from .test_case_03 import TestCase03DeleteCompanyAPITestCase

__all__ = [
    "TestCase01DeleteCompanyAPITestCase",
    "TestCase02DeleteCompanyAPITestCase",
    "TestCase03DeleteCompanyAPITestCase"
]
