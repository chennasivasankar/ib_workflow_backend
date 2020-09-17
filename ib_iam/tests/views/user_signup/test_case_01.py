"""
Success case for Signup User and create User account
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01UserSignupAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': []}}

    @pytest.mark.django_db
    def test_case_with_valid_details_and_email_is_use_first_time(
            self, snapshot, mocker):
        self.mock_all_third_party_modules_where_email_is_used_first_time(
            mocker=mocker)

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

    @pytest.mark.django_db
    def test_case_with_valid_details_and_and_use_deactivated_emails(
            self, snapshot, mocker):
        self.mock_all_third_party_modules_for_deactivate_account(mocker=mocker)

        body = {'name': 'durga', 'email': 'durga123@gmail.com',
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

    @staticmethod
    def elastic_storage_create_elastic_user_mock(mocker):
        mock = mocker.patch(
            "ib_iam.storages.elastic_storage_implementation.ElasticStorageImplementation.create_elastic_user"
        )
        mock.create_elastic_user.return_value = "elastic_user1"
        return mock

    @staticmethod
    def elastic_storage_create_elastic_user_intermediary_mock(mocker):
        mock = mocker.patch(
            "ib_iam.storages.elastic_storage_implementation.ElasticStorageImplementation.create_elastic_user_intermediary"
        )
        mock.create_elastic_user_intermediary.return_value = None
        return mock

    @staticmethod
    def send_verification_email_mock(mocker):
        mock = mocker.patch(
            "ib_iam.interactors.auth.send_verify_email_link_interactor.SendVerifyEmailLinkInteractor.send_verification_email"
        )
        return mock

    def mock_all_third_party_modules_where_email_is_used_first_time(
            self, mocker):
        user_id = "123e4567-e89b-12d3-a456-426614174000"
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
        create_user_account_adapter_mock.return_value = user_id
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            create_user_profile_adapter_mock
        create_user_profile_adapter_mock = create_user_profile_adapter_mock(
            mocker=mocker)
        create_user_profile_adapter_mock.return_value = None
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            update_is_email_verified_value_mock
        update_is_email_verified_value_mock = update_is_email_verified_value_mock(
            mocker=mocker)
        update_is_email_verified_value_mock.return_value = None
        self.elastic_storage_create_elastic_user_mock(mocker=mocker)
        self.elastic_storage_create_elastic_user_intermediary_mock(
            mocker=mocker)
        send_verification_email_mock = self.send_verification_email_mock(
            mocker=mocker)
        send_verification_email_mock.return_value = None

    def mock_all_third_party_modules_for_deactivate_account(self, mocker):
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        get_user_id_for_given_email_mock.return_value = user_id
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            is_active_user_account_mock
        is_active_user_account_mock = is_active_user_account_mock(
            mocker=mocker)
        is_active_user_account_mock.return_value = False
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            activate_user_account_mock
        activate_user_account_mock = activate_user_account_mock(mocker=mocker)
        activate_user_account_mock.return_value = None
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            update_user_profile_success_adapter_mock
        update_user_profile_success_adapter_mock(mocker=mocker)
        self.elastic_storage_create_elastic_user_mock(mocker=mocker)
        self.elastic_storage_create_elastic_user_intermediary_mock(
            mocker=mocker)
        send_verification_mock = self.send_verification_email_mock(
            mocker=mocker)
        send_verification_mock.return_value = None
