from ib_utility_tools.constants.enum import EntityType
from ib_utility_tools.interactors.presenter_interfaces \
    .checklist_presenter_interface import CreateChecklistItemPresenterInterface
from ib_utility_tools.interactors.storage_interfaces \
    .checklist_storage_interface import ChecklistStorageInterface
from ib_utility_tools.interactors.storage_interfaces.dtos import \
    ChecklistItemWithEntityDTO


class CreateChecklistItemInteractor:

    def __init__(self, checklist_storage: ChecklistStorageInterface):
        self.checklist_storage = checklist_storage

    def create_checklist_item_wrapper(
            self, checklist_item_with_entity_dto: ChecklistItemWithEntityDTO,
            presenter: CreateChecklistItemPresenterInterface
    ):
        checklist_item_id = self.create_checklist_item(
            checklist_item_with_entity_dto=checklist_item_with_entity_dto
        )
        return presenter.get_response_for_create_checklist_item(
            checklist_item_id=checklist_item_id
        )

    def create_checklist_item(
            self, checklist_item_with_entity_dto: ChecklistItemWithEntityDTO
    ) -> str:
        checklist_id = self._get_or_create_checklist_for_given_entity_details(
            entity_id=checklist_item_with_entity_dto.entity_id,
            entity_type=checklist_item_with_entity_dto.entity_type
        )
        from ib_utility_tools.interactors.storage_interfaces.dtos import \
            ChecklistItemWithChecklistIdDTO
        checklist_item_with_checklist_id_dto = ChecklistItemWithChecklistIdDTO(
            checklist_id=checklist_id,
            text=checklist_item_with_entity_dto.text,
            is_checked=checklist_item_with_entity_dto.is_checked
        )
        return self.checklist_storage.create_checklist_item(
            checklist_item_with_checklist_id_dto=
            checklist_item_with_checklist_id_dto
        )

    def _get_or_create_checklist_for_given_entity_details(
            self, entity_id: str, entity_type: EntityType
    ) -> str:
        from ib_utility_tools.interactors.storage_interfaces.dtos import (
            EntityDTO
        )
        entity_dto = EntityDTO(entity_id=entity_id, entity_type=entity_type)
        checklist_id = self.checklist_storage.get_checklist_id_if_exists(
            entity_dto=entity_dto
        )
        if checklist_id is None:
            checklist_id = self.checklist_storage.create_checklist(
                entity_dto=entity_dto
            )
        return checklist_id
