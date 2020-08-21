"""
All invalid cases
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02UserSignupAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': []}}

    # @pytest.fixture
    # def set_up_for_already_used_email(self, mocker):
    #     user_id = "123e4567-e89b-12d3-a456-426614174000"
    #     from ib_iam.tests.common_fixtures.adapters.user_service import \
    #         get_user_id_for_given_email_mock
    #     get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
    #         mocker=mocker)
    #     get_user_id_for_given_email_mock.return_value = user_id
    #     from ib_iam.tests.common_fixtures.adapters.user_service import \
    #         is_active_user_account_mock
    #     is_active_user_account_mock = is_active_user_account_mock(
    #         mocker=mocker)
    #     is_active_user_account_mock.return_value = True
    #
    # @pytest.mark.django_db
    # def test_with_active_email_then_raise_exception(
    #         self, set_up_for_already_used_email, snapshot):
    #     body = {'name': 'durga', 'email': 'durgaprasad@gmail.com',
    #             'password': 'Password123@'}
    #     path_params = {}
    #     query_params = {}
    #     headers = {}
    #     self.make_api_call(
    #         body=body,
    #         path_params=path_params,
    #         query_params=query_params,
    #         headers=headers,
    #         snapshot=snapshot
    #     )

    @pytest.fixture
    def set_up_for_invalid_email(self, mocker):
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        from ib_iam.exceptions.custom_exceptions import UserAccountDoesNotExist
        get_user_id_for_given_email_mock.side_effect = UserAccountDoesNotExist
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            create_user_account_adapter_mock
        create_user_account_adapter_mock = create_user_account_adapter_mock(
            mocker=mocker)
        from ib_iam.exceptions.custom_exceptions import InvalidEmail
        create_user_account_adapter_mock.side_effect = InvalidEmail

    @pytest.mark.django_db
    def test_with_invalid_email(self, set_up_for_invalid_email, snapshot):
        body = {'name': 'durga', 'email': 'durgaprasad@gmail.com',
                'password': 'Password123@'}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            snapshot=snapshot
        )

    @pytest.fixture
    def set_up_for_invalid_password(self):
        invalid_password = "1230"
        return invalid_password

    @pytest.mark.django_db
    def test_with_invalid_password(self, set_up_for_invalid_password,
                                   snapshot):
        invalid_password = set_up_for_invalid_password
        body = {'name': 'durga', 'email': 'durgaprasad@gmail.com',
                'password': invalid_password}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            snapshot=snapshot
        )

    @pytest.fixture
    def set_up_for_invalid_email_domain(self):
        invalid_email = "durga@youtube.com"
        return invalid_email

    @pytest.mark.django_db
    def test_with_invalid_email_domain(
            self, set_up_for_invalid_email_domain, snapshot):
        invalid_email = set_up_for_invalid_email_domain
        body = {'name': 'durga', 'email': invalid_email,
                'password': "Password123@"}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            snapshot=snapshot
        )
