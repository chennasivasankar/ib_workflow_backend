from django_swagger_utils.utils.http_response_mixin \
    import HTTPResponseMixin
from django.http import HttpResponse
from ib_iam.adapters.auth_service import UserTokensDTO
from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    AuthPresenterInterface, CreateUserAccountPresenterInterface, \
    SendVerifyEmailLinkPresenterInterface

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


ACCOUNT_ALREADY_EXISTS = (
    "The given email has already account, try with another email",
    "ACCOUNT_ALREADY_EXISTS"
)

PASSWORD_DOES_NOT_MATCH_CRITERIA = (
    'not a valid password, try with valid password',
    "PASSWORD_DOES_NOT_MATCH_CRITERIA"
)

INVALID_DOMAIN = (
    "Currently, you can sign up to the portal only with iB Hubs and related companies email IDs",
    "INVALID_DOMAIN"
)


class CreateUserAccountPresenterImplementation(
    CreateUserAccountPresenterInterface, HTTPResponseMixin):
    def raise_account_already_exists_exception(self):
        response_dict = {
            "response": ACCOUNT_ALREADY_EXISTS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": ACCOUNT_ALREADY_EXISTS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_password_not_matched_with_criteria_exception(self):
        response_dict = {
            "response": PASSWORD_DOES_NOT_MATCH_CRITERIA[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": PASSWORD_DOES_NOT_MATCH_CRITERIA[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_invalid_email_exception(self):
        response_dict = {
            "response": INVALID_EMAIL[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_EMAIL[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_invalid_domain_exception(self):
        response_dict = {
            "response": INVALID_DOMAIN[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_DOMAIN[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def get_response_for_create_user_account(self):
        return self.prepare_200_success_response(response_dict={})

    def raise_invalid_name_length_exception(self):
        from ib_iam.constants.exception_messages import \
            INVALID_NAME_LENGTH
        from ib_iam.constants.config import MINIMUM_USER_NAME_LENGTH
        response_dict = {
            "response": INVALID_NAME_LENGTH[0].format(
                minimum_name_length=MINIMUM_USER_NAME_LENGTH
            ),
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_NAME_LENGTH[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_name_should_not_contain_special_characters_exception(self):
        from ib_iam.constants.exception_messages import \
            NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS
        response_dict = {
            "response":
                NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status":
                NAME_SHOULD_NOT_CONTAIN_SPECIAL_CHARACTERS_AND_NUMBERS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)


EMAIL_ALREADY_VERIFIED = (
    "The given email is already verified, now you can login",
    "EMAIL_ALREADY_VERIFIED"
)

ACCOUNT_DOES_NOT_EXISTS = (
    "account doesn't exist with the given email id",
    "ACCOUNT_DOES_NOT_EXISTS"
)


class SendVerifyEmailLinkPresenterImplementation(
    SendVerifyEmailLinkPresenterInterface, HTTPResponseMixin):
    def raise_account_does_not_exist_exception(self):
        response_dict = {
            "response": ACCOUNT_DOES_NOT_EXISTS[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": ACCOUNT_DOES_NOT_EXISTS[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def raise_email_already_verified_exception(self):
        response_dict = {
            "response": EMAIL_ALREADY_VERIFIED[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": EMAIL_ALREADY_VERIFIED[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
