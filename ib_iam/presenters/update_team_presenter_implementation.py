from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.constants.exception_messages import INVALID_TEAM_FOR_UPDATE_TEAM
from ib_iam.interactors.presenter_interfaces \
    .update_team_presenter_interface import UpdateTeamPresenterInterface


class UpdateTeamPresenterImplementation(
    UpdateTeamPresenterInterface, HTTPResponseMixin
):

    def make_empty_http_success_response(self):
        empty_dict = {}
        return self.prepare_200_success_response(response_dict=empty_dict)

    def get_invalid_team_response_for_update_team(self):
        response_dict = {
            "response": INVALID_TEAM_FOR_UPDATE_TEAM[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_TEAM_FOR_UPDATE_TEAM[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def get_team_name_already_exists_response_for_update_team(self, exception):
        pass
