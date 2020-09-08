from typing import List
from ib_utility_tools.interactors.presenter_interfaces.checklist_presenter_interface import (
    GetChecklistPresenterInterface
)
from ib_utility_tools.interactors.storage_interfaces.checklist_storage_interface import (
    ChecklistStorageInterface
)
from ib_utility_tools.interactors.storage_interfaces.dtos import (
    EntityDTO, ChecklistItemWithIdDTO
)


class GetChecklistInteractor:
    def __init__(self, checklist_storage: ChecklistStorageInterface):
        self.checklist_storage = checklist_storage

    def get_checklist_wrapper(
            self, entity_dto: EntityDTO,
            presenter: GetChecklistPresenterInterface
    ):
        checklist_item_dtos = self.get_checklist(entity_dto=entity_dto)
        return presenter.get_response_for_get_checklist(
            checklist_item_dtos=checklist_item_dtos
        )

    def get_checklist(
            self, entity_dto: EntityDTO
    ) -> List[ChecklistItemWithIdDTO]:
        checklist_id = self.checklist_storage.get_checklist_id_if_exists(
            entity_dto=entity_dto
        )
        if checklist_id is None:
            return []
        checklist_item_dtos = self.checklist_storage.get_checklist_item_dtos(
            checklist_id=checklist_id
        )
        return checklist_item_dtos
