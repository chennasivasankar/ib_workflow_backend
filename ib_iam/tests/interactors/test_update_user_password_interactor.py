import pytest


class TestUpdateUserProfileInteractor:

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_iam.interactors.presenter_interfaces \
            .update_user_password_presenter_interface import \
            UpdateUserPasswordPresenterInterface
        storage = mock.create_autospec(UpdateUserPasswordPresenterInterface)
        return storage

    @pytest.fixture
    def interactor(self):
        from ib_iam.interactors.update_user_password_interactor import \
            UpdateUserPassword
        interactor = UpdateUserPassword()
        return interactor

    @pytest.fixture
    def adapter_mock(self, mocker):
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            prepare_update_user_password
        update_user_password_mock = prepare_update_user_password(mocker)
        return update_user_password_mock

    def test_given_invalid_new_password_raises_invalid_new_password_exception(
            self, interactor, presenter, adapter_mock):
        from ib_iam.exceptions.custom_exceptions import InvalidNewPassword
        adapter_mock.side_effect = InvalidNewPassword

        interactor.update_user_password_wrapper(
            user_id=user_id,
            current_and_new_password_dto=current_and_new_password_dto)

