from unittest.mock import create_autospec, patch, Mock

import pytest

from ib_iam.exceptions.custom_exceptions import InvalidEmail
from ib_iam.interactors.sign_up_interactor import SignupInteractor


class TestSignUpInteractor():

    @pytest.fixture
    def user_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        user_storage_mock = create_autospec(UserStorageInterface)
        return user_storage_mock

    @pytest.fixture
    def presenter_mock(self):
        from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
            CreateUserAccountPresenterInterface
        presenter_mock = create_autospec(CreateUserAccountPresenterInterface)
        return presenter_mock

    @pytest.fixture
    def init_interactor(self, user_storage_mock):
        interactor = SignupInteractor(user_storage=user_storage_mock)
        return interactor, user_storage_mock

    @pytest.fixture
    def set_up(self):
        email = "sample@gmail.com"
        password = "Password@123"
        name = "Sample"
        return email, password, name

    @staticmethod
    def send_verification_email_mock(mocker):
        mock = mocker.patch(
            "ib_iam.interactors.send_verify_email_link_interactor.SendVerifyEmailLinkInteractor.send_verification_email"
        )
        return mock

    def test_create_user_given_valid_details_and_send_verification_link_to_email(
            self, init_interactor, presenter_mock, set_up, mocker):
        user_id = "1"
        email, password, name = set_up
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        from ib_iam.exceptions.custom_exceptions import UserAccountDoesNotExist
        get_user_id_for_given_email_mock.side_effect = UserAccountDoesNotExist
        interactor, user_storage_mock = init_interactor
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
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            update_user_profile_success_adapter_mock
        update_user_profile_success_adapter_mock(mocker=mocker)
        send_verification_mock = self.send_verification_email_mock(
            mocker=mocker)
        send_verification_mock.return_value = None
        user_storage_mock.create_user.return_value = None
        presenter_mock.get_response_for_create_user_account.return_value = Mock()

        interactor.signup_wrapper(email=email, password=password, name=name,
                                  presenter=presenter_mock)

        user_storage_mock.create_user.assert_called_once_with(
            is_admin=False, name=name, user_id=user_id)
        get_user_id_for_given_email_mock.assert_called_once_with(email=email)
        send_verification_mock.assert_called_once()
        presenter_mock.get_response_for_create_user_account.assert_called_once()

    def test_given_invalid_email_raises_exception(
            self, init_interactor, presenter_mock, set_up, mocker):
        email, password, name = set_up
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        from ib_iam.exceptions.custom_exceptions import UserAccountDoesNotExist
        get_user_id_for_given_email_mock.side_effect = UserAccountDoesNotExist
        interactor, user_storage_mock = init_interactor
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            create_user_account_adapter_mock
        create_user_account_adapter_mock = create_user_account_adapter_mock(
            mocker=mocker)
        create_user_account_adapter_mock.side_effect = InvalidEmail
        presenter_mock.raise_invalid_email_exception.return_value = Mock()

        interactor.signup_wrapper(email=email, password=password, name=name,
                                  presenter=presenter_mock)

        get_user_id_for_given_email_mock.assert_called_once_with(email=email)
        presenter_mock.raise_invalid_email_exception.assert_called_once()
        create_user_account_adapter_mock.assert_called_once_with(
            email=email, password=password)

    def test_given_already_exists_email__and_email_is_active_then_raises_exception(
            self, init_interactor, presenter_mock, set_up, mocker):
        email, password, name = set_up
        user_id = "1"
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        get_user_id_for_given_email_mock.return_value = user_id
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            is_active_user_account_mock
        is_active_user_account_mock = is_active_user_account_mock(
            mocker=mocker)
        is_active_user_account_mock.return_value = True
        interactor, user_storage_mock = init_interactor
        presenter_mock.raise_account_already_exists_exception.return_value = \
            Mock()

        interactor.signup_wrapper(email=email, password=password, name=name,
                                  presenter=presenter_mock)

        get_user_id_for_given_email_mock.assert_called_once_with(email=email)
        presenter_mock.raise_account_already_exists_exception.assert_called_once()
        is_active_user_account_mock.assert_called_once_with(email=email)

    def test_given_invalid_password_email_raises_exception(
            self, init_interactor, presenter_mock, set_up):
        email, password, name = set_up
        password = "123"
        interactor, user_storage_mock = init_interactor
        presenter_mock.raise_password_not_matched_with_criteria_exception. \
            return_value = Mock()

        interactor.signup_wrapper(email=email, password=password, name=name,
                                  presenter=presenter_mock)

        presenter_mock.raise_password_not_matched_with_criteria_exception. \
            assert_called_once()

    def test_given_invalid_email_domain_raises_exception(
            self, init_interactor, presenter_mock, set_up):
        email, password, name = set_up
        email = "sample@youtube.com"
        interactor, user_storage_mock = init_interactor
        presenter_mock.raise_invalid_domain_exception. \
            return_value = Mock()

        interactor.signup_wrapper(email=email, password=password, name=name,
                                  presenter=presenter_mock)

        presenter_mock.raise_invalid_domain_exception. \
            assert_called_once()

    def test_given_valid_details_and_user_account_is_deactivated_then_activate_account_and_update_details(
            self, init_interactor, presenter_mock, set_up, mocker):
        user_id = "1"
        email, password, name = set_up
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        get_user_id_for_given_email_mock.return_value = user_id
        interactor, user_storage_mock = init_interactor
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
        send_verification_mock = self.send_verification_email_mock(
            mocker=mocker)
        send_verification_mock.return_value = None
        user_storage_mock.create_user.return_value = None
        presenter_mock.get_response_for_create_user_account.return_value = Mock()

        interactor.signup_wrapper(email=email, password=password, name=name,
                                  presenter=presenter_mock)

        user_storage_mock.create_user.assert_called_once_with(
            is_admin=False, name=name, user_id=user_id)
        get_user_id_for_given_email_mock.assert_called_once_with(email=email)
        send_verification_mock.assert_called_once()
        presenter_mock.get_response_for_create_user_account.assert_called_once()
