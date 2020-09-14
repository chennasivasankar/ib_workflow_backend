"""
As given user is not admin returns user does not have permission response
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetConfigurationDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture
    def user_set_up(self, api_user):
        user_id = api_user.user_id
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_user_details_factory
        reset_sequence_user_details_factory()
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.create(user_id=user_id, is_admin=False,
                                  company=None)

    @pytest.mark.django_db
    def test_given_user_not_admin_returns_user_does_not_have_perrmission_response(
            self, user_set_up, snapshot
    ):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
