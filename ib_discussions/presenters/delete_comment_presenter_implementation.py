from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    DeleteCommentPresenterInterface

COMMENT_ID_NOT_FOUND = (
    "Please send valid comment id to delete comment",
    "COMMENT_ID_NOT_FOUND"
)

USER_CANNOT_EDIT_COMMENT = (
    "Please send valid user id to comment id to delete comment",
    "USER_CANNOT_EDIT_COMMENT"
)


class DeleteCommentPresenterImplementation(
    DeleteCommentPresenterInterface, HTTPResponseMixin
):

    def prepare_response_for_comment_id_not_found(self):
        response_dict = {
            "response": COMMENT_ID_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": COMMENT_ID_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def response_for_user_cannot_edit_comment(self):
        response_dict = {
            "response": USER_CANNOT_EDIT_COMMENT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": USER_CANNOT_EDIT_COMMENT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def prepare_response_for_delete_comment(self):
        return self.prepare_200_success_response(response_dict={})
