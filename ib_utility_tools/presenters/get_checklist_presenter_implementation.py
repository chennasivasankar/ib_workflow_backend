from typing import List
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from ib_utility_tools.interactors.presenter_interfaces.get_checklist_presenter_interface import (
    GetChecklistPresenterInterface
)
from ib_utility_tools.interactors.storage_interfaces.dtos import (
    ChecklistItemWithIdDTO
)


class GetChecklistPresenterImplementation(
    GetChecklistPresenterInterface, HTTPResponseMixin
):
    def get_response_for_get_checklist(
            self, checklist_item_dtos: List[ChecklistItemWithIdDTO]
    ):
        checklist_items = self._convert_to_checklist_items_dict(
            checklist_item_dtos=checklist_item_dtos
        )
        return self.prepare_200_success_response(
            response_dict={"checklist": checklist_items}
        )

    def _convert_to_checklist_items_dict(
            self, checklist_item_dtos: List[ChecklistItemWithIdDTO]
    ) -> List[dict]:
        checklist_items = [
            self._convert_checklist_item_dict(checklist_item_dto)
            for checklist_item_dto in checklist_item_dtos
        ]
        return checklist_items

    @staticmethod
    def _convert_checklist_item_dict(
            checklist_item_dto: ChecklistItemWithIdDTO
    ) -> dict:
        checklist_item_dict = {
            "checklist_item_id": checklist_item_dto.checklist_item_id,
            "text": checklist_item_dto.text,
            "is_checked": checklist_item_dto.is_checked
        }
        return checklist_item_dict
