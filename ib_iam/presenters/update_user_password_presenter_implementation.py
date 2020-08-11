from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces.update_user_password_presenter_interface import \
    UpdateUserPasswordPresenterInterface
from ib_iam.constants.enums import StatusCode


class UpdateUserPasswordPresenterImplementation(
    UpdateUserPasswordPresenterInterface, HTTPResponseMixin):

    def get_success_response_for_update_user_password(self):
        empty_dict = {}
        return self.prepare_200_success_response(response_dict=empty_dict)

    def raise_invalid_new_password_exception(self):
        from ib_iam.constants.exception_messages import INVALID_NEW_PASSWORD
        response_dict = {
            "response": INVALID_NEW_PASSWORD[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_NEW_PASSWORD[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_invalid_current_password_exception(self):
        from ib_iam.constants.exception_messages import \
            INVALID_CURRENT_PASSWORD
        response_dict = {
            "response": INVALID_CURRENT_PASSWORD[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_CURRENT_PASSWORD[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def raise_current_password_mismatch_exception(self):
        from ib_iam.constants.exception_messages import \
            CURRENT_PASSWORD_MISMATCH
        response_dict = {
            "response": CURRENT_PASSWORD_MISMATCH[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": CURRENT_PASSWORD_MISMATCH[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
