from django.http import HttpResponse
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

    def prepare_response_for_tokens_dto(self, tokens_dto: TokensDTO):
        response_dict = {
            "access_token": tokens_dto.access_token,
            "refresh_token": tokens_dto.refresh_token,
            "expires_in_seconds": tokens_dto.expires_in_seconds
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
