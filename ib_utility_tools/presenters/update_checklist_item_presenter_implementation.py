from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_utility_tools.constants.enum import StatusCode
from ib_utility_tools.interactors.presenter_interfaces \
    .update_checklist_item_presenter_interface import \
    UpdateChecklistItemPresenterInterface


class UpdateChecklistItemPresenterImplementation(
    UpdateChecklistItemPresenterInterface, HTTPResponseMixin
):

    def get_success_response_for_update_checklist_item(self):
        return self.prepare_200_success_response(response_dict={})

    def get_checklist_item_id_not_found_response(self):
        from ib_utility_tools.constants.exception_messages import \
            CHECKLIST_ITEM_ID_NOT_FOUND_FOR_UPDATE_CHECKLIST_ITEM
        response_dict = {
            "response":
                CHECKLIST_ITEM_ID_NOT_FOUND_FOR_UPDATE_CHECKLIST_ITEM[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status":
                CHECKLIST_ITEM_ID_NOT_FOUND_FOR_UPDATE_CHECKLIST_ITEM[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def response_for_empty_checklist_item_text_exception(self):
        from ib_utility_tools.constants.exception_messages import \
            EMPTY_CHECKLIST_ITEM_TEXT_FOR_UPDATE_CHECKLIST_ITEM
        response_dict = {
            "response": EMPTY_CHECKLIST_ITEM_TEXT_FOR_UPDATE_CHECKLIST_ITEM[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status":
                EMPTY_CHECKLIST_ITEM_TEXT_FOR_UPDATE_CHECKLIST_ITEM[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
