from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.adapters.auth_service import UserTokensDTO
from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.get_refresh_auth_tokens_presenter_interface import \
    GetRefreshTokensPresenterInterface

ACCESS_TOKEN_NOT_FOUND = (
    "Please send valid access token, to get refresh tokens",
    "ACCESS_TOKEN_NOT_FOUND"
)

REFRESH_TOKEN_HAS_EXPIRED = (
    "Please send valid refresh token, send refresh token expired",
    "REFRESH_TOKEN_HAS_EXPIRED"
)

REFRESH_TOKEN_NOT_FOUND = (
    "Please send valid refresh token, your refresh token not found",
    "REFRESH_TOKEN_NOT_FOUND"
)

USER_ACCOUNT_NOT_FOUND = (
    "Please send valid access token, your account is not found",
    "USER_ACCOUNT_NOT_FOUND"
)


class GetRefreshTokensPresenterImplementation(
    GetRefreshTokensPresenterInterface, HTTPResponseMixin
):

    def response_for_access_token_not_found(self):
        response_dict = {
            "response": ACCESS_TOKEN_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": ACCESS_TOKEN_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def response_for_refresh_token_expired(self):
        response_dict = {
            "response": REFRESH_TOKEN_HAS_EXPIRED[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": REFRESH_TOKEN_HAS_EXPIRED[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def response_for_refresh_token_not_found(self):
        response_dict = {
            "response": REFRESH_TOKEN_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": REFRESH_TOKEN_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def response_for_user_account_not_found(self):
        response_dict = {
            "response": USER_ACCOUNT_NOT_FOUND[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": USER_ACCOUNT_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def response_for_user_tokens_dto(self, user_tokens_dto: UserTokensDTO):
        response_dict = {
            "access_token": user_tokens_dto.access_token,
            "refresh_token": user_tokens_dto.refresh_token,
            "expires_in_seconds": user_tokens_dto.expires_in_seconds,
        }
        return self.prepare_200_success_response(response_dict=response_dict)
