from ib_utility_tools.exceptions.custom_exceptions import \
    ChecklistItemIdNotFound
from ib_utility_tools.interactors.presenter_interfaces \
    .checklist_presenter_interface import UpdateChecklistItemPresenterInterface
from ib_utility_tools.interactors.storage_interfaces \
    .checklist_storage_interface import ChecklistStorageInterface
from ib_utility_tools.interactors.storage_interfaces.dtos import \
    ChecklistItemWithIdDTO


class UpdateChecklistItemInteractor:
    def __init__(self, checklist_storage: ChecklistStorageInterface):
        self.checklist_storage = checklist_storage

    def update_checklist_item_wrapper(
            self, checklist_item_with_id_dto: ChecklistItemWithIdDTO,
            presenter: UpdateChecklistItemPresenterInterface):
        try:
            self.update_checklist_item(
                checklist_item_with_id_dto=checklist_item_with_id_dto)
            response = \
                presenter.get_success_response_for_update_checklist_item()
        except ChecklistItemIdNotFound:
            response = presenter.get_checklist_item_id_not_found_response()
        return response

    def update_checklist_item(
            self, checklist_item_with_id_dto: ChecklistItemWithIdDTO):
        checklist_item_id = checklist_item_with_id_dto.checklist_item_id
        self._validate_checklist_item_id(checklist_item_id=checklist_item_id)
        self.checklist_storage.update_checklist_item(
            checklist_item_with_id_dto=checklist_item_with_id_dto)

    def _validate_checklist_item_id(self, checklist_item_id: str):
        is_checklist_item_id_exist = self.checklist_storage \
            .is_checklist_item_id_exists(checklist_item_id=checklist_item_id)
        if is_checklist_item_id_exist is False:
            raise ChecklistItemIdNotFound
