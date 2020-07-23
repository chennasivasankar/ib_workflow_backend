"""
Deletes a company as valid parameters are given
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01DeleteCompanyAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['delete']}}

    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        company_id = setup
        body = {}
        path_params = {"company_id": company_id}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.fixture
    def setup(self, api_user):
        user_id = api_user.id
        company_id = "413642ff-1272-4990-b878-6607a5e02bc1"
        # TODO After storage and factory implementation for company related \
        #  models check this out
        # from ib_iam.tests.factories import CompanyFactory, UserDetailsFactory
        # UserDetailsFactory.reset_sequence(1)
        # CompanyFactory.reset_sequence(1)
        # UserDetailsFactory.create(user_id=user_id, is_admin=True)
        # CompanyFactory.create(company_id=company_id)
        # return company_id
