from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    CreateDiscussionPresenterInterface

ENTITY_ID_NOT_FOUND = (
    "Please send valid entity id",
    "ENTITY_ID_NOT_FOUND"
)

INVALID_ENTITY_TYPE_FOR_ENTITY_ID = (
    "Please valid entity type for entity id",
    "INVALID_ENTITY_TYPE_FOR_ENTITY_ID"
)

INVALID_OFFSET = (
    "Please send the valid offset value",
    "INVALID_OFFSET"
)

INVALID_LIMIT = (
    "Please send the valid limit value",
    "INVALID_LIMIT"
)


class CreateDiscussionPresenterImplementation(CreateDiscussionPresenterInterface, HTTPResponseMixin):
    def raise_exception_for_entity_id_not_found(self):
        response_dict = {
            "response": ENTITY_ID_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": ENTITY_ID_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def raise_exception_for_invalid_entity_type_for_entity_id(self):
        response_dict = {
            "response": INVALID_ENTITY_TYPE_FOR_ENTITY_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_ENTITY_TYPE_FOR_ENTITY_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def prepare_success_response_for_create_discussion(self):
        return self.prepare_201_created_response(response_dict={})
