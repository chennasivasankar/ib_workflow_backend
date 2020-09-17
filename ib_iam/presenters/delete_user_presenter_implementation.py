from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.user_presenter_interface import \
    DeleteUserPresenterInterface


class DeleteUserPresenterImplementation(DeleteUserPresenterInterface,
                                        HTTPResponseMixin):
    def get_delete_user_response(self):
        return self.prepare_200_success_response(response_dict={})

    def response_for_user_is_not_admin_exception(self):
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
        from ib_iam.constants.exception_messages \
            import USER_DOES_NOT_EXIST
        response_dict = {
            "response": USER_DOES_NOT_EXIST[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": USER_DOES_NOT_EXIST[1]
        }
        response = self.prepare_404_not_found_response(
            response_dict=response_dict)
        return response

    def raise_user_does_not_have_delete_permission_exception(self):
        from ib_iam.constants.exception_messages import \
            USER_DOES_NOT_HAVE_DELETE_PERMISSION
        response_dict = {
            "response": USER_DOES_NOT_HAVE_DELETE_PERMISSION[0],
            "http_status_code": StatusCode.FORBIDDEN.value,
            "res_status": USER_DOES_NOT_HAVE_DELETE_PERMISSION[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict)
