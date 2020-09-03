from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    AddMembersToLevelPresenterInterface

INVALID_TEAM_ID = (
    "Please send valid team id to add members to team member levels",
    "INVALID_TEAM_ID"
)

TEAM_MEMBER_LEVEL_IDS_NOT_FOUND = (
    "Please send valid team member level ids, invalid team member level ids are {team_member_level_ids}",
    "TEAM_MEMBER_LEVEL_IDS_NOT_FOUND"
)

TEAM_MEMBER_IDS_NOT_FOUND = (
    "Please send valid team member ids, invalid team member ids are {team_member_ids}",
    "TEAM_MEMBER_IDS_NOT_FOUND"
)


class AddMembersToLevelPresenterImplementation(
    AddMembersToLevelPresenterInterface, HTTPResponseMixin
):

    def prepare_success_response_for_add_members_to_levels(self):
        return self.prepare_201_created_response(response_dict={})

    def response_for_invalid_team_id(self):
        response_dict = {
            "response": INVALID_TEAM_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_TEAM_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def response_for_team_member_level_ids_not_found(self, err):
        response_dict = {
            "response": TEAM_MEMBER_LEVEL_IDS_NOT_FOUND[0].format(
                team_member_level_ids=err.team_member_level_ids
            ),
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": TEAM_MEMBER_LEVEL_IDS_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict)

    def response_for_team_member_ids_not_found(self, err):
        response_dict = {
            "response": TEAM_MEMBER_IDS_NOT_FOUND[0].format(
                team_member_ids=err.team_member_ids
            ),
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": TEAM_MEMBER_IDS_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict)
