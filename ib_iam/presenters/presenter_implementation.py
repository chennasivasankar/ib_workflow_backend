from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.adapters.auth_service import TokensDTO
from ib_iam.interactors.presenter_interfaces.presenter_interface import \
    AuthPresenterInterface

INVALID_EMAIL = (
    "Please send valid email",
    "INVALID_EMAIL"
)

INVALID_PASSWORD = (
    "Please send valid password",
    "INVALID_PASSWORD"
)

USER_ACCOUNT_DOES_NOT_EXIST = (
    "user account does not exist. please send valid email",
    "USER_ACCOUNT_DOES_NOT_EXIST"
)

NOT_STRONG_PASSWORD = (
    "Please send the strong password",
    "NOT_STRONG_PASSWORD"
)

TOKEN_DOES_NOT_EXIST = (
    "Please send valid token",
    "TOKEN_DOES_NOT_EXIST"
)

TOKEN_HAS_EXPIRED = (
    "Please send valid token which is not expired",
    "TOKEN_HAS_EXPIRED"
)


class AuthPresenterImplementation(AuthPresenterInterface, HTTPResponseMixin):

    def raise_invalid_email(self):
        response_dict = {
            "response": INVALID_EMAIL[0],
            "http_status_code": 404,
            "res_status": INVALID_EMAIL[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def raise_invalid_password(self):
        response_dict = {
            "response": INVALID_PASSWORD[0],
            "http_status_code": 400,
            "res_status": INVALID_PASSWORD[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def prepare_response_for_tokens_dto(self, tokens_dto: TokensDTO,
                                        is_admin: bool):
        response_dict = {
            "access_token": tokens_dto.access_token,
            "refresh_token": tokens_dto.refresh_token,
            "expires_in_seconds": tokens_dto.expires_in_seconds,
            "is_admin": is_admin
        }
        return self.prepare_200_success_response(response_dict)

    def raise_user_account_does_not_exist(self):
        response_dict = {
            "response": USER_ACCOUNT_DOES_NOT_EXIST[0],
            "http_status_code": 404,
            "res_status": USER_ACCOUNT_DOES_NOT_EXIST[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def get_success_response_for_reset_password_link_to_user_email(self):
        return self.prepare_200_success_response(response_dict={})

    def raise_exception_for_not_a_strong_password(self):
        response_dict = {
            "response": NOT_STRONG_PASSWORD[0],
            "http_status_code": 400,
            "res_status": NOT_STRONG_PASSWORD[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_exception_for_token_does_not_exists(self):
        response_dict = {
            "response": TOKEN_DOES_NOT_EXIST[0],
            "http_status_code": 404,
            "res_status": TOKEN_DOES_NOT_EXIST[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def raise_exception_for_token_has_expired(self):
        response_dict = {
            "response": TOKEN_HAS_EXPIRED[0],
            "http_status_code": 400,
            "res_status": TOKEN_HAS_EXPIRED[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_update_user_password_success_response(self):
        return self.prepare_200_success_response(response_dict={})
