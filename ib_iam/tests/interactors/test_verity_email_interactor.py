from unittest.mock import create_autospec, Mock

import pytest


class TestVerifyEmailInteractor:

    @pytest.fixture
    def presenter_mock(self):
        from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
            VerifyEmailPresenterInterface
        presenter_mock = create_autospec(VerifyEmailPresenterInterface)
        return presenter_mock

    @pytest.fixture
    def init_interactor(self):
        from ib_iam.interactors.verify_user_email_interactor import \
            VerifyEmailInteractor
        interactor = VerifyEmailInteractor()
        return interactor

    def test_given_invalid_email_raises_exception(
            self, init_interactor, presenter_mock, mocker
    ):
        # Arrange
        interactor = init_interactor
        user_id = "76fcdf69-853e-486d-bb90-2ef99bb43aa5"
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(
            mocker=mocker)
        from ib_iam.adapters.dtos import UserProfileDTO
        get_user_profile_dto_mock.return_value = UserProfileDTO(
            user_id=user_id, name="Baba"
        )
        presenter_mock.response_for_email_does_not_exist_exception. \
            return_value = Mock()

        # Act
        interactor.link_verified_email_to_user_account_wrapper(
            user_id=user_id, presenter=presenter_mock)

        # Assert
        get_user_profile_dto_mock.assert_called_once_with(user_id=user_id)
        presenter_mock.response_for_email_does_not_exist_exception \
            .assert_called_once()

    def test_given_email_already_verified_raises_exception(
            self, init_interactor, presenter_mock, mocker
    ):
        # Arrange
        interactor = init_interactor
        user_id = "76fcdf69-853e-486d-bb90-2ef99bb43aa5"
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(
            mocker=mocker)
        from ib_iam.adapters.dtos import UserProfileDTO
        get_user_profile_dto_mock.return_value = UserProfileDTO(
            email="example@gmail.com", user_id=user_id, name="Baba",
            is_email_verified=True
        )
        presenter_mock.response_for_email_already_verified_exception.return_value \
            = Mock()

        # Act
        interactor.link_verified_email_to_user_account_wrapper(
            user_id=user_id, presenter=presenter_mock)

        # Arrange
        get_user_profile_dto_mock.assert_called_once_with(user_id=user_id)
        presenter_mock.response_for_email_already_verified_exception \
            .assert_called_once()

    def test_verified_email_then_return_response(
            self, init_interactor, presenter_mock, mocker
    ):
        # Arrange
        interactor = init_interactor
        user_id = "76fcdf69-853e-486d-bb90-2ef99bb43aa5"
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(
            mocker=mocker)
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        get_user_profile_dto_mock.return_value = UserProfileDTOFactory.create(
            name="Baba", user_id=user_id, is_email_verified=False
        )

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            update_is_email_verified_value_mock
        update_is_email_verified_value_mock = update_is_email_verified_value_mock(
            mocker=mocker)
        update_is_email_verified_value_mock.return_value = None
        presenter_mock.get_response_for_verified_email.return_value \
            = Mock()

        # Act
        interactor.link_verified_email_to_user_account_wrapper(
            user_id=user_id, presenter=presenter_mock)

        # Assert
        get_user_profile_dto_mock.assert_called_once_with(user_id=user_id)
        update_is_email_verified_value_mock.assert_called_once_with(
            user_id=user_id, is_email_verified=True)
        presenter_mock.get_response_for_verified_email.assert_called_once()
