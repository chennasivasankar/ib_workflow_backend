from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    GetUserProfilePresenterInterface

INVALID_USER_ID = (
    "Please send valid user id, given user id is empty",
    "INVALID_USER_ID"
)

USER_ACCOUNT_DOES_NOT_EXIST = (
    "Please send valid user id",
    "USER_ACCOUNT_DOES_NOT_EXIST"
)


class GetUserProfilePresenterImplementation(GetUserProfilePresenterInterface,
                                            HTTPResponseMixin):

    def raise_exception_for_invalid_user_id(self):
        response_dict = {
            "response": INVALID_USER_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_USER_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_exception_for_user_account_does_not_exist(self):
        response_dict = {
            "response": USER_ACCOUNT_DOES_NOT_EXIST[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": USER_ACCOUNT_DOES_NOT_EXIST[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def prepare_response_for_user_profile_dto(self,
                                              user_profile_dto: UserProfileDTO):
        response_dict = {
            "user_id": user_profile_dto.user_id,
            "name": user_profile_dto.name,
            "is_admin": user_profile_dto.is_admin,
            "email": user_profile_dto.email,
            "profile_pic_url": user_profile_dto.profile_pic_url
        }
        return self.prepare_200_success_response(response_dict=response_dict)
