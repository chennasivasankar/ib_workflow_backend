from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.add_specific_project_details_presenter_interface import \
    AddSpecificProjectDetailsPresenterInterface

INVALID_USER_IDS_FOR_PROJECT = (
    "Please send valid user ids for project, invalid user ids are {invalid_user_ids}",
    "INVALID_USER_IDS_FOR_PROJECT"
)

INVALID_ROLE_IDS_FOR_PROJECT = (
    "Please send valid role ids for project, invalid role ids are {invalid_role_ids}",
    "INVALID_ROLE_IDS_FOR_PROJECT"
)


class AddSpecificProjectDetailsPresenterImplementation(
    AddSpecificProjectDetailsPresenterInterface, HTTPResponseMixin
):

    def prepare_success_response_for_add_specific_project_details(self):
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
