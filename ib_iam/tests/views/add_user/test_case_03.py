"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase03AddUserAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture
    def user_set_up(self, api_user):
        user_id = api_user.user_id
        from ib_iam.tests.factories.models import UserDetailsFactory
        user = UserDetailsFactory.create(user_id=user_id, is_admin=True)
        from ib_iam.tests.factories.models \
            import CompanyFactory, TeamFactory, RoleFactory
        CompanyFactory.create(company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331')
        TeamFactory.create(team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331')
        RoleFactory.create(role_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331')

    @pytest.mark.django_db
    def test_case(self, user_set_up, snapshot):
        body = {'name': 'parker', 'email': 'parker@string.com',
                'company_id': 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                'team_ids': ['ef6d1fc6-ac3f-4d2d-a983-752c992e8331'],
                'role_ids': ['ef6d1fc6-ac3f-4d2d-a983-752c992e8331']}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
