from django.http import HttpResponse

from ib_iam.adapters.auth_service import TokensDTO
from ib_iam.interactors.presenter_interfaces.presenter_interface import PresenterInterface

INVALID_EMAIL = (
    "Please send valid email",
    "INVALID_EMAIL"
)

INVALID_PASSWORD = (
    "Please send valid password",
    "INVALID_PASSWORD"
)


class LoginPresenterImplementation(PresenterInterface):

    def raise_invalid_email(self):
        import json
        data = json.dumps(
            {
                "response": INVALID_EMAIL[0],
                "http_status_code": 400,
                "res_status": INVALID_EMAIL[1]
            }
        )
        response_object = HttpResponse(data, status=400)
        return response_object

    def raise_invalid_password(self):
        import json
        data = json.dumps(
            {
                "response": INVALID_PASSWORD[0],
                "http_status_code": 400,
                "res_status": INVALID_PASSWORD[1]
            }
        )
        response_object = HttpResponse(data, status=400)
        return response_object

    def prepare_response_for_tokens_dto(self, tokens_dto: TokensDTO):
        import json
        data = json.dumps(
            {
                "access_token": tokens_dto.access_token,
                "refresh_token": tokens_dto.refresh_token,
                "expires_in_seconds": tokens_dto.expires_in_seconds
            }
        )
        response_object = HttpResponse(data, status=200)
        return response_object
