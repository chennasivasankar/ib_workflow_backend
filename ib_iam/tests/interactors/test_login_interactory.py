import pytest
from unittest.mock import patch

class TestLoginInteractor:

    @property
    def storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.storage_interfaces import \
            StorageInterface
        storage = create_autospec(StorageInterface)
        return storage

    @property
    def presenter_mock(self):
        # import unittest
        from unittest.mock import create_autospec
        from ib_iam.interactors.presenter_interfaces import \
            PresenterInterface
        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture()
    def email_and_password_dto(self):
        from ib_iam.interactors.login_interactor import \
            EmailAndPasswordDTO
        email_and_password_dto = EmailAndPasswordDTO(
            email="test#gamil.com",
            password="test123"
        )
        return email_and_password_dto

    @patch("ib_iam.adapters.get_service_adapter")
    def test_validate_email_raise_exception(self, get_service_adapter, email_and_password_dto):
        # Arrange
        email = "test#gamil.com"
        from ib_iam.interactors.login_interactor import \
            InvalidEmail
        get_service_adapter.get_user_id_form_email_and_password_dto.return_value = InvalidEmail

        from ib_iam.interactors.login_interactor import LoginInteractor
        interactor = LoginInteractor(storage=self.storage_mock)

        # Assert
        with pytest.raises(InvalidEmail):
            interactor.login_wrapper(email_and_password_dto=email_and_password_dto)
