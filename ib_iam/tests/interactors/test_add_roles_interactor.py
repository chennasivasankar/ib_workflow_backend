from unittest.mock import create_autospec, Mock

from ib_iam.interactors.add_list_of_roles_interactor import AddRolesInteractor
from ib_iam.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_iam.interactors.presenter_interfaces.presenter_interface \
    import PresenterInterface

import pytest


class TestAddRolesInteractor:

    def when_role_id_is_empty_raise_exception(self):

        # Arrange
        list_of_roles = [{
            "role_id": "",
            "role_name": "payment poc",
            "role_description": "payment poc"
        }]
        expected_output = Mock()
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = AddRolesInteractor(storage=storage)
        presenter.raise_role_id_should_not_be_empty.return_value = \
            expected_output

        # Act
        output = interactor.add_roles_wrapper(roles=list_of_roles,
                                              presenter=presenter)

        # Assert
        assert output == expected_output
        presenter.raise_role_id_should_not_be_empty.assert_called_once()

    def test_when_role_id_is_not_string_raise_exception(self):

        # Arrange
        list_of_roles = [{
            "role_id": 123,
            "role_name": "payment poc",
            "role_description": "payment poc"
        }]
        expected_output = Mock()
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = AddRolesInteractor(storage=storage)
        presenter.raise_invalid_role_id_execption.return_value = \
            expected_output

        # Act
        output = interactor.add_roles_wrapper(roles=list_of_roles,
                                              presenter=presenter)

        # Assert
        assert output == expected_output
        presenter.raise_invalid_role_id_execption.assert_called_once()


    def test_when_role_ids_are_duplicate_raise_exception(self):

        # Arrange
        list_of_roles = [
            {
                "role_id": "PAYMENT_POC",
                "role_name": "payment poc",
                "role_description": "payment poc"
            },
            {
                "role_id": "PAYMENT_POC_PAYMENT_POC2",
                "role_name": "payment_poc",
                "role_description": "payment poc"
            },
            {
                "role_id": "PAYMENTPOC",
                "role_name": "payment_poc",
                "role_description": "payment poc"
            },

        ]
        expected_output = Mock()
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = AddRolesInteractor(storage=storage)
        presenter.raise_duplicate_role_ids_exception.return_value = \
            expected_output

        # Act
        output = interactor.add_roles_wrapper(roles=list_of_roles,
                                              presenter=presenter)

        # Assert
        assert output == expected_output
        presenter.raise_duplicate_role_ids_exception.assert_called_once()

    def test_when_role_name_is_empty_raise_exception(self):

        # Arrange
        list_of_roles = [{
            "role_id": "PAYMENT_POC",
            "role_name": "",
            "role_description": "payment poc"
        }]
        expected_output = Mock()
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = AddRolesInteractor(storage=storage)
        presenter.raise_role_name_should_not_be_empty.return_value = \
            expected_output

        # Act
        output = interactor.add_roles_wrapper(
             roles=list_of_roles, presenter=presenter)

        # Assert
        assert output == expected_output
        presenter.raise_role_name_should_not_be_empty.assert_called_once()


    def test_when_role_description_is_empty_raise_exception(self):

        # Arrange
        list_of_roles = [{
            "role_id": "PAYMENT_POC",
            "role_name": "payment poc",
            "role_description": ""
        }]
        expected_output = Mock()
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = AddRolesInteractor(storage=storage)
        presenter.raise_role_description_should_not_be_empty.return_value = \
            expected_output

        # Act
        output = interactor.add_roles_wrapper(
            roles=list_of_roles, presenter=presenter)

        # Assert
        assert output == expected_output
        presenter.raise_role_description_should_not_be_empty.assert_called_once()


    def test_when_role_id_is_not_in_camel_case_or_empty_raise_exception(self):

        # Arrange
        list_of_roles = [{
            "role_id": "payment_poc",
            "role_name": "payment poc",
            "role_description": "payment poc"
        }]
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = AddRolesInteractor(storage=storage)

        # Act
        interactor.add_roles_wrapper(
            roles=list_of_roles, presenter=presenter)

        # Assert
        presenter.raise_role_id_format_is_invalid.assert_called_once()


    def test_when_valid_details_given(self):

        # Arrange
        list_of_roles = [{
            "role_id": "PAYMENT_POC",
            "role_name": "payment poc",
            "role_description": "payment poc"
        }]
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)
        interactor = AddRolesInteractor(storage=storage)

        # Act
        interactor.add_roles_wrapper(
            roles=list_of_roles, presenter=presenter)

        # Assert
        storage.create_roles_from_list_of_role_dtos.assert_called_once()
        # presenter.raise_role_id_should_not_be_empty.assert_called_once()