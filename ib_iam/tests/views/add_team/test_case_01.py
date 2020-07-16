"""
# TODO: Returns team_id as all the parametes are given properly
"""
from uuid import UUID
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from mock import patch
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01AddTeamAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    @patch("uuid.uuid4")
    def test_case(self, uuid4_mock, snapshot, setup):
        uuid4_mock.return_value = UUID("f2c02d98-f311-4ab2-8673-3daa00757002")
        body = {'name': 'team_name1', 'description': ''}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.fixture()
    def setup(self, api_user):
        user_obj = api_user
        user_id = str(user_obj.id)
        from ib_iam.tests.factories.models import UserFactory
        UserFactory.reset_sequence(1)
        UserFactory.create(user_id=user_id, admin=True)
