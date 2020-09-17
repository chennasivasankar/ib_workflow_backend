from collections import defaultdict
from typing import List, Dict

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.adapters.auth_service import UserProfileDTO
from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.dtos import \
    CommentWithRepliesCountAndEditableDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    GetCommentsForDiscussionPresenterInterface
from ib_discussions.interactors.storage_interfaces.dtos import \
    CommentIdWithMultiMediaDTO, CommentIdWithMentionUserIdDTO

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
            self, user_profile_dtos: List[UserProfileDTO],
            comment_with_replies_count_and_editable_dtos: List[
                CommentWithRepliesCountAndEditableDTO],
            comment_id_with_multimedia_dtos: List[CommentIdWithMultiMediaDTO],
            comment_id_with_mention_user_id_dtos: List[
                CommentIdWithMentionUserIdDTO]
    ):
        user_id_wise_user_details_dict = \
            self._prepare_user_id_wise_user_details_dict(
                user_profile_dtos=user_profile_dtos
            )
        comment_id_wise_multimedia_list_dict = \
            self._prepare_comment_id_wise_multimedia_list_dict(
                comment_id_with_multimedia_dtos=comment_id_with_multimedia_dtos
            )
        comment_id_wise_mention_user_details_list_dict = \
            self._prepare_comment_id_wise_mention_user_details_list(
                comment_id_with_mention_user_id_dtos=comment_id_with_mention_user_id_dtos,
                user_id_wise_user_details_dict=user_id_wise_user_details_dict
            )
        comments_details_list = [
            self._prepare_comment_details_dict(
                comment_details_dto,
                comment_id_wise_mention_user_details_list_dict,
                comment_id_wise_multimedia_list_dict,
                user_id_wise_user_details_dict)
            for comment_details_dto in
            comment_with_replies_count_and_editable_dtos
        ]
        response = {
            "comments": comments_details_list
        }
        return self.prepare_200_success_response(response_dict=response)

    @staticmethod
    def _prepare_comment_details_dict(
            comment_details_dto,
            comment_id_wise_mention_user_details_list_dict: Dict[
                str, List[Dict[str, str]]],
            comment_id_wise_multimedia_list_dict: Dict[
                str, List[Dict[str, str]]],
            user_id_wise_user_details_dict: Dict[str, Dict[str, str]]
    ):
        comment_id = str(comment_details_dto.comment_id)
        from ib_discussions.utils.datetime_utils import get_datetime_as_string
        comment_details_dict = {
            "comment_id": comment_id,
            "comment_content": comment_details_dto.comment_content,
            "author": user_id_wise_user_details_dict[
                comment_details_dto.user_id
            ],
            "created_at": get_datetime_as_string(
                comment_details_dto.created_at
            ),
            "total_replies_count": comment_details_dto.replies_count,
            "is_editable": comment_details_dto.is_editable,
            "multimedia": comment_id_wise_multimedia_list_dict[comment_id],
            "mention_users": comment_id_wise_mention_user_details_list_dict[
                comment_id
            ]
        }
        return comment_details_dict

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

    def _prepare_comment_id_wise_multimedia_list_dict(
            self,
            comment_id_with_multimedia_dtos: List[CommentIdWithMultiMediaDTO]
    ) -> Dict[str, List[Dict[str, str]]]:
        comment_id_wise_multimedia_list_dict = defaultdict(list)
        for comment_id_with_multimedia_dto in comment_id_with_multimedia_dtos:
            comment_id = str(comment_id_with_multimedia_dto.comment_id)
            comment_id_wise_multimedia_list_dict[comment_id].append(
                self._prepare_comment_id_with_multimedia_dto_dict(
                    comment_id_with_multimedia_dto
                )
            )
        return comment_id_wise_multimedia_list_dict

    @staticmethod
    def _prepare_comment_id_with_multimedia_dto_dict(
            comment_id_with_multimedia_dto: CommentIdWithMultiMediaDTO
    ) -> Dict[str, str]:
        comment_id_with_multimedia_dict = {
            "multimedia_id": str(comment_id_with_multimedia_dto.multimedia_id),
            "format_type": comment_id_with_multimedia_dto.format_type,
            "url": comment_id_with_multimedia_dto.url,
            "thumbnail_url": comment_id_with_multimedia_dto.thumbnail_url
        }
        return comment_id_with_multimedia_dict

    @staticmethod
    def _prepare_comment_id_wise_mention_user_details_list(
            comment_id_with_mention_user_id_dtos: List[
                CommentIdWithMentionUserIdDTO],
            user_id_wise_user_details_dict
    ) -> Dict[str, List[Dict[str, str]]]:
        comment_id_wise_mention_user_details_list_dict = defaultdict(list)

        for comment_id_with_mention_user_id_dto in comment_id_with_mention_user_id_dtos:
            comment_id = str(comment_id_with_mention_user_id_dto.comment_id)
            user_id = str(comment_id_with_mention_user_id_dto.mention_user_id)
            comment_id_wise_mention_user_details_list_dict[comment_id].append(
                user_id_wise_user_details_dict[user_id]
            )
        return comment_id_wise_mention_user_details_list_dict
