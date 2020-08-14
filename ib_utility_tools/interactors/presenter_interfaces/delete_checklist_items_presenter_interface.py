import abc


class DeleteChecklistItemsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_delete_checklist_items(self):
        pass

    @abc.abstractmethod
    def get_duplicate_checklist_item_ids_for_delete_checklist_items(self):
        pass

    @abc.abstractmethod
    def get_invalid_checklist_item_ids_for_delete_checklist_items(self):
        pass
