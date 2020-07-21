from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces \
    .delete_team_presenter_interface import DeleteTeamPresenterInterface

from ib_iam.constants.enums import StatusCode
from ib_iam.constants.exception_messages import (
    USER_HAS_NO_ACCESS_FOR_DELETE_TEAM,
    INVALID_TEAM_FOR_DELETE_TEAM

)


class DeleteTeamPresenterImplementation(
    DeleteTeamPresenterInterface, HTTPResponseMixin
):

    def get_success_response_for_delete_team(self):
        empty_dict = {}
        return self.prepare_200_success_response(response_dict=empty_dict)

    def get_user_has_no_access_response_for_delete_team(self):
        response_dict = {
            "response": USER_HAS_NO_ACCESS_FOR_DELETE_TEAM[0],
            "http_status_code": StatusCode.UNAUTHORIZED.value,
            "res_status": USER_HAS_NO_ACCESS_FOR_DELETE_TEAM[1]
        }
        return self.prepare_401_unauthorized_response(
            response_dict=response_dict
        )

    def get_invalid_team_response_for_delete_team(self):
        response_dict = {
            "response": INVALID_TEAM_FOR_DELETE_TEAM[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_TEAM_FOR_DELETE_TEAM[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )
