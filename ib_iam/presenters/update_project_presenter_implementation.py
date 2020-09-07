from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces \
    .update_project_presenter_interface import UpdateProjectPresenterInterface


class UpdateProjectPresenterImplementation(UpdateProjectPresenterInterface,
                                           HTTPResponseMixin):

    def get_success_response_for_update_project(self):
        return self.prepare_200_success_response(response_dict={})
