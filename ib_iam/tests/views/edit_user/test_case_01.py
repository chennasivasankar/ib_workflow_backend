"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01EditUserAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture
    def user_set_up(self, api_user):
        user_id = api_user.user_id
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_user_details_factory
        reset_sequence_user_details_factory()
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.create(user_id=user_id, is_admin=False, company=None)

    @pytest.mark.django_db
    def test_case(self, user_set_up, snapshot):
        body = {'name': 'parker', 'email': 'parker2020@gmail.com',
                'company_id': 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                'team_ids': ['ef6d1fc6-ac3f-4d2d-a983-752c992e8344',
                             'ef6d1fc6-ac3f-4d2d-a983-752c992e8343'],
                'role_ids': ['ROLE_1']}
        path_params = {"user_id": "ef6d1fc6-ac3f-4d2d-a983-752c992e8300"}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )