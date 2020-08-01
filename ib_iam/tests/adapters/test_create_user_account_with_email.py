from unittest.mock import patch

import pytest


class TestCreateAccountWithEmail:
    @patch('ib_users.interfaces.service_interface.ServiceInterface.create_user_account_with_email')
    def test_create_account_with_already_existed_account_with_that_email_raise_exception(
            self, create_user_account_with_email_mock):
        # Arrange
        email = "parker2020@gmail.com"
        from ib_users.exceptions.registration_exceptions \
            import AccountWithThisEmailAlreadyExistsException

        from ib_iam.exceptions.custom_exceptions \
            import UserAccountAlreadyExistWithThisEmail

        create_user_account_with_email_mock.side_effect = \
            AccountWithThisEmailAlreadyExistsException
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Assert
        with pytest.raises(UserAccountAlreadyExistWithThisEmail):
            service_adapter.user_service.create_user_account_with_email(email=email)

    @patch('ib_users.interfaces.service_interface.ServiceInterface.create_user_account_with_email')
    def test_create_account_when_creates_then_returns_user_id(
            self, create_user_account_with_email_mock):
        # Arrange
        email = "parker2020@gmail.com"
        expected_user_id = 'e06b8a3b-94af-4d2e-ba14-bcec11140277'

        create_user_account_with_email_mock.return_value = expected_user_id
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Act
        user_id = service_adapter.user_service.create_user_account_with_email(
            email=email)

        # Assert
        assert user_id == expected_user_id
        create_user_account_with_email_mock.assert_called_once_with(email=email)
