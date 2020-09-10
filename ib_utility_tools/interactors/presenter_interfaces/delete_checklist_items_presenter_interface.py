import abc


class DeleteChecklistItemsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_delete_checklist_items(self):
        pass

    @abc.abstractmethod
    def response_for_duplicate_checklist_item_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_checklist_item_ids_exception(self):
        pass
