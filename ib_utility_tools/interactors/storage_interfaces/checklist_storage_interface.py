import abc
from typing import Optional

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    ChecklistItemWithChecklistIdDTO, EntityDTO, ChecklistItemWithIdDTO


class ChecklistStorageInterface(abc.ABC):

    def create_checklist_item(self,
                              checklist_item_with_checklist_id_dto:
                              ChecklistItemWithChecklistIdDTO):
        pass

    def get_checklist_id_if_exists(self,
                                   entity_dto: EntityDTO) -> Optional[str]:
        pass

    def create_checklist(self, entity_dto: EntityDTO) -> str:
        pass

    def update_checklist_item(
            self, checklist_item_with_id_dto: ChecklistItemWithIdDTO):
        pass

    def validate_checklist_item_id(self, checklist_item_id: str) -> bool:
        pass
