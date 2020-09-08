"""
# Returns company_id as valid parameters are given
"""
from uuid import UUID

import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ib_iam.tests.common_fixtures.adapters.uuid_mock import prepare_uuid_mock


class TestCase01AddCompanyAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, mocker, snapshot, setup):
        mock = prepare_uuid_mock(mocker)
        mock.return_value = UUID("f2c02d98-f311-4ab2-8673-3daa00757002")
        body = {'name': 'string', 'description': 'string', 'logo_url': 'string', 'employee_ids': ["2", "3"]}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
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
        for user_id in ["2", "3"]:
            UserFactory.create(user_id=user_id)
