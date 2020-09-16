"""
Invalid cases of get users
1. User is not admin
2. Invalid limit value
3. Invalid offset value
4. Invalid user_id
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

USER_ID = '7e39bf1c-f9a5-4e76-8451-b962ddd520fc'


class TestCase01GetUsersAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture
    def set_up_for_not_admin_user(self, api_user):
        user_id = api_user.user_id
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_user_details_factory
        reset_sequence_user_details_factory()
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.create(
            user_id=user_id, is_admin=False, company=None
        )

    @pytest.fixture
    def set_up_for_admin_user(self, api_user):
        user_id = api_user.user_id
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_user_details_factory
        reset_sequence_user_details_factory()
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.create(user_id=user_id, is_admin=True,
                                  company=None)

    @pytest.mark.django_db
    def test_given_user_is_not_admin_returns_user_has_no_access_response(
            self, set_up_for_not_admin_user, snapshot
    ):
        body = {}
        path_params = {}
        query_params = {'offset': 0, 'limit': 10, 'search_query': ''}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_given_invalid_limit_returns_invalid_limit_response(
            self, set_up_for_admin_user, snapshot
    ):
        body = {}
        path_params = {}
        query_params = {'offset': 0, 'limit': -1, 'search_query': ''}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_given_invalid_offset_returns_invalid_offset_response(
            self, set_up_for_admin_user, snapshot
    ):
        body = {}
        path_params = {}
        query_params = {'offset': -1, 'limit': 10, 'search_query': ''}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
