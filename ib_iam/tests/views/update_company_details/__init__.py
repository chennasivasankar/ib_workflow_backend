# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "update_company_details"
REQUEST_METHOD = "put"
URL_SUFFIX = "company/{company_id}/v1/"

from .test_case_01 import TestCase01UpdateCompanyDetailsAPITestCase
from .test_case_02 import TestCase02UpdateCompanyDetailsAPITestCase
from .test_case_03 import TestCase03UpdateCompanyDetailsAPITestCase
from .test_case_04 import TestCase04UpdateCompanyDetailsAPITestCase
from .test_case_05 import TestCase05UpdateCompanyDetailsAPITestCase
from .test_case_06 import TestCase06UpdateCompanyDetailsAPITestCase

__all__ = [
    "TestCase01UpdateCompanyDetailsAPITestCase",
    "TestCase02UpdateCompanyDetailsAPITestCase",
    "TestCase03UpdateCompanyDetailsAPITestCase",
    "TestCase04UpdateCompanyDetailsAPITestCase",
    "TestCase05UpdateCompanyDetailsAPITestCase",
    "TestCase06UpdateCompanyDetailsAPITestCase"
]
