import abc


class CreateChecklistItemPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_create_checklist_item(self,
                                                       checklist_item_id: str):
        pass

    @abc.abstractmethod
    def get_response_for_empty_checklist_item_text_exception(self):
        pass
