from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    CreateDiscussionPresenterInterface

INVALID_OFFSET = (
    "Please send the valid offset value",
    "INVALID_OFFSET"
)

INVALID_LIMIT = (
    "Please send the valid limit value",
    "INVALID_LIMIT"
)

EMPTY_TITLE = (
    "Please send valid title, your title is empty",
    "EMPTY_TITLE"
)


class CreateDiscussionPresenterImplementation(
    CreateDiscussionPresenterInterface, HTTPResponseMixin
):

    def response_for_empty_title(self):
        response_dict = {
            "response": EMPTY_TITLE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": EMPTY_TITLE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def prepare_success_response_for_create_discussion(self):
        return self.prepare_201_created_response(response_dict={})
