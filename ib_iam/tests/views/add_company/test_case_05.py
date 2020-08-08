"""
Raises InvalidMembers exception as
as we send invalid member ids(not user ids)
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase05AddCompanyAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {'name': 'company1', 'description': '', 'logo_url': 'string', 'employee_ids': ["2", "3"]}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.fixture()
    def setup(self, api_user):
        user_obj = api_user
        user_id = str(user_obj.user_id)
        from ib_iam.tests.factories.models import UserFactory
        UserFactory.reset_sequence(1)
        UserFactory.create(user_id=user_id, is_admin=True)
        UserFactory.create(user_id="2")
