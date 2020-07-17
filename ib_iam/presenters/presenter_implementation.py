from django.http import HttpResponse
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.adapters.auth_service import UserTokensDTO
from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.presenter_interface import \
    AuthPresenterInterface

INVALID_EMAIL = (
    "Please send valid email",
    "INVALID_EMAIL"
)

INCORRECT_PASSWORD = (
    "Please send valid password with you registered",
    "INCORRECT_PASSWORD"
)

PASSWORD_MIN_LENGTH = (
    "Please send the password with minimum required length is {password_min_length}",
    "PASSWORD_MIN_LENGTH"
)

PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER = (
    "Please send the password at least with one special character",
    "PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER"
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

    def raise_exception_for_invalid_email(self) -> HttpResponse:
        response_dict = {
            "response": INVALID_EMAIL[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_EMAIL[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_exception_for_incorrect_password(self) -> HttpResponse:
        response_dict = {
            "response": INCORRECT_PASSWORD[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INCORRECT_PASSWORD[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def prepare_response_for_user_tokens_dto_and_is_admin(
            self, tokens_dto: UserTokensDTO, is_admin: int
    ) -> HttpResponse:
        response_dict = {
            "access_token": tokens_dto.access_token,
            "refresh_token": tokens_dto.refresh_token,
            "expires_in_seconds": tokens_dto.expires_in_seconds,
            "is_admin": is_admin
        }
        return self.prepare_200_success_response(
            response_dict=response_dict
        )

    def raise_exception_for_user_account_does_not_exists(self) -> HttpResponse:
        response_dict = {
            "response": USER_ACCOUNT_DOES_NOT_EXIST[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": USER_ACCOUNT_DOES_NOT_EXIST[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def raise_exception_for_password_min_length_required(self) -> HttpResponse:
        from ib_iam.constants.config import REQUIRED_PASSWORD_MIN_LENGTH
        min_required_length_for_password = REQUIRED_PASSWORD_MIN_LENGTH
        response_dict = {
            "response": PASSWORD_MIN_LENGTH[0].format(
                password_min_length=min_required_length_for_password
            ),
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": PASSWORD_MIN_LENGTH[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def raise_exception_for_password_at_least_one_special_character_required(
            self
    ) -> HttpResponse:
        response_dict = {
            "response": PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER[1]
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

    def raise_exception_for_token_does_not_exists(self):
        response_dict = {
            "response": TOKEN_DOES_NOT_EXIST[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": TOKEN_DOES_NOT_EXIST[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def raise_exception_for_token_has_expired(self):
        response_dict = {
            "response": TOKEN_HAS_EXPIRED[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": TOKEN_HAS_EXPIRED[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_update_user_password_success_response(self):
        return self.prepare_200_success_response(response_dict={})

    def get_success_response_for_reset_password_link_to_user_email(self) \
            -> HttpResponse:
        return self.prepare_200_success_response(response_dict={})
