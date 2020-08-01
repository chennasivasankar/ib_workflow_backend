"""
Returns duplicate users exception response as
duplicate user ids has been sent
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase04UpdateCompanyDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        company_id, user_ids = setup
        body = {'name': 'company 1', 'description': 'description 1',
                'logo_url': 'url 1', 'employee_ids': user_ids}
        path_params = {"company_id": company_id}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot)

    @pytest.fixture
    def setup(self, api_user):
        user_id = str(api_user.user_id)
        from ib_iam.tests.factories.models import \
            UserDetailsFactory, CompanyFactory
        UserDetailsFactory.reset_sequence(1)
        CompanyFactory.reset_sequence(1)
        UserDetailsFactory(user_id=user_id, is_admin=True, company=None)
        company_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
        company = CompanyFactory.create(company_id=company_id)
        user_ids = ["2", "3", "2"]
        for user_id in user_ids:
            UserDetailsFactory.create(user_id=user_id, company=company)
        return company_id, user_ids