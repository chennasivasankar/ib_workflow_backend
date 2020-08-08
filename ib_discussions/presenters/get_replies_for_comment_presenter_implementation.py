import json
from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.adapters.auth_service import UserProfileDTO
from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.dtos import \
    CommentIdWithEditableStatusDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    GetRepliesForCommentPresenterInterface
from ib_discussions.interactors.storage_interfaces.dtos import CommentDTO

COMMENT_ID_NOT_FOUND = (
    "Please send valid comment id to get replies for comment",
    "COMMENT_ID_NOT_FOUND"
)


class GetRepliesForCommentPresenterImplementation(
    GetRepliesForCommentPresenterInterface, HTTPResponseMixin
):

    def response_for_comment_id_not_found(self):
        response_dict = {
            "response": COMMENT_ID_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": COMMENT_ID_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def prepare_response_for_replies_with_users_dtos(
            self, user_profile_dtos: List[UserProfileDTO],
            comment_with_editable_status_dtos: List[
                CommentIdWithEditableStatusDTO],
            comment_dtos: List[CommentDTO]
    ):
        user_id_wise_user_profile_dto_dict = {
            user_profile_dto.user_id: user_profile_dto
            for user_profile_dto in user_profile_dtos
        }

        comment_id_wise_editable_status_dto_dict = {
            comment_with_editable_status_dto.comment_id: comment_with_editable_status_dto
            for comment_with_editable_status_dto in
            comment_with_editable_status_dtos
        }

        replies = [
            self._prepare_response_for_reply(
                comment_dto=comment_dto,
                comment_with_editable_status_dto= \
                    comment_id_wise_editable_status_dto_dict[
                        comment_dto.comment_id],
                user_profile_dto=user_id_wise_user_profile_dto_dict[
                    comment_dto.user_id]
            )
            for comment_dto in comment_dtos
        ]
        response_dict = {
            "replies": replies
        }
        return self.prepare_200_success_response(response_dict=response_dict)

    @staticmethod
    def _prepare_response_for_reply(
            comment_dto: CommentDTO,
            comment_with_editable_status_dto: CommentIdWithEditableStatusDTO,
            user_profile_dto: UserProfileDTO):
        from ib_discussions.presenters.create_reply_presenter_implementation import \
            CreateReplyPresenterImplementation
        presenter = CreateReplyPresenterImplementation()
        response_object = presenter.prepare_response_for_reply(
            comment_dto=comment_dto, user_profile_dto=user_profile_dto,
            comment_with_editable_status_dto=comment_with_editable_status_dto
        )
        response_dict = json.loads(response_object.content)
        return response_dict
