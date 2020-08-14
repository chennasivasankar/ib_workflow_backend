from ib_utility_tools.interactors.storage_interfaces.checklist_storage_interface import \
    ChecklistStorageInterface


class DeleteChecklistItemsInteractor:
    def __init__(self, checklist_storage: ChecklistStorageInterface):
        self.checklist_storage = checklist_storage

    def delete_checklist_items_wrapper(self, checklist_item_ids: List[str], presenter: DeleteChecklistItemsPresenterInterface):
        pass

    def delete_checklist_items(self, checklist_item_ids):
        pass
