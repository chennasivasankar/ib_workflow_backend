import abc


class DeleteChecklistItemsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_delete_checklist_items(self):
        pass

