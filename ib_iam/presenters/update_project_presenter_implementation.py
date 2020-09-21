from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces.project_presenter_interface import (
    UpdateProjectPresenterInterface
)


class UpdateProjectPresenterImplementation(
    UpdateProjectPresenterInterface, HTTPResponseMixin
):

    def get_success_response_for_update_project(self):
        return self.prepare_200_success_response(response_dict={})

    def response_for_user_has_no_access_exception(self):
        from ib_iam.constants.exception_messages import \
            USER_HAS_NO_ACCESS_TO_ADD_PROJECT
        response_dict = {
            "response": USER_HAS_NO_ACCESS_TO_ADD_PROJECT[0],
            "http_status_code": StatusCode.UNAUTHORIZED.value,
            "res_status": USER_HAS_NO_ACCESS_TO_ADD_PROJECT[1]
        }
        return self.prepare_401_unauthorized_response(
            response_dict=response_dict
        )

    def response_for_invalid_project_id_exception(self):
        from ib_iam.constants.exception_messages import INVALID_PROJECT_ID
        response_dict = {
            "response": INVALID_PROJECT_ID[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_PROJECT_ID[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def response_for_project_name_already_exists_exception(self):
        from ib_iam.constants.exception_messages import (
            PROJECT_NAME_ALREADY_EXISTS
        )
        response_dict = {
            "response": PROJECT_NAME_ALREADY_EXISTS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": PROJECT_NAME_ALREADY_EXISTS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_duplicate_team_ids_exception(self):
        from ib_iam.constants.exception_messages import DUPLICATE_TEAM_IDS
        response_dict = {
            "response": DUPLICATE_TEAM_IDS[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": DUPLICATE_TEAM_IDS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_invalid_team_ids_exception(self):
        from ib_iam.constants.exception_messages import INVALID_TEAM_IDS
        response_dict = {
            "response": INVALID_TEAM_IDS[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_TEAM_IDS[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def response_for_duplicate_role_ids_exception(self):
        from ib_iam.constants.exception_messages import (
            DUPLICATE_ROLE_IDS_FOR_UPDATE_PROJECT
        )
        response_dict = {
            "response": DUPLICATE_ROLE_IDS_FOR_UPDATE_PROJECT[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": DUPLICATE_ROLE_IDS_FOR_UPDATE_PROJECT[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_invalid_role_ids_exception(self):
        from ib_iam.constants.exception_messages import INVALID_ROLE_IDS
        response_dict = {
            "response": INVALID_ROLE_IDS[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_ROLE_IDS[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )

    def response_for_duplicate_role_names_exception(self):
        from ib_iam.constants.exception_messages import DUPLICATE_ROLE_NAMES
        response_dict = {
            "response": DUPLICATE_ROLE_NAMES[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": DUPLICATE_ROLE_NAMES[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def response_for_role_names_already_exists_exception(self, exception):
        from ib_iam.constants.exception_messages import \
            ROLE_NAMES_ALREADY_EXISTS
        response_dict = {
            "response": ROLE_NAMES_ALREADY_EXISTS[0].format(
                role_names=exception.role_names),
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": ROLE_NAMES_ALREADY_EXISTS[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )
