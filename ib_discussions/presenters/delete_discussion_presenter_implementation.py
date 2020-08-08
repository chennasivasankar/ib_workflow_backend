from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    DeleteDiscussionPresenterInterface

DISCUSSION_ID_NOT_FOUND = (
    "Please send valid discussion id to delete discussion",
    "DISCUSSION_ID_NOT_FOUND"
)

USER_CANNOT_DELETE_DISCUSSION = (
    "User cannot delete discussion",
    "USER_CANNOT_DELETE_DISCUSSION"
)


class DeleteDiscussionPresenterImplementation(
    DeleteDiscussionPresenterInterface, HTTPResponseMixin
):

    def response_for_discussion_id_not_found(self):
        response_dict = {
            "response": DISCUSSION_ID_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": DISCUSSION_ID_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def response_for_user_cannot_delete_discussion(self):
        response_dict = {
            "response": USER_CANNOT_DELETE_DISCUSSION[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": USER_CANNOT_DELETE_DISCUSSION[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def prepare_success_response_for_delete_discussion(self):
        return self.prepare_201_created_response(response_dict={})
