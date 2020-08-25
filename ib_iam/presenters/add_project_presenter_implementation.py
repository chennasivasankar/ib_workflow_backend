from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces \
    .add_project_presenter_interface import AddProjectPresenterInterface


class AddProjectPresenterImplementation(AddProjectPresenterInterface,
                                        HTTPResponseMixin):

    def get_success_response_for_add_project(self):
        return self.prepare_201_created_response(response_dict={})
