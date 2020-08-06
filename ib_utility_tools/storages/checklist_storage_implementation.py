from typing import Optional, List

from ib_utility_tools.interactors.storage_interfaces \
    .checklist_storage_interface import ChecklistStorageInterface
from ib_utility_tools.interactors.storage_interfaces.dtos import \
    ChecklistItemWithChecklistIdDTO, EntityDTO, ChecklistItemWithIdDTO
from ib_utility_tools.models import ChecklistItem, Checklist


class ChecklistStorageImplementation(ChecklistStorageInterface):

    def create_checklist_item(self,
                              checklist_item_with_checklist_id_dto:
                              ChecklistItemWithChecklistIdDTO):
        checklist_item_object = ChecklistItem.objects.create(
            checklist_id=checklist_item_with_checklist_id_dto.checklist_id,
            text=checklist_item_with_checklist_id_dto.text,
            is_checked=checklist_item_with_checklist_id_dto.is_checked)
        return str(checklist_item_object.checklist_item_id)

    def get_checklist_id_if_exists(self,
                                   entity_dto: EntityDTO) -> Optional[str]:
        try:
            Checklist.objects.get(entity_id=entity_dto.entity_id,
                                  entity_type=entity_dto.entity_type)
        except Checklist.DoesNotExist:
            return None

    def create_checklist(self, entity_dto: EntityDTO) -> str:
        checklist_object = Checklist.objects.create(
            entity_id=entity_dto.entity_id, entity_type=entity_dto.entity_type)
        return checklist_object.id

    def update_checklist_item(
            self, checklist_item_with_id_dto: ChecklistItemWithIdDTO):
        ChecklistItem.objects.filter(
            checklist_item_id=checklist_item_with_id_dto.checklist_item_id
        ).update(
            text=checklist_item_with_id_dto.text,
            is_checked=checklist_item_with_id_dto.is_checked)

    def validate_checklist_item_id(self, checklist_item_id: str) -> bool:
        is_checklist_item_exists = ChecklistItem.objects.get(
            checklist_item_id=checklist_item_id).exists()
        return is_checklist_item_exists

    def get_checklist_items_dto(self, checklist_id: str) -> \
            List[ChecklistItemWithIdDTO]:
        checklist_item_objects = ChecklistItem.objects.filter(
            checklist_id=checklist_id)
        checklist_item_dtos = [
            self._prepare_checklist_item_dto_from_checklist_item_object(
                checklist_item_object=checklist_item_object
            ) for checklist_item_object in checklist_item_objects
        ]
        return checklist_item_dtos

    @staticmethod
    def _prepare_checklist_item_dto_from_checklist_item_object(
            checklist_item_object) -> ChecklistItemWithIdDTO:
        checklist_item_with_id_dto = ChecklistItemWithIdDTO(
            checklist_item_id=checklist_item_object.checklist_item_id,
            text=checklist_item_object.text,
            is_checked=checklist_item_object.is_checked)
        return checklist_item_with_id_dto
