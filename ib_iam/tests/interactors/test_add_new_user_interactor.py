from unittest.mock import Mock

import pytest

from ib_iam.interactors.add_new_user_interactor import AddNewUserInteractor


class TestAddNewUserIneractor:

    @pytest.fixture
    def storage_mock(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces.storage_interface import StorageInterface
        storage = mock.create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_iam.interactors.presenter_interfaces.presenter_interface import PresenterInterface
        storage = mock.create_autospec(PresenterInterface)
        return storage

    def test_create_user_when_user_is_not_admin_then_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        name = "username"
        email = "user@email.com"

        interactor = AddNewUserInteractor(storage=storage_mock)
        storage_mock.validate_user_is_admin.return_value = False
        presenter_mock.raise_user_is_not_admin_exception.return_value = Mock()
        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id, name=name, email=email, presenter=presenter_mock)

        # Assert
        storage_mock.validate_user_is_admin.assert_called_once_with(
            user_id=user_id)
        presenter_mock.raise_user_is_not_admin_exception.assert_called_once()

    def test_validate_name_and_throw_exception(self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        name = ""
        email = "user@email.com"
        interactor = AddNewUserInteractor(storage=storage_mock)
        storage_mock.validate_user_is_admin.return_value = True
        presenter_mock.raise_invalid_name_exception.return_value = Mock()

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id, name=name, email=email, presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_name_exception.assert_called_once()

    def test_validate_email_and_throw_exception(self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        name = ""
        email = "user@email.com"
        interactor = AddNewUserInteractor(storage=storage_mock)
        storage_mock.validate_user_is_admin.return_value = True
        presenter_mock.raise_invalid_name_exception.return_value = Mock()

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id, name=name, email=email, presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_name_exception.assert_called_once()
