import pytest


class TestUpdateUserPasswordAdapter:
    @staticmethod
    def update_user_password_mock(mocker):
        mock = mocker.patch(
            "ib_users.interfaces.service_interface.ServiceInterface.update_password"
        )
        return mock

    def test_update_user_password_with_valid_details(self, mocker):
        current_password = "Password@"
        new_password = "Password@"
        user_id = "1"
        from ib_iam.adapters.dtos import CurrentAndNewPasswordDTO
        current_and_new_password_dto = CurrentAndNewPasswordDTO(
            current_password=current_password, new_password=new_password)
        update_user_password_mock = self.update_user_password_mock(
            mocker=mocker)
        update_user_password_mock.return_value = None

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        auth_service.update_user_password(
            user_id=user_id,
            current_and_new_password_dto=current_and_new_password_dto)

        update_user_password_mock.assert_called_once_with(
            user_id=user_id, current_password=current_password,
            new_password=new_password)

    def test_update_user_password_with_invalid_current_password_then_raise_exception(
            self, mocker):
        invalid_current_password = "Password 1234"
        new_password = "Password@"
        user_id = "1"
        from ib_iam.adapters.dtos import CurrentAndNewPasswordDTO
        current_and_new_password_dto = CurrentAndNewPasswordDTO(
            current_password=invalid_current_password,
            new_password=new_password)
        update_user_password_mock = self.update_user_password_mock(
            mocker=mocker)
        from ib_users.interactors.user_credentials.exceptions. \
            user_credentials_exceptions import InvalidCurrentPasswordException
        update_user_password_mock.side_effect = InvalidCurrentPasswordException

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        from ib_iam.exceptions.custom_exceptions import InvalidCurrentPassword
        with pytest.raises(InvalidCurrentPassword):
            auth_service.update_user_password(
                user_id=user_id,
                current_and_new_password_dto=current_and_new_password_dto)

        update_user_password_mock.assert_called_once_with(
            user_id=user_id, current_password=invalid_current_password,
            new_password=new_password)

    def test_update_user_password_with_invalid_new_password_then_raise_exception(
            self, mocker):
        current_password = "Password@"
        invalid_new_password = "Password 123"
        user_id = "1"
        from ib_iam.adapters.dtos import CurrentAndNewPasswordDTO
        current_and_new_password_dto = CurrentAndNewPasswordDTO(
            current_password=current_password,
            new_password=invalid_new_password)
        update_user_password_mock = self.update_user_password_mock(
            mocker=mocker)
        from ib_users.interactors.user_credentials.exceptions. \
            user_credentials_exceptions import InvalidNewPasswordException
        update_user_password_mock.side_effect = InvalidNewPasswordException

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        from ib_iam.exceptions.custom_exceptions import InvalidNewPassword
        with pytest.raises(InvalidNewPassword):
            auth_service.update_user_password(
                user_id=user_id,
                current_and_new_password_dto=current_and_new_password_dto)

        update_user_password_mock.assert_called_once_with(
            user_id=user_id, current_password=current_password,
            new_password=invalid_new_password)

    def test_update_user_password_with_current_and_new_password_mismatch_then_raise_exception(
            self, mocker):
        current_password = "Password@"
        invalid_new_password = "Password1@"
        user_id = "1"
        from ib_iam.adapters.dtos import CurrentAndNewPasswordDTO
        current_and_new_password_dto = CurrentAndNewPasswordDTO(
            current_password=current_password,
            new_password=invalid_new_password)
        update_user_password_mock = self.update_user_password_mock(
            mocker=mocker)

        from ib_users.interactors.exceptions.user_credentials_exceptions import \
            CurrentPasswordMismatchException
        update_user_password_mock.side_effect = CurrentPasswordMismatchException
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        from ib_iam.exceptions.custom_exceptions import CurrentPasswordMismatch
        with pytest.raises(CurrentPasswordMismatch):
            auth_service.update_user_password(
                user_id=user_id,
                current_and_new_password_dto=current_and_new_password_dto)

        update_user_password_mock.assert_called_once_with(
            user_id=user_id, current_password=current_password,
            new_password=invalid_new_password)
