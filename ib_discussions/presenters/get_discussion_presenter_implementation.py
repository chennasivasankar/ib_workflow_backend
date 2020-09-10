from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.adapters.auth_service import UserProfileDTO
from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.dtos import \
    DiscussionsWithUsersAndDiscussionCountDTO, DiscussionIdWithEditableStatusDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    GetDiscussionsPresenterInterface
from ib_discussions.interactors.storage_interfaces.dtos import \
    DiscussionIdWithCommentsCountDTO

INVALID_OFFSET = (
    "Please send the valid offset value",
    "INVALID_OFFSET"
)

INVALID_LIMIT = (
    "Please send the valid limit value",
    "INVALID_LIMIT"
)

INVALID_USER_ID = (
    "Please send the valid user id",
    "INVALID_USER_ID"
)

DISCUSSION_SET_NOT_FOUND = (
    "There is no discussion for given entity id and entity type",
    "DISCUSSION_SET_NOT_FOUND"
)


class GetDiscussionPresenterImplementation(
    GetDiscussionsPresenterInterface, HTTPResponseMixin
):

    def raise_exception_for_invalid_offset(self):
        response_dict = {
            "response": INVALID_OFFSET[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_OFFSET[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_exception_for_invalid_limit(self):
        response_dict = {
            "response": INVALID_LIMIT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_LIMIT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_exception_for_invalid_user_id(self):
        response_dict = {
            "response": INVALID_USER_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_USER_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_exception_for_discussion_set_not_found(self):
        response_dict = {
            "response": DISCUSSION_SET_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": DISCUSSION_SET_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def prepare_response_for_discussions_details_dto(
            self,
            discussions_with_users_and_discussion_count_dto: DiscussionsWithUsersAndDiscussionCountDTO,
            discussion_id_with_editable_status_dtos: List[
                DiscussionIdWithEditableStatusDTO],
            discussion_id_with_comments_count_dtos: List[
                DiscussionIdWithCommentsCountDTO]

    ):
        user_profiles_dtos_with_user_id_key = self._convert_to_dict_with_key_user_id(
            discussions_with_users_and_discussion_count_dto.user_profile_dtos
        )
        discussion_id_with_editable_status_dtos_with_discussion_key = self._convert_to_dict_with_key_discussion_id(
            discussion_id_with_editable_status_dtos
        )
        discussion_id_wise_comments_count_dto_dict = {
            discussion_id_with_comments_count_dto.discussion_id: discussion_id_with_comments_count_dto
            for discussion_id_with_comments_count_dto in
            discussion_id_with_comments_count_dtos
        }
        discussions_list = [
            self._convert_discussion_dto_to_dict_with_user_profile(
                discussion_dto=discussion_dto,
                user_profile_dto=user_profiles_dtos_with_user_id_key[
                    str(discussion_dto.user_id)
                ],
                discussion_id_with_editable_status_dto=
                discussion_id_with_editable_status_dtos_with_discussion_key[
                    discussion_dto.discussion_id],
                comments_count=discussion_id_wise_comments_count_dto_dict[
                    str(discussion_dto.discussion_id)].comments_count
            )
            for discussion_dto in
            discussions_with_users_and_discussion_count_dto.discussion_dtos
        ]
        discussions_details_dict = {
            "discussions": discussions_list,
            "total_count": discussions_with_users_and_discussion_count_dto.total_count
        }
        return self.prepare_200_success_response(
            response_dict=discussions_details_dict
        )

    def _convert_discussion_dto_to_dict_with_user_profile(
            self, discussion_dto, user_profile_dto: UserProfileDTO,
            discussion_id_with_editable_status_dto: DiscussionIdWithEditableStatusDTO,
            comments_count: int
    ):
        from ib_discussions.utils.datetime_utils import get_datetime_as_string
        is_editable = discussion_id_with_editable_status_dto.is_editable
        complete_discussion_dict = {
            "discussion_id": discussion_dto.discussion_id,
            "description": discussion_dto.description,
            "title": discussion_dto.title,
            "created_at": get_datetime_as_string(
                discussion_dto.created_at
            ),
            "author": self._prepare_user_profile_dict(
                user_profile_dto=user_profile_dto
            ),
            "is_clarified": discussion_dto.is_clarified,
            "is_editable": is_editable,
            "total_comments_count": comments_count
        }
        return complete_discussion_dict

    @staticmethod
    def _convert_to_dict_with_key_user_id(user_profile_dtos):
        user_profiles_dict = {
            user_profile_dto.user_id: user_profile_dto
            for user_profile_dto in user_profile_dtos
        }
        return user_profiles_dict

    @staticmethod
    def _prepare_user_profile_dict(user_profile_dto):
        user_profile_dict = {
            "user_id": user_profile_dto.user_id,
            "name": user_profile_dto.name,
            "profile_pic_url": user_profile_dto.profile_pic_url
        }
        return user_profile_dict

    @staticmethod
    def _convert_to_dict_with_key_discussion_id(
            discussion_id_with_editable_status_dtos: \
                    List[DiscussionIdWithEditableStatusDTO]
    ):
        discussion_id_with_editable_status_dtos_dict = {
            discussion_id_with_editable_status_dto.discussion_id: \
                discussion_id_with_editable_status_dto
            for discussion_id_with_editable_status_dto in
            discussion_id_with_editable_status_dtos
        }
        return discussion_id_with_editable_status_dtos_dict
