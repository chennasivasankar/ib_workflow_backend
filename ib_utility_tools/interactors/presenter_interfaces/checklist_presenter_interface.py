import abc
from typing import List

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    ChecklistItemWithIdDTO


class DeleteChecklistItemsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_delete_checklist_items(self):
        pass

    @abc.abstractmethod
    def get_response_for_duplicate_checklist_item_ids_exception(self):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_checklist_item_ids_exception(self):
        pass


class CreateChecklistItemPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_create_checklist_item(self, checklist_item_id: str):
        pass


class GetChecklistPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_checklist(
            self, checklist_item_dtos: List[ChecklistItemWithIdDTO]
    ):
        pass


class UpdateChecklistItemPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_update_checklist_item(self):
        pass

    @abc.abstractmethod
    def get_checklist_item_id_not_found_response(self):
        pass
