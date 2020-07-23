# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "add_company"
REQUEST_METHOD = "post"
URL_SUFFIX = "company/add/v1/"

from .test_case_01 import TestCase01AddCompanyAPITestCase
from .test_case_02 import TestCase02AddCompanyAPITestCase
from .test_case_03 import TestCase03AddCompanyAPITestCase
from .test_case_04 import TestCase04AddCompanyAPITestCase
from .test_case_05 import TestCase05AddCompanyAPITestCase

__all__ = [
    "TestCase01AddCompanyAPITestCase",
    "TestCase02AddCompanyAPITestCase",
    "TestCase03AddCompanyAPITestCase",
    "TestCase04AddCompanyAPITestCase",
    "TestCase05AddCompanyAPITestCase"
]
