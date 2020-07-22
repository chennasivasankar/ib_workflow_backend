# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "add_company"
REQUEST_METHOD = "post"
URL_SUFFIX = "company/add/v1/"

from .test_case_01 import TestCase01AddCompanyAPITestCase

__all__ = [
    "TestCase01AddCompanyAPITestCase"
]
