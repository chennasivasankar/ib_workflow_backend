from django.http import HttpResponse
from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.adapters.dtos import UserTokensDTO
from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    LoginWithUserTokePresenterInterface


class LoginWithUserTokePresenterImplementation(
    LoginWithUserTokePresenterInterface, HTTPResponseMixin
):
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
