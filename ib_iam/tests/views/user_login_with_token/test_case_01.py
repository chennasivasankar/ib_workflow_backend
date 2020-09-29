"""
Given valid data returns tokens successfully
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01UserLoginWithTokenAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        body = {}
        path_params = {}
        query_params = {'token': setup['token']}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.fixture
    def setup(self, mocker):
        user_id = "user_id_1"
        token = "token1"
        from ib_iam.tests.factories.adapter_dtos import UserTokensDTOFactory
        user_tokens_dto = UserTokensDTOFactory(user_id=user_id)
        from ib_iam.tests.common_fixtures.adapters \
            .auth_service_adapter_mocks import create_auth_tokens_for_user_mock
        create_auth_tokens_for_user_mock = create_auth_tokens_for_user_mock(
            mocker=mocker
        )
        create_auth_tokens_for_user_mock.return_value = user_tokens_dto
        from ib_iam.tests.factories.models import \
            UserAuthTokenFactory, UserDetailsFactory
        UserAuthTokenFactory.create(user_id=user_id, token=token)
        UserDetailsFactory.create(user_id=user_id, is_admin=True)
        return {"token": token}
    # TODO need to change from implementation
