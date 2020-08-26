from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces.add_specific_project_details_presenter_interface import \
    AddSpecificProjectDetailsPresenterInterface


class AddSpecificProjectDetailsPresenterImplementation(
    AddSpecificProjectDetailsPresenterInterface, HTTPResponseMixin
):

    def prepare_success_response_for_add_specific_project_details(self):
        return self.prepare_201_created_response(response_dict={})
