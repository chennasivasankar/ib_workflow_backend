from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    VerifyEmailPresenterInterface


class VerifyEmailPresenterImplementation(
    VerifyEmailPresenterInterface, HTTPResponseMixin
):
    def response_for_email_does_not_exist_exception(self):
        from ib_iam.constants.exception_messages import ACCOUNT_DOES_NOT_EXISTS
        response_dict = {
            "response": ACCOUNT_DOES_NOT_EXISTS[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": ACCOUNT_DOES_NOT_EXISTS[1]
        }
        return self.prepare_404_not_found_response(response_dict=response_dict)

    def get_response_for_verified_email(self):
        return self.prepare_200_success_response(response_dict={})

    def response_for_email_already_verified_exception(self):
        from ib_iam.constants.exception_messages import EMAIL_ALREADY_VERIFIED
        response_dict = {
            "response": EMAIL_ALREADY_VERIFIED[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": EMAIL_ALREADY_VERIFIED[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
