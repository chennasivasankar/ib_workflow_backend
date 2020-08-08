from ib_utility_tools.exceptions.custom_exceptions import \
    EmptyChecklistItemText, ChecklistItemIdNotFound
from ib_utility_tools.interactors.presenter_interfaces \
    .update_checklist_item_presenter_interface import \
    UpdateChecklistItemPresenterInterface
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
        except EmptyChecklistItemText:
            response = presenter \
                .get_response_for_empty_checklist_item_text_exception()
        return response

    def update_checklist_item(
            self, checklist_item_with_id_dto: ChecklistItemWithIdDTO):
        checklist_item_text = checklist_item_with_id_dto.text
        checklist_item_id = checklist_item_with_id_dto.checklist_item_id
        self._validate_checklist_item_text(text=checklist_item_text)
        self._validate_checklist_item_id(checklist_item_id=checklist_item_id)
        self.checklist_storage.update_checklist_item(
            checklist_item_with_id_dto=checklist_item_with_id_dto)

    @staticmethod
    def _validate_checklist_item_text(text: str):
        is_text_empty = not text
        is_text_contains_only_white_spaces = text.isspace()
        if is_text_empty or is_text_contains_only_white_spaces:
            raise EmptyChecklistItemText

    def _validate_checklist_item_id(self, checklist_item_id: str):
        is_checklist_item_id_exist = self.checklist_storage \
            .validate_checklist_item_id(checklist_item_id=checklist_item_id)
        if is_checklist_item_id_exist is False:
            raise ChecklistItemIdNotFound
