from collections import defaultdict
from typing import List, Dict

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.adapters.auth_service import UserProfileDTO
from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.dtos import \
    CommentIdWithEditableStatusDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    GetRepliesForCommentPresenterInterface
from ib_discussions.interactors.storage_interfaces.dtos import CommentDTO, \
    CommentIdWithMultiMediaDTO, CommentIdWithMentionUserIdDTO

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
                CommentIdWithEditableStatusDTO], comment_dtos: List[CommentDTO],
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
        comment_id_wise_editable_status_dto_dict = \
            self._prepare_comment_id_wise_editable_status_dict(
                comment_with_editable_status_dtos)
        comments_details_list = [
            self._prepare_comment_details_dict(
                comment_dto, comment_id_wise_editable_status_dto_dict,
                comment_id_wise_mention_user_details_list_dict,
                comment_id_wise_multimedia_list_dict,
                user_id_wise_user_details_dict)
            for comment_dto in comment_dtos
        ]

        response_dict = {"replies": comments_details_list}
        return self.prepare_200_success_response(response_dict=response_dict)

    @staticmethod
    def _prepare_comment_details_dict(
            comment_dto, comment_id_wise_editable_status_dto_dict,
            comment_id_wise_mention_user_details_list_dict,
            comment_id_wise_multimedia_list_dict,
            user_id_wise_user_details_dict):
        comment_id = str(comment_dto.comment_id)
        from ib_discussions.utils.datetime_utils import get_datetime_as_string
        comment_details_dict = {
            "comment_id": comment_id,
            "comment_content": comment_dto.comment_content,
            "author": user_id_wise_user_details_dict[
                comment_dto.user_id
            ],
            "created_at": get_datetime_as_string(
                comment_dto.created_at
            ),
            "is_editable": comment_id_wise_editable_status_dto_dict[
                str(comment_id)
            ],
            "multimedia": comment_id_wise_multimedia_list_dict[comment_id],
            "mention_users": comment_id_wise_mention_user_details_list_dict[
                comment_id
            ]
        }
        return comment_details_dict

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
            "url": comment_id_with_multimedia_dto.url
        }
        return comment_id_with_multimedia_dict

    @staticmethod
    def _prepare_comment_id_wise_mention_user_details_list(
            comment_id_with_mention_user_id_dtos: List[
                CommentIdWithMentionUserIdDTO],
            user_id_wise_user_details_dict: Dict[str, Dict[str, str]]
    ):
        comment_id_wise_mention_user_details_list_dict = defaultdict(list)

        for comment_id_with_mention_user_id_dto in comment_id_with_mention_user_id_dtos:
            comment_id = str(comment_id_with_mention_user_id_dto.comment_id)
            user_id = str(comment_id_with_mention_user_id_dto.mention_user_id)
            comment_id_wise_mention_user_details_list_dict[comment_id].append(
                user_id_wise_user_details_dict[user_id]
            )
        return comment_id_wise_mention_user_details_list_dict

    @staticmethod
    def _prepare_comment_id_wise_editable_status_dict(
            comment_with_editable_status_dtos: List[
                CommentIdWithEditableStatusDTO]
    ) -> Dict[str, bool]:
        comment_id_wise_editable_status_dto_dict = {
            str(
                comment_with_editable_status_dto.comment_id): comment_with_editable_status_dto.is_editable
            for comment_with_editable_status_dto in
            comment_with_editable_status_dtos
        }
        return comment_id_wise_editable_status_dto_dict

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
