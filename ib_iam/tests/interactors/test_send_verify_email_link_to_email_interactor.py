from unittest.mock import patch, Mock, create_autospec

import pytest


class TestSendLinkToUserMail:

    @pytest.fixture
    def init_interactor(self):
        from ib_iam.interactors.send_verify_email_link_interactor import \
            SendVerifyEmailLinkInteractor
        return SendVerifyEmailLinkInteractor()

    @pytest.fixture
    def presenter_mock(self):
        from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
            SendVerifyEmailLinkPresenterInterface
        presenter_mock = create_autospec(SendVerifyEmailLinkPresenterInterface)
        return presenter_mock

    def test_send_verify_email_link_to_email_given_valid_email(
            self, presenter_mock, init_interactor, mocker):
        interactor = init_interactor
        email = "example@gmail.com"
        user_id = "1"
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            create_auth_tokens_for_user_mock
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        get_user_id_for_given_email_mock.return_value = user_id
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(
            mocker=mocker)
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        UserProfileDTOFactory.reset_sequence(0)
        get_user_profile_dto_mock.return_value = UserProfileDTOFactory.create(
            user_id=user_id, is_email_verify=False)
        create_auth_tokens_for_user_mock = create_auth_tokens_for_user_mock(
            mocker=mocker)
        from ib_iam.tests.factories.adapter_dtos import UserTokensDTOFactory
        UserTokensDTOFactory.reset_sequence(0)
        create_auth_tokens_for_user_mock.return_value = \
            UserTokensDTOFactory.create()
        from ib_iam.tests.common_fixtures.adapters.email_service_adapter_mocks import \
            send_email_mock
        send_email_mock = send_email_mock(mocker=mocker)
        send_email_mock.return_value = None

        interactor.send_verify_email_link_wrapper(
            email=email,
            presenter=presenter_mock
        )

        create_auth_tokens_for_user_mock.assert_called_once_with(
            user_id=user_id, expiry_in_seconds=3600)
        get_user_id_for_given_email_mock.assert_called_once_with(email=email)

    def test_given_invalid_email_then_raises_exception(
            self, presenter_mock, init_interactor, mocker):
        email = "example@gmail.com"
        interactor = init_interactor
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        from ib_iam.exceptions.custom_exceptions import UserAccountDoesNotExist
        get_user_id_for_given_email_mock.side_effect = \
            UserAccountDoesNotExist()
        presenter_mock.raise_account_does_not_exist_exception.return_value = \
            Mock()

        interactor.send_verify_email_link_wrapper(
            email=email, presenter=presenter_mock)

        presenter_mock.raise_account_does_not_exist_exception.assert_called_once()
        get_user_id_for_given_email_mock.assert_called_once_with(email=email)

    def test_given_email_is_already_verify_then_raise_exception(self,
                                                                presenter_mock,
                                                                init_interactor,
                                                                mocker):
        interactor = init_interactor
        email = "example@gmail.com"
        user_id = "1"
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            get_user_id_for_given_email_mock
        get_user_id_for_given_email_mock = get_user_id_for_given_email_mock(
            mocker=mocker)
        get_user_id_for_given_email_mock.return_value = user_id
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(
            mocker=mocker)
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        UserProfileDTOFactory.reset_sequence(0)
        get_user_profile_dto_mock.return_value = UserProfileDTOFactory.create(
            user_id=user_id, is_email_verify=True)
        presenter_mock.raise_email_already_verified_exception.return_value = Mock()

        interactor.send_verify_email_link_wrapper(
            email=email,
            presenter=presenter_mock
        )

        get_user_id_for_given_email_mock.assert_called_once_with(email=email)
        get_user_profile_dto_mock.assert_called_once_with(user_id=user_id)
        presenter_mock.raise_email_already_verified_exception.assert_called_once()
