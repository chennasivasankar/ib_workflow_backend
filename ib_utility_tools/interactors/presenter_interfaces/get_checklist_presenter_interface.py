import abc
from typing import List

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    ChecklistItemWithIdDTO


class GetChecklistPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_success_response_for_get_checklist(
            self, checklist_item_dtos: List[ChecklistItemWithIdDTO]):
        pass
