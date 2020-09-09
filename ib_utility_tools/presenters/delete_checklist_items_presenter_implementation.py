from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from ib_utility_tools.interactors.presenter_interfaces.checklist_presenter_interface import (
    DeleteChecklistItemsPresenterInterface
)
from ib_utility_tools.constants.enum import StatusCode


class DeleteChecklistItemsPresenterImplementation(
    DeleteChecklistItemsPresenterInterface, HTTPResponseMixin
):

    def get_response_for_delete_checklist_items(self):
        return self.prepare_200_success_response(response_dict={})

    def response_for_duplicate_checklist_item_ids_exception(self):
        from ib_utility_tools.constants.exception_messages import (
            DUPLICATE_CHECKLIST_ITEM_IDS
        )
        response_dict = {
            "response": DUPLICATE_CHECKLIST_ITEM_IDS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": DUPLICATE_CHECKLIST_ITEM_IDS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_invalid_checklist_item_ids_exception(self):
        from ib_utility_tools.constants.exception_messages import (
            INVALID_CHECKLIST_ITEM_IDS
        )
        response_dict = {
            "response": INVALID_CHECKLIST_ITEM_IDS[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_CHECKLIST_ITEM_IDS[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)
