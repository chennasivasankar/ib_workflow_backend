from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.dtos import \
    DiscussionsDetailsDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    GetDiscussionsPresenterInterface

ENTITY_ID_NOT_FOUND = (
    "Please send valid entity id",
    "ENTITY_ID_NOT_FOUND"
)

INVALID_ENTITY_TYPE_FOR_ENTITY_ID = (
    "Please valid entity type for entity id",
    "INVALID_ENTITY_TYPE_FOR_ENTITY_ID"
)

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
    def raise_exception_for_entity_id_not_found(self):
        response_dict = {
            "response": ENTITY_ID_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": ENTITY_ID_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def raise_exception_for_invalid_entity_type_for_entity_id(self):
        response_dict = {
            "response": INVALID_ENTITY_TYPE_FOR_ENTITY_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_ENTITY_TYPE_FOR_ENTITY_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

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
            self, discussions_details_dto: DiscussionsDetailsDTO
    ):
        user_profiles_dict = self._convert_to_dict_with_key_ids(
            user_profile_dtos=discussions_details_dto.user_profile_dtos
        )
        from ib_discussions.utils.datetime_utils import get_datetime_as_string
        discussions_list = [
            {
                "discussion_id": complete_discussion_dto.discussion_id,
                "description": complete_discussion_dto.description,
                "title": complete_discussion_dto.title,
                "created_at": get_datetime_as_string(
                    complete_discussion_dto.created_at
                ),
                "author": self._prepare_user_profile_dict(
                    user_profile_dto \
                        =user_profiles_dict[str(complete_discussion_dto.user_id)]
                ),
                "is_clarified": complete_discussion_dto.is_clarified
            }
            for complete_discussion_dto in
            discussions_details_dto.complete_discussion_dtos
        ]
        discussions_details_dict = {
            "discussions": discussions_list,
            "total_count": discussions_details_dto.total_count
        }
        print(discussions_list)
        return self.prepare_200_success_response(
            response_dict=discussions_details_dict
        )

    @staticmethod
    def _convert_to_dict_with_key_ids(user_profile_dtos):
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
