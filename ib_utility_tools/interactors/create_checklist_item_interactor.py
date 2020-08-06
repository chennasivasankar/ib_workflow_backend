from ib_utility_tools.interactors.dtos.dtos import \
    ChecklistItemWithEntityDetailsDTO
from ib_utility_tools.interactors.storage_interfaces \
    .checklist_storage_interface import ChecklistStorageInterface


class CreateChecklistItemInteractor:
    def __init__(self, checklist_storage: ChecklistStorageInterface):
        self.checklist_storage = checklist_storage

    def create_checklist_item_wrapper(self,
                                      checklist_item_with_entity_details_dto:
                                      ChecklistItemWithEntityDetailsDTO):
        pass

    def create_checklist_item(self):
        pass
