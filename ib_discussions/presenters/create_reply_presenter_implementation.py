from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_discussions.adapters.auth_service import UserProfileDTO
from ib_discussions.constants.enum import StatusCode
from ib_discussions.interactors.presenter_interfaces.dtos import \
    CommentIdWithEditableStatusDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    CreateReplyPresenterInterface
from ib_discussions.interactors.storage_interfaces.dtos import CommentDTO

COMMENT_ID_NOT_FOUND = (
    "Please send valid comment id to create reply for comment",
    "COMMENT_ID_NOT_FOUND"
)


class CreateReplyPresenterImplementation(
    CreateReplyPresenterInterface, HTTPResponseMixin
):

    def response_for_comment_id_not_found(self):
        response_dict = {
            "response": COMMENT_ID_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": COMMENT_ID_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def prepare_response_for_reply(
            self, comment_dto: CommentDTO,
            comment_with_editable_status_dto: CommentIdWithEditableStatusDTO,
            user_profile_dto: UserProfileDTO
    ):
        from ib_discussions.utils.datetime_utils import get_datetime_as_string
        created_at = get_datetime_as_string(comment_dto.created_at)

        response = {
            "comment_id": str(comment_dto.comment_id),
            "comment_content": comment_dto.comment_content,
            "author": {
                "user_id": user_profile_dto.user_id,
                "name": user_profile_dto.name,
                "profile_pic_url": user_profile_dto.profile_pic_url
            },
            "created_at": created_at,
            "is_editable": comment_with_editable_status_dto.is_editable
        }
        return self.prepare_200_success_response(response_dict=response)
