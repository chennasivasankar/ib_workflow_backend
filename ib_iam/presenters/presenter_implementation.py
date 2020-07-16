from django.http import HttpResponse
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.adapters.auth_service import TokensDTO
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
    "Please send the password with minimum required length is %s",
    "PASSWORD_MIN_LENGTH"
)

USER_ACCOUNT_DOES_NOT_EXIST = (
    "Please send valid email which is already exist",
    "USER_ACCOUNT_DOES_NOT_EXIST"
)

PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER = (
    "Please send the password at least with one special character",
    "PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER"
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

    def prepare_response_for_tokens_dto(self, tokens_dto: TokensDTO) \
            -> HttpResponse:
        response_dict = {
            "access_token": tokens_dto.access_token,
            "refresh_token": tokens_dto.refresh_token,
            "expires_in_seconds": tokens_dto.expires_in_seconds
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
            "response": PASSWORD_MIN_LENGTH[
                            0] % min_required_length_for_password,
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

    def get_success_response_for_reset_password_link_to_user_email(self) \
            -> HttpResponse:
        return self.prepare_200_success_response(response_dict={})
