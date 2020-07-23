from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces.delete_user_presenter_interface import \
    DeleteUserPresenterInterface


class DeleteUserPresenterImplementation(DeleteUserPresenterInterface,
                                        HTTPResponseMixin):
    def get_delete_user_response(self):
        return self.prepare_200_success_response(response_dict={})

    def raise_user_is_not_admin_exception(self):
        pass

    def raise_user_is_not_found_exception(self):
        pass

    def raise_user_does_not_have_delete_permission_exception(self):
        pass
