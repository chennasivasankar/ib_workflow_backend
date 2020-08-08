from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_utility_tools.interactors.presenter_interfaces \
    .get_checklist_presenter_interface import GetChecklistPresenterInterface
from ib_utility_tools.interactors.storage_interfaces.dtos import \
    ChecklistItemWithIdDTO, EntityDTO


class GetChecklistPresenterImplementation(GetChecklistPresenterInterface,
                                          HTTPResponseMixin):

    def get_success_response_for_get_checklist(
            self, entity_dto: EntityDTO,
            checklist_item_dtos: List[ChecklistItemWithIdDTO]):
        checklist_items = self._prepare_checklist_items(
            checklist_item_dtos=checklist_item_dtos)
        checklist_items_with_entity_details_dict = {
            "entity_id": entity_dto.entity_id,
            "entity_type": entity_dto.entity_type,
            "checklist": checklist_items
        }
        return self.prepare_200_success_response(
            response_dict=checklist_items_with_entity_details_dict)

    def _prepare_checklist_items(
            self, checklist_item_dtos: List[ChecklistItemWithIdDTO]):
        checklist_items = [
            self._prepare_checklist_item_dict(checklist_item_dto)
            for checklist_item_dto in checklist_item_dtos
        ]
        return checklist_items

    @staticmethod
    def _prepare_checklist_item_dict(
            checklist_item_dto: ChecklistItemWithIdDTO):
        checklist_item_dict = {
            "checklist_item_id": checklist_item_dto.checklist_item_id,
            "text": checklist_item_dto.text,
            "is_checked": checklist_item_dto.is_checked
        }
        return checklist_item_dict
