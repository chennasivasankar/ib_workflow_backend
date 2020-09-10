from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    AddTeamMemberLevelsPresenterInterface

INVALID_TEAM_ID = (
    "Please send valid team id to add team member levels",
    "INVALID_TEAM_ID"
)

DUPLICATE_LEVEL_HIERARCHIES = (
    "Please send unique level hierarchies, duplicate level hierarchies are {level_hierarchies}",
    "DUPLICATE_LEVEL_HIERARCHIES"
)

NEGATIVE_LEVEL_HIERARCHIES = (
    "Please send positive level hierarchies, negative level hierarchies are {level_hierarchies}",
    "NEGATIVE_LEVEL_HIERARCHIES"
)

DUPLICATE_TEAM_MEMBER_LEVEL_NAMES = (
    "Please send unique level names, duplicate team member level names are {team_member_level_names}",
    "DUPLICATE_TEAM_MEMBER_LEVEL_NAMES"
)

USER_DOES_NOT_HAVE_ACCESS = (
    "User does not have provision to access",
    "USER_DOES_NOT_HAVE_ACCESS"
)


class AddTeamMemberLevelsPresenterImplementation(
    AddTeamMemberLevelsPresenterInterface, HTTPResponseMixin
):

    def prepare_success_response_for_add_team_member_levels_to_team(self):
        return self.prepare_201_created_response(response_dict={})

    def response_for_invalid_team_id(self):
        response_dict = {
            "response": INVALID_TEAM_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_TEAM_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_duplicate_level_hierarchies(self, err):
        response_dict = {
            "response": DUPLICATE_LEVEL_HIERARCHIES[0].format(
                level_hierarchies=err.level_hierarchies
            ),
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": DUPLICATE_LEVEL_HIERARCHIES[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_negative_level_hierarchies(self, err):
        response_dict = {
            "response": NEGATIVE_LEVEL_HIERARCHIES[0].format(
                level_hierarchies=err.level_hierarchies
            ),
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": NEGATIVE_LEVEL_HIERARCHIES[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_duplicate_team_member_level_names(self, err):
        response_dict = {
            "response": DUPLICATE_TEAM_MEMBER_LEVEL_NAMES[0].format(
                team_member_level_names=err.team_member_level_names
            ),
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": DUPLICATE_TEAM_MEMBER_LEVEL_NAMES[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_user_is_not_admin(self):
        response_dict = {
            "response": USER_DOES_NOT_HAVE_ACCESS[0],
            "http_status_code": StatusCode.FORBIDDEN.value,
            "res_status": USER_DOES_NOT_HAVE_ACCESS[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )
