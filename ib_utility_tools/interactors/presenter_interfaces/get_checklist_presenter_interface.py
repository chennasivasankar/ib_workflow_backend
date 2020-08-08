import abc
from typing import List

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    ChecklistItemWithIdDTO, EntityDTO


class GetChecklistPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_success_response_for_get_checklist(
            self, entity_dto: EntityDTO,
            checklist_item_dtos: List[ChecklistItemWithIdDTO]):
        pass
