from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.adapters.auth_service import UserProfileDTO
from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.dtos import \
    CommentWithRepliesCountAndEditableDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    UpdateCommentPresenterInterface
from ib_discussions.interactors.storage_interfaces.dtos import \
    CommentIdWithMultiMediaDTO, CommentIdWithMentionUserIdDTO

COMMENT_ID_NOT_FOUND = (
    "Please send valid comment id to update comment",
    "COMMENT_ID_NOT_FOUND"
)

INVALID_USER_IDS = (
    "Please send valid user ids to update comment, invalid user ids are {user_ids}",
    "INVALID_USER_IDS"
)

USER_CANNOT_EDIT_COMMENT = (
    "Please send valid user id to comment id to update comment",
    "USER_CANNOT_EDIT_COMMENT"
)


class UpdateCommentPresenterImplementation(
    UpdateCommentPresenterInterface, HTTPResponseMixin
):

    def prepare_response_for_comment_id_not_found(self):
        response_dict = {
            "response": COMMENT_ID_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": COMMENT_ID_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def response_for_invalid_user_ids(self, err):
        response_dict = {
            "response": INVALID_USER_IDS[0].format(user_ids=err.user_ids),
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_USER_IDS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def prepare_response_for_comment(
            self,
            comment_with_replies_count_and_editable_dto: CommentWithRepliesCountAndEditableDTO,
            user_profile_dtos: List[UserProfileDTO],
            comment_id_with_multimedia_dtos: List[CommentIdWithMultiMediaDTO],
            comment_id_with_mention_user_id_dtos: List[
                CommentIdWithMentionUserIdDTO]
    ):
        from ib_discussions.presenters.create_comment_presenter_implementation import \
            CreateCommentPresenterImplementation
        presenter = CreateCommentPresenterImplementation()

        response = presenter.prepare_response_for_comment(
            comment_id_with_mention_user_id_dtos=comment_id_with_mention_user_id_dtos,
            comment_with_replies_count_and_editable_dto=comment_with_replies_count_and_editable_dto,
            comment_id_with_multimedia_dtos=comment_id_with_multimedia_dtos,
            user_profile_dtos=user_profile_dtos,
        )
        return response

    def response_for_user_cannot_edit_comment(self):
        response_dict = {
            "response": USER_CANNOT_EDIT_COMMENT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": USER_CANNOT_EDIT_COMMENT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
