import abc


class UpdateChecklistItemPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_update_checklist_item(self):
        pass

    @abc.abstractmethod
    def get_checklist_item_id_not_found_response(self):
        pass

    @abc.abstractmethod
    def get_response_for_empty_checklist_item_text_exception(self):
        pass
