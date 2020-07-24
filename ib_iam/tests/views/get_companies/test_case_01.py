"""
Gives all available companies if accessed by an admin
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetCompaniesAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.fixture
    def setup(self, api_user):
        user_id = str(api_user.id)
        from ib_iam.tests.factories.models import \
            UserDetailsFactory, CompanyFactory
        UserDetailsFactory.reset_sequence(1)
        UserDetailsFactory.create(user_id=user_id, is_admin=True)
        CompanyFactory.reset_sequence(1)
        company_objects = CompanyFactory.create_batch(size=2)
        for company_object in company_objects:
            UserDetailsFactory.create_batch(size=2, company=company_object)
        UserDetailsFactory.create_batch(size=1, company=company_objects[0])

