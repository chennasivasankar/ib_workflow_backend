"""
Gives all available companies if accessed by an admin
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ib_iam.tests.common_fixtures.adapters.user_service_mocks import (
    prepare_user_profile_dtos_mock)


class TestCase01GetCompaniesAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, mocker, setup, snapshot):
        employee_ids = [
            '2bdb417e-4632-419a-8ddd-085ea272c6eb',
            '548a803c-7b48-47ba-a700-24f2ea0d1280',
            '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
            '7ee2c7b4-34c8-4d65-a83a-f87da75db24e']
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        UserProfileDTOFactory.reset_sequence(1)
        mock = prepare_user_profile_dtos_mock(mocker)
        mock.return_value = [
            UserProfileDTOFactory(user_id=employee_id)
            for employee_id in employee_ids
        ]
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
        user_id = str(api_user.user_id)
        from ib_iam.tests.factories.models import \
            UserDetailsFactory, CompanyFactory
        UserDetailsFactory.reset_sequence(1)
        UserDetailsFactory.create(user_id=user_id, is_admin=True, company=None)
        companies = [
            {
                "company_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
                "employees_ids": ['2bdb417e-4632-419a-8ddd-085ea272c6eb',
                                  '548a803c-7b48-47ba-a700-24f2ea0d1280',
                                  '4b8fb6eb-fa7d-47c1-8726-cd917901104e']
            },
            {
                "company_id": "aa66c40f-6d93-484a-b418-984716514c7b",
                "employees_ids": ['2bdb417e-4632-419a-8ddd-085ea272c6eb',
                                  '7ee2c7b4-34c8-4d65-a83a-f87da75db24e']
            }
        ]
        CompanyFactory.reset_sequence(1)
        for company in companies:
            company_object = CompanyFactory.create(
                company_id=company["company_id"])
            for employee_id in company["employees_ids"]:
                UserDetailsFactory(user_id=employee_id, company=company_object)
