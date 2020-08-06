import json
from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.adapters.auth_service import UserProfileDTO
from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.dtos import \
    CommentWithRepliesCountAndEditableDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    GetCommentsForDiscussionPresenterInterface

DISCUSSION_ID_NOT_FOUND = (
    "Please send valid discussion id to get comments for discussion",
    "DISCUSSION_ID_NOT_FOUND"
)


class GetCommentsForDiscussionPresenterImplementation(
    GetCommentsForDiscussionPresenterInterface, HTTPResponseMixin
):

    def response_for_discussion_id_not_found(self):
        response_dict = {
            "response": DISCUSSION_ID_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": DISCUSSION_ID_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def prepare_response_for_comments_with_users_dtos(
            self,
            comment_with_replies_count_and_editable_dtos: List[
                CommentWithRepliesCountAndEditableDTO],
            user_profile_dtos: List[UserProfileDTO]
    ):
        user_id_wise_user_profile_dto_dict = {
            user_profile_dto.user_id: user_profile_dto
            for user_profile_dto in user_profile_dtos
        }
        comments_details_list = [
            self._prepare_response_for_comment(
                comment_with_replies_count_and_editable_dto\
                    =comment_with_replies_count_and_editable_dto,
                user_profile_dto=user_id_wise_user_profile_dto_dict[
                    comment_with_replies_count_and_editable_dto.user_id
                ]
            )
            for comment_with_replies_count_and_editable_dto in
            comment_with_replies_count_and_editable_dtos
        ]
        response = {
            "comments": comments_details_list
        }
        return self.prepare_200_success_response(
            response_dict=response)

    @staticmethod
    def _prepare_response_for_comment(
            comment_with_replies_count_and_editable_dto: CommentWithRepliesCountAndEditableDTO,
            user_profile_dto: UserProfileDTO
    ):
        from ib_discussions.presenters.create_comment_presenter_implementation import \
            CreateCommentPresenterImplementation
        presenter = CreateCommentPresenterImplementation()
        response = presenter.prepare_response_for_comment(
            comment_with_replies_count_and_editable_dto\
                =comment_with_replies_count_and_editable_dto,
            user_profile_dto=user_profile_dto
        )
        response_dict = json.loads(response.content)
        return response_dict
