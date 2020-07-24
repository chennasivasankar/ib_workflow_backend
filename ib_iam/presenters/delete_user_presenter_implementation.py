from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.delete_user_presenter_interface import \
    DeleteUserPresenterInterface


class DeleteUserPresenterImplementation(DeleteUserPresenterInterface,
                                        HTTPResponseMixin):
    def get_delete_user_response(self):
        return self.prepare_200_success_response(response_dict={})

    def raise_user_is_not_admin_exception(self):
        from ib_iam.constants.exception_messages import \
            USER_DOES_NOT_HAVE_PERMISSION
        response_dict = {
            "response": USER_DOES_NOT_HAVE_PERMISSION[0],
            "http_status_code": StatusCode.FORBIDDEN.value,
            "res_status": USER_DOES_NOT_HAVE_PERMISSION[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict)

    def raise_user_is_not_found_exception(self):
        pass

    def raise_user_does_not_have_delete_permission_exception(self):
        pass
