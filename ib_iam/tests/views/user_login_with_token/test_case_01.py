"""
Given valid token for which user already exists returns tokens successfully
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
    def test_auth_user_already_exist_returns_response(
            self, setup_for_auth_user_already_exist_case, snapshot
    ):
        token = setup_for_auth_user_already_exist_case["token"]
        body = {
            "name": "username",
            "user_id": "89d96f4b-c19d-4e69-8eae-e818f3123b09"
        }
        path_params = {}
        query_params = {'token': token}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)
        self.checks_to_perform(token=token, snapshot=snapshot)

    @pytest.fixture
    def setup_for_auth_user_already_exist_case(self, mocker):
        from ib_iam.tests.factories.adapter_dtos import UserTokensDTOFactory
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import create_auth_tokens_for_user_mock
        from ib_iam.tests.factories.models import UserAuthTokenFactory
        user_id = "user_id_1"
        token = "token1"

        UserAuthTokenFactory.create(
            user_id=user_id, token=token,
            auth_token_user_id="89d96f4b-c19d-4e69-8eae-e818f3123b09"
        )
        UserTokensDTOFactory.reset_sequence(0)
        user_tokens_dto = UserTokensDTOFactory(user_id=user_id)
        create_auth_tokens_for_user_mock = create_auth_tokens_for_user_mock(
            mocker=mocker
        )
        create_auth_tokens_for_user_mock.return_value = user_tokens_dto
        return {"token": token}

    @staticmethod
    def checks_to_perform(token, snapshot):
        from ib_iam.models import UserAuthToken
        user_auth_values = UserAuthToken.objects.filter(token=token).values()
        snapshot.assert_match(user_auth_values[0], "UserAuthDetails")
