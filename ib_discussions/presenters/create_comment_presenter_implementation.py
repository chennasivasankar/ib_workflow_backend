from typing import List, Dict

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

INVALID_USER_IDS = (
    "Please send valid mention user ids, invalid user ids are {user_ids}",
    "INVALID_USER_IDS"
)

COMMENT_OR_MULTIMEDIA_SHOULD_BE_PROVIDED = (
    "Please provide comment comment or multimedia to create the comment",
    "COMMENT_OR_MULTIMEDIA_SHOULD_BE_PROVIDED"
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

    def response_for_invalid_user_ids(self, err):
        response_dict = {
            "response": INVALID_USER_IDS[0].format(user_ids=err.user_ids),
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_USER_IDS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def response_for_comment_or_multimedia_should_be_provided(self):
        response_dict = {
            "response": COMMENT_OR_MULTIMEDIA_SHOULD_BE_PROVIDED[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": COMMENT_OR_MULTIMEDIA_SHOULD_BE_PROVIDED[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def prepare_response_for_comment(
            self, user_profile_dtos: List[UserProfileDTO],
            comment_with_replies_count_and_editable_dto: CommentWithRepliesCountAndEditableDTO,
            comment_id_with_multimedia_dtos: List[CommentIdWithMultiMediaDTO],
            comment_id_with_mention_user_id_dtos: List[
                CommentIdWithMentionUserIdDTO]
    ):
        multimedia_list = self._prepare_multimedia_list(
            comment_id_with_multimedia_dtos)
        user_id_wise_user_details_dict = \
            self._prepare_user_id_wise_user_details_dict(
                user_profile_dtos=user_profile_dtos
            )
        mention_users = self._prepare_mention_users_list(
            comment_id_with_mention_user_id_dtos,
            user_id_wise_user_details_dict)

        from ib_discussions.utils.datetime_utils import get_datetime_as_string
        created_at = get_datetime_as_string(
            comment_with_replies_count_and_editable_dto.created_at
        )
        comment_details_dto = comment_with_replies_count_and_editable_dto

        response = {
            "comment_id": str(comment_details_dto.comment_id),
            "comment_content": comment_details_dto.comment_content,
            "author": user_id_wise_user_details_dict[
                comment_with_replies_count_and_editable_dto.user_id
            ],
            "created_at": created_at,
            "total_replies_count": comment_details_dto.replies_count,
            "is_editable": comment_details_dto.is_editable,
            "multimedia": multimedia_list,
            "mention_users": mention_users
        }
        return self.prepare_200_success_response(response_dict=response)

    @staticmethod
    def _prepare_mention_users_list(
            comment_id_with_mention_user_id_dtos: List[
                CommentIdWithMentionUserIdDTO],
            user_id_wise_user_details_dict
    ) -> List[Dict[str, str]]:
        mention_users = [
            user_id_wise_user_details_dict[
                comment_id_with_mention_user_id_dto.mention_user_id
            ]
            for comment_id_with_mention_user_id_dto in
            comment_id_with_mention_user_id_dtos
        ]
        return mention_users

    @staticmethod
    def _prepare_multimedia_list(
            comment_id_with_multimedia_dtos: List[CommentIdWithMultiMediaDTO]
    ) -> List[Dict[str, str]]:
        multimedia_list = [
            {
                "multimedia_id": str(multimedia_dto.multimedia_id),
                "format_type": multimedia_dto.format_type,
                "url": multimedia_dto.url,
                "thumbnail_url": multimedia_dto.thumbnail_url
            }
            for multimedia_dto in comment_id_with_multimedia_dtos
        ]
        return multimedia_list

    @staticmethod
    def _prepare_user_id_wise_user_details_dict(
            user_profile_dtos: List[UserProfileDTO]
    ) -> Dict[str, Dict[str, str]]:
        user_id_wise_user_details_dict = {
            str(user_profile_dto.user_id): {
                "user_id": str(user_profile_dto.user_id),
                "name": user_profile_dto.name,
                "profile_pic_url": user_profile_dto.profile_pic_url
            }
            for user_profile_dto in user_profile_dtos
        }
        return user_id_wise_user_details_dict
