import mock
import pytest


class TestUpdateUserProfileInteractor:

    @pytest.fixture
    def presenter_mock(self):
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
            self, interactor, presenter_mock, adapter_mock):
        from ib_iam.exceptions.custom_exceptions import InvalidNewPassword
        from ib_iam.tests.factories.interactor_dtos import \
            CurrentAndNewPasswordDTOFactory
        user_id = "1"
        current_and_new_password_dto = CurrentAndNewPasswordDTOFactory()
        adapter_mock.side_effect = InvalidNewPassword
        presenter_mock.raise_invalid_new_password_exception \
            .return_value = mock.Mock(())

        interactor.update_user_password_wrapper(
            user_id=user_id,
            current_and_new_password_dto=current_and_new_password_dto,
            presenter=presenter_mock)

        adapter_mock.assert_called_once_with(
            user_id=user_id,
            current_and_new_password_dto=current_and_new_password_dto)
        presenter_mock.raise_invalid_new_password_exception \
            .assert_called_once()

    def test_given_invalid_current_password_raises_invalid_current_password_exception(
            self, interactor, presenter_mock, adapter_mock):
        from ib_iam.exceptions.custom_exceptions import InvalidCurrentPassword
        from ib_iam.tests.factories.interactor_dtos import \
            CurrentAndNewPasswordDTOFactory
        user_id = "1"
        current_and_new_password_dto = CurrentAndNewPasswordDTOFactory()
        adapter_mock.side_effect = InvalidCurrentPassword
        presenter_mock.raise_invalid_new_password_exception \
            .return_value = mock.Mock(())

        interactor.update_user_password_wrapper(
            user_id=user_id,
            current_and_new_password_dto=current_and_new_password_dto,
            presenter=presenter_mock)

        adapter_mock.assert_called_once_with(
            user_id=user_id,
            current_and_new_password_dto=current_and_new_password_dto)
        presenter_mock.raise_invalid_current_password_exception \
            .assert_called_once()

    def test_given_mismatching_current_password_raises_current_password_mismatch_exception(
            self, interactor, presenter_mock, adapter_mock):
        from ib_iam.exceptions.custom_exceptions import CurrentPasswordMismatch
        from ib_iam.tests.factories.interactor_dtos import \
            CurrentAndNewPasswordDTOFactory
        user_id = "1"
        current_and_new_password_dto = CurrentAndNewPasswordDTOFactory()
        adapter_mock.side_effect = CurrentPasswordMismatch
        presenter_mock.raise_invalid_new_password_exception \
            .return_value = mock.Mock(())

        interactor.update_user_password_wrapper(
            user_id=user_id,
            current_and_new_password_dto=current_and_new_password_dto,
            presenter=presenter_mock)

        adapter_mock.assert_called_once_with(
            user_id=user_id,
            current_and_new_password_dto=current_and_new_password_dto)
        presenter_mock.raise_current_password_mismatch_exception \
            .assert_called_once()

    def test_given_valid_details_returns_success_response(
            self, interactor, presenter_mock, adapter_mock):
        from ib_iam.tests.factories.interactor_dtos import \
            CurrentAndNewPasswordDTOFactory
        user_id = "1"
        current_and_new_password_dto = CurrentAndNewPasswordDTOFactory()
        presenter_mock.get_success_response_for_update_user_password \
            .return_value = mock.Mock(())

        interactor.update_user_password_wrapper(
            user_id=user_id,
            current_and_new_password_dto=current_and_new_password_dto,
            presenter=presenter_mock)

        adapter_mock.assert_called_once_with(
            user_id=user_id,
            current_and_new_password_dto=current_and_new_password_dto)
        presenter_mock.get_success_response_for_update_user_password \
            .assert_called_once()
