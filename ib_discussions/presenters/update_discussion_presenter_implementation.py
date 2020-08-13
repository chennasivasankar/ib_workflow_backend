from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    UpdateDiscussionPresenterInterface

EMPTY_TITLE = (
    "Please send title with content",
    "EMPTY_TITLE"
)

DISCUSSION_ID_NOT_FOUND = (
    "Please send valid discussion id to update discussion",
    "DISCUSSION_ID_NOT_FOUND"
)

USER_CANNOT_UPDATE_DISCUSSION = (
    "User cannot update discussion",
    "USER_CANNOT_UPDATE_DISCUSSION"
)


class UpdateDiscussionPresenterImplementation(
    UpdateDiscussionPresenterInterface, HTTPResponseMixin):

    def response_for_empty_title(self):
        response_dict = {
            "response": EMPTY_TITLE[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": EMPTY_TITLE[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_discussion_id_not_found(self):
        response_dict = {
            "response": DISCUSSION_ID_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": DISCUSSION_ID_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def response_for_user_cannot_update_discussion(self):
        response_dict = {
            "response": USER_CANNOT_UPDATE_DISCUSSION[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": USER_CANNOT_UPDATE_DISCUSSION[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def prepare_success_response_for_update_discussion(self):
        return self.prepare_200_success_response(response_dict={})
