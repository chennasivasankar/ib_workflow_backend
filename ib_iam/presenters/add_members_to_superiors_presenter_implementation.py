from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    AddMembersToSuperiorsPresenterInterface

INVALID_TEAM_ID = (
    "Please send valid team id, to add members to superiors",
    "INVALID_TEAM_ID"
)

INVALID_LEVEL_HIERARCHY = (
    "Please send valid level hierarchy of a team",
    "INVALID_LEVEL_HIERARCHY"
)

TEAM_MEMBER_IDS_NOT_FOUND = (
    "Please send valid member ids, invalid member ids are {team_member_ids}",
    "TEAM_MEMBER_IDS_NOT_FOUND"
)

USERS_NOT_BELONG_TO_TEAM_MEMBER_LEVEL = (
    "Please send valid user ids, invalid user ids are {user_ids} for level hierarchy is {level_hierarchy}",
    "USERS_NOT_BELONG_TO_TEAM_MEMBER_LEVEL"
)

USER_DOES_NOT_HAVE_ACCESS = (
    "User does not have provision to access",
    "USER_DOES_NOT_HAVE_ACCESS"
)


class AddMembersToSuperiorsPresenterImplementation(
    AddMembersToSuperiorsPresenterInterface, HTTPResponseMixin
):

    def prepare_success_response_for_add_members_superiors(self):
        return self.prepare_201_created_response(response_dict={})

    def response_for_invalid_team_id_exception(self):
        response_dict = {
            "response": INVALID_TEAM_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_TEAM_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_invalid_level_hierarchy_of_team(self):
        response_dict = {
            "response": INVALID_LEVEL_HIERARCHY[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_LEVEL_HIERARCHY[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_team_member_ids_not_found(self, err):
        response_dict = {
            "response": TEAM_MEMBER_IDS_NOT_FOUND[0].format(
                team_member_ids=err.team_member_ids
            ),
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": TEAM_MEMBER_IDS_NOT_FOUND[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def response_for_users_not_belong_to_team_member_level(self, err):
        response_dict = {
            "response": USERS_NOT_BELONG_TO_TEAM_MEMBER_LEVEL[0].format(
                user_ids=err.user_ids,
                level_hierarchy=err.level_hierarchy
            ),
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": USERS_NOT_BELONG_TO_TEAM_MEMBER_LEVEL[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def response_for_user_is_not_admin_exception(self):
        response_dict = {
            "response": USER_DOES_NOT_HAVE_ACCESS[0],
            "http_status_code": StatusCode.FORBIDDEN.value,
            "res_status": USER_DOES_NOT_HAVE_ACCESS[1]
        }
        return self.prepare_403_forbidden_response(
            response_dict=response_dict
        )
