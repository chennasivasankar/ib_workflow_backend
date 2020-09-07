import mock
import pytest


class TestDeleteChecklistItemsInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from ib_utility_tools.interactors.storage_interfaces.checklist_storage_interface import (
            ChecklistStorageInterface
        )
        storage = mock.create_autospec(ChecklistStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from ib_utility_tools.interactors.presenter_interfaces.checklist_presenter_interface import (
            DeleteChecklistItemsPresenterInterface
        )
        presenter = mock.create_autospec(
            DeleteChecklistItemsPresenterInterface
        )
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_utility_tools.interactors.delete_checklist_items_interactor import (
            DeleteChecklistItemsInteractor
        )
        interactor = DeleteChecklistItemsInteractor(
            checklist_storage=storage_mock
        )
        return interactor

    def test_valid_item_ids_returns_success_response(
            self, storage_mock, presenter_mock, interactor
    ):
        # Arrange
        checklist_item_ids = ["1"]
        storage_mock.get_valid_checklist_item_ids.return_value = checklist_item_ids
        presenter_mock.get_response_for_delete_checklist_items.return_value = \
            mock.Mock()

        # Act
        interactor.delete_checklist_items_wrapper(
            checklist_item_ids=checklist_item_ids, presenter=presenter_mock
        )

        # Assert
        storage_mock.delete_checklist_items_bulk.assert_called_once_with(
            checklist_item_ids=checklist_item_ids
        )
        storage_mock.get_valid_checklist_item_ids.assert_called_once_with(
            checklist_item_ids=checklist_item_ids
        )
        presenter_mock.get_response_for_delete_checklist_items.assert_called_once()

    def test_given_duplicate_item_ids_then_raise_duplicate_item_ids_response(
            self, storage_mock, presenter_mock, interactor
    ):
        # Arrange
        checklist_item_ids = ["1", "1"]

        # Act
        interactor.delete_checklist_items_wrapper(
            checklist_item_ids=checklist_item_ids, presenter=presenter_mock
        )

        # Assert
        presenter_mock.response_for_duplicate_checklist_item_ids_exception \
            .return_value = mock.Mock()

    def test_given_invalid_item_ids_then_raise_invalid_item_ids_response(
            self, storage_mock, presenter_mock, interactor
    ):
        # Arrange
        checklist_item_ids = ["1", "2"]
        storage_mock.get_valid_checklist_item_ids.return_value = ["1"]

        # Act
        interactor.delete_checklist_items_wrapper(
            checklist_item_ids=checklist_item_ids, presenter=presenter_mock
        )

        # Assert
        storage_mock.get_valid_checklist_item_ids.assert_called_once_with(
            checklist_item_ids=checklist_item_ids
        )
        presenter_mock.response_for_invalid_checklist_item_ids_exception \
            .return_value = mock.Mock()
