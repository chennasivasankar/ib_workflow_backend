"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01UpdateCompanyDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['update']}}
    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {'name': 'string', 'description': 'string', 'logo_url': 'string', 'user_ids': ['string']}
        path_params = {"company_id": "413642ff-1272-4990-b878-6607a5e02bc1"}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )