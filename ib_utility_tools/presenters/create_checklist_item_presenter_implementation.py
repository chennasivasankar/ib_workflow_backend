from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_utility_tools.constants.enum import StatusCode
from ib_utility_tools.interactors.presenter_interfaces \
    .create_checklist_item_presenter_interface import \
    CreateChecklistItemPresenterInterface


class CreateChecklistItemPresenterImplementation(
    CreateChecklistItemPresenterInterface, HTTPResponseMixin):

    def get_success_response_for_create_checklist_item(self,
                                                       checklist_item_id: str):
        return self.prepare_201_created_response(
            response_dict={"checklist_item_id": checklist_item_id})

    def get_response_for_empty_checklist_item_text_exception(self):
        from ib_utility_tools.constants.exception_messages import \
            EMPTY_CHECKLIST_ITEM_TEXT_FOR_CREATE_CHECKLIST_ITEM
        response_dict = {
            "response": EMPTY_CHECKLIST_ITEM_TEXT_FOR_CREATE_CHECKLIST_ITEM[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status":
                EMPTY_CHECKLIST_ITEM_TEXT_FOR_CREATE_CHECKLIST_ITEM[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
