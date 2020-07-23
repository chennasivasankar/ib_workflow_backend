# pylint: disable=wrong-import-position

APP_NAME = "ib_iam"
OPERATION_NAME = "update_company_details"
REQUEST_METHOD = "put"
URL_SUFFIX = "company/{company_id}/v1/"

from .test_case_01 import TestCase01UpdateCompanyDetailsAPITestCase

__all__ = [
    "TestCase01UpdateCompanyDetailsAPITestCase"
]
