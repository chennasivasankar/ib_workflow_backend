from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.adapters.auth_service import UserProfileDTO
from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.dtos import \
    CommentWithRepliesCountAndEditableDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    CreateCommentPresenterInterface
from ib_discussions.interactors.storage_interfaces.dtos import \
    CommentIdWithMultiMediaDTO, CommentIdWithMentionUserIdDTO

DISCUSSION_ID_NOT_FOUND = (
    "Please send valid discussion id to create comment for discussion",
    "DISCUSSION_ID_NOT_FOUND"
)


class CreateCommentPresenterImplementation(CreateCommentPresenterInterface,
                                           HTTPResponseMixin):

    def response_for_discussion_id_not_found(self):
        response_dict = {
            "response": DISCUSSION_ID_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": DISCUSSION_ID_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def prepare_response_for_comment(
            self,
            comment_with_replies_count_and_editable_dto: CommentWithRepliesCountAndEditableDTO,
            user_profile_dtos: List[UserProfileDTO],
            comment_id_with_multi_media_dtos: List[CommentIdWithMultiMediaDTO],
            comment_id_with_mention_user_id_dtos: List[
                CommentIdWithMentionUserIdDTO]
    ):
        # TODO: Optimise to 20 line function
        from ib_discussions.utils.datetime_utils import get_datetime_as_string
        comment_id = comment_with_replies_count_and_editable_dto.comment_id
        comment_content = comment_with_replies_count_and_editable_dto. \
            comment_content
        created_at = get_datetime_as_string(
            comment_with_replies_count_and_editable_dto.created_at
        )
        replies_count = comment_with_replies_count_and_editable_dto. \
            replies_count
        is_editable = comment_with_replies_count_and_editable_dto.is_editable

        multi_media_list = [
            {
                "multi_media_id": str(multi_media_dto.multi_media_id),
                "format_type": multi_media_dto.format_type,
                "url": multi_media_dto.url
            }
            for multi_media_dto in comment_id_with_multi_media_dtos
        ]

        user_id_wise_user_details_dict = \
            self._prepare_user_id_wise_user_details_dict(
                user_profile_dtos=user_profile_dtos
            )
        mention_users = [
            user_id_wise_user_details_dict[
                comment_id_with_mention_user_id_dto.mention_user_id
            ]
            for comment_id_with_mention_user_id_dto in
            comment_id_with_mention_user_id_dtos
        ]
        response = {
            "comment_id": str(comment_id),
            "comment_content": comment_content,
            "author": user_id_wise_user_details_dict[
                comment_with_replies_count_and_editable_dto.user_id
            ],
            "created_at": created_at,
            "total_replies_count": replies_count,
            "is_editable": is_editable,
            "multi_media": multi_media_list,
            "mention_users": mention_users
        }
        print(multi_media_list)
        return self.prepare_200_success_response(response_dict=response)

    @staticmethod
    def _prepare_user_id_wise_user_details_dict(
            user_profile_dtos: List[UserProfileDTO]):
        user_id_wise_user_details_dict = {
            str(user_profile_dto.user_id): {
                "user_id": str(user_profile_dto.user_id),
                "name": user_profile_dto.name,
                "profile_pic_url": user_profile_dto.profile_pic_url
            }
            for user_profile_dto in user_profile_dtos
        }
        return user_id_wise_user_details_dict
