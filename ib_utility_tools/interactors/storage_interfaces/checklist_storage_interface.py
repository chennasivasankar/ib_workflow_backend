import abc
from typing import Optional, List

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    ChecklistItemWithChecklistIdDTO, EntityDTO, ChecklistItemWithIdDTO


class ChecklistStorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_checklist_item(self,
                              checklist_item_with_checklist_id_dto:
                              ChecklistItemWithChecklistIdDTO):
        pass

    @abc.abstractmethod
    def get_checklist_id_if_exists(self,
                                   entity_dto: EntityDTO) -> Optional[str]:
        pass

    @abc.abstractmethod
    def create_checklist(self, entity_dto: EntityDTO) -> str:
        pass

    @abc.abstractmethod
    def update_checklist_item(
            self, checklist_item_with_id_dto: ChecklistItemWithIdDTO):
        pass

    @abc.abstractmethod
    def is_checklist_item_id_exists(self, checklist_item_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_checklist_item_dtos(self, checklist_id: str) -> \
            List[ChecklistItemWithIdDTO]:
        pass
