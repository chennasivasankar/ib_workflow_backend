from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_utility_tools.constants.enum import StatusCode
from ib_utility_tools.interactors.presenter_interfaces.checklist_presenter_interface import (
    UpdateChecklistItemPresenterInterface
)


class UpdateChecklistItemPresenterImplementation(
    UpdateChecklistItemPresenterInterface, HTTPResponseMixin
):

    def get_success_response_for_update_checklist_item(self):
        return self.prepare_200_success_response(response_dict={})

    def get_checklist_item_id_not_found_response(self):
        from ib_utility_tools.constants.exception_messages import (
            CHECKLIST_ITEM_ID_NOT_FOUND_FOR_UPDATE_CHECKLIST_ITEM as checklist_item_id_not_found
        )
        response_dict = {"response": checklist_item_id_not_found[0],
                         "http_status_code": StatusCode.BAD_REQUEST.value,
                         "res_status": checklist_item_id_not_found[1]
                         }
        return self.prepare_404_not_found_response(response_dict=response_dict)
