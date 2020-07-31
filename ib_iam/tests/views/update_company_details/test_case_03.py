"""
# Returns invalid company exception response as the company does not exists
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase03UpdateCompanyDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        company_id = setup
        body = {'name': 'company 1', 'description': 'description 1', 'logo_url': 'url 1', 'employee_ids': ["2", "3"]}
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
        return company_id

