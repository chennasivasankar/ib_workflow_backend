from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.assign_user_roles_for_given_project_presenter_interface import \
    AssignUserRolesForGivenProjectBulkPresenterInterface

INVALID_USER_IDS_FOR_PROJECT = (
    "Please send valid user ids for project, invalid user ids are {invalid_user_ids}",
    "INVALID_USER_IDS_FOR_PROJECT"
)

INVALID_ROLE_IDS_FOR_PROJECT = (
    "Please send valid role ids for project, invalid role ids are {invalid_role_ids}",
    "INVALID_ROLE_IDS_FOR_PROJECT"
)

INVALID_PROJECT_ID = (
    "Please send valid project id",
    "INVALID_PROJECT_ID"
)


class AssignUserRolesForGivenProjectBulkPresenterImplementation(
    AssignUserRolesForGivenProjectBulkPresenterInterface, HTTPResponseMixin
):

    def prepare_success_response_for_assign_user_roles_for_given_project(self):
        return self.prepare_201_created_response(response_dict={})

    def response_for_invalid_user_ids_for_project(self, err):
        response_dict = {
            "response": INVALID_USER_IDS_FOR_PROJECT[0].format(
                invalid_user_ids=err.user_ids),
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_USER_IDS_FOR_PROJECT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def response_for_invalid_role_ids_for_project(self, err):
        response_dict = {
            "response": INVALID_ROLE_IDS_FOR_PROJECT[0].format(
                invalid_role_ids=err.role_ids
            ),
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_ROLE_IDS_FOR_PROJECT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def response_for_invalid_project_id(self):
        response_dict = {
            "response": INVALID_PROJECT_ID[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": INVALID_PROJECT_ID[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
