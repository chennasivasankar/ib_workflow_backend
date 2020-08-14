import mock
import pytest


class TestDeleteChecklistItemsInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from ib_utility_tools.interactors.storage_interfaces \
            .checklist_storage_interface import ChecklistStorageInterface
        storage = mock.create_autospec(ChecklistStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from ib_utility_tools.interactors.presenter_interfaces \
            .delete_checklist_items_presenter_interface import \
            DeleteChecklistItemsPresenterInterface
        presenter = \
            mock.create_autospec(DeleteChecklistItemsPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_utility_tools.interactors.delete_checklist_items_interactor \
            import DeleteChecklistItemsInteractor
        interactor = \
            DeleteChecklistItemsInteractor(checklist_storage=storage_mock)
        return interactor

    def test_valid_item_ids_returns_success_response(
            self, storage_mock, presenter_mock, interactor):
        checklist_item_ids = ["1"]

        interactor.delete_checklist_items_wrapper(
            checklist_item_ids=checklist_item_ids,
            presenter=presenter_mock)

        storage_mock.delete_checklist_items_bulk.assert_called_once_with(
            checklist_item_ids=checklist_item_ids)
        presenter_mock.get_success_response_for_delete_checklist_items \
            .return_value = mock.Mock()
