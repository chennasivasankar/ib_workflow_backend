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
        self.delete_checklist_items(checklist_item_ids=checklist_item_ids)
        response = presenter.get_success_response_for_delete_checklist_items()
        return response

    def delete_checklist_items(self, checklist_item_ids: List[str]):
        self.checklist_storage.delete_checklist_items_bulk(
            checklist_item_ids=checklist_item_ids)
