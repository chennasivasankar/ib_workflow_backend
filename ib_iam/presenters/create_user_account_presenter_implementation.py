from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.constants.exception_messages import INVALID_EMAIL
from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    CreateUserAccountPresenterInterface

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
    CreateUserAccountPresenterInterface, HTTPResponseMixin
):
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

    def response_for_invalid_email_exception(self):
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

    def response_for_invalid_name_length_exception(self):
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

    def response_for_name_contains_special_character_exception(self):
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
