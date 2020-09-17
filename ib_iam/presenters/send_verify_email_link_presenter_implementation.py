from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    SendVerifyEmailLinkPresenterInterface

EMAIL_ALREADY_VERIFIED = (
    "The given email is already verified, now you can login",
    "EMAIL_ALREADY_VERIFIED"
)

ACCOUNT_DOES_NOT_EXISTS = (
    "account doesn't exist with the given email id",
    "ACCOUNT_DOES_NOT_EXISTS"
)


# TODO: Write in a different file
class SendVerifyEmailLinkPresenterImplementation(
    SendVerifyEmailLinkPresenterInterface, HTTPResponseMixin
):
    def get_response_send_verify_email_link(self):
        return self.prepare_200_success_response(response_dict={})

    def response_for_account_does_not_exist_exception(self):
        response_dict = {
            "response": ACCOUNT_DOES_NOT_EXISTS[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": ACCOUNT_DOES_NOT_EXISTS[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def response_for_email_already_verified_exception(self):
        response_dict = {
            "response": EMAIL_ALREADY_VERIFIED[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": EMAIL_ALREADY_VERIFIED[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
