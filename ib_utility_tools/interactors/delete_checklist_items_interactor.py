from typing import List

from ib_utility_tools.exceptions.custom_exceptions import \
    DuplicateChecklistItemIds
from ib_utility_tools.interactors.presenter_interfaces.delete_checklist_items_presenter_interface import \
    DeleteChecklistItemsPresenterInterface
from ib_utility_tools.interactors.storage_interfaces.checklist_storage_interface import \
    ChecklistStorageInterface


class DeleteChecklistItemsInteractor:
    def __init__(self, checklist_storage: ChecklistStorageInterface):
        self.checklist_storage = checklist_storage

    def delete_checklist_items_wrapper(
            self, checklist_item_ids: List[str],
            presenter: DeleteChecklistItemsPresenterInterface):
        try:
            self.delete_checklist_items(checklist_item_ids=checklist_item_ids)
            response = \
                presenter.get_success_response_for_delete_checklist_items()
        except DuplicateChecklistItemIds:
            response = presenter \
                .get_duplicate_checklist_item_ids_for_delete_checklist_items()
        return response

    def delete_checklist_items(self, checklist_item_ids: List[str]):
        self._validate_checklist_item_ids(
            checklist_item_ids=checklist_item_ids)
        self.checklist_storage.delete_checklist_items_bulk(
            checklist_item_ids=checklist_item_ids)

    def _validate_checklist_item_ids(self, checklist_item_ids: List[str]):
        self._validate_duplicate_checklist_item_ids(checklist_item_ids)

    @staticmethod
    def _validate_duplicate_checklist_item_ids(checklist_item_ids):
        is_duplicate_ids_exist = \
            len(checklist_item_ids) != len(set(checklist_item_ids))
        if is_duplicate_ids_exist:
            raise DuplicateChecklistItemIds