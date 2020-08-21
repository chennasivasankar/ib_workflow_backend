from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    AddMembersToLevelPresenterInterface


class AddMembersToLevelPresenterImplementation(
    AddMembersToLevelPresenterInterface, HTTPResponseMixin
):

    def prepare_success_response_for_add_members_to_levels(self):
        return self.prepare_201_created_response(response_dict={})

