from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    AddTeamMemberLevelsPresenterInterface


class AddTeamMemberLevelsPresenterImplementation(
    AddTeamMemberLevelsPresenterInterface, HTTPResponseMixin
):

    def prepare_success_response_for_add_team_member_levels_to_team(self):
        return self.prepare_201_created_response(response_dict={})
