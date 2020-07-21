from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.constants.exception_messages import (
    INVALID_TEAM_FOR_UPDATE_TEAM,
    USER_HAS_NO_ACCESS_FOR_UPDATE_TEAM,
    TEAM_NAME_ALREADY_EXISTS_FOR_UPDATE_TEAM,
    DUPLICATE_USERS_FOR_UPDATE_TEAM,
    INVALID_USERS_FOR_UPDATE_TEAM

)
from ib_iam.interactors.presenter_interfaces \
    .update_team_presenter_interface import UpdateTeamPresenterInterface


class UpdateTeamPresenterImplementation(
    UpdateTeamPresenterInterface, HTTPResponseMixin
):

    def get_success_response_for_update_team(self):
        empty_dict = {}
        return self.prepare_200_success_response(response_dict=empty_dict)

    def get_user_has_no_access_response_for_update_team(self):
        response_dict = {
            "response": USER_HAS_NO_ACCESS_FOR_UPDATE_TEAM[0],
            "http_status_code": StatusCode.UNAUTHORIZED.value,
            "res_status": USER_HAS_NO_ACCESS_FOR_UPDATE_TEAM[1]
        }
        return self.prepare_401_unauthorized_response(
            response_dict=response_dict
        )

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
        team_name = exception.team_name
        response_dict = {
            "response":
                TEAM_NAME_ALREADY_EXISTS_FOR_UPDATE_TEAM[0] % team_name,
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": TEAM_NAME_ALREADY_EXISTS_FOR_UPDATE_TEAM[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_duplicate_users_response_for_update_team(self):
        response_dict = {
            "response": DUPLICATE_USERS_FOR_UPDATE_TEAM[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": DUPLICATE_USERS_FOR_UPDATE_TEAM[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_invalid_users_response_for_update_team(self):
        response_dict = {
            "response": INVALID_USERS_FOR_UPDATE_TEAM[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_USERS_FOR_UPDATE_TEAM[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )
