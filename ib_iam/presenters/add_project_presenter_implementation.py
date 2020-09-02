from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces \
    .add_project_presenter_interface import AddProjectPresenterInterface


class AddProjectPresenterImplementation(AddProjectPresenterInterface,
                                        HTTPResponseMixin):

    def get_success_response_for_add_project(self):
        return self.prepare_201_created_response(response_dict={})

    def get_user_has_no_access_response(self):
        from ib_iam.constants.exception_messages import \
            USER_HAS_NO_ACCESS_TO_ADD_PROJECT
        response_dict = {
            "response": USER_HAS_NO_ACCESS_TO_ADD_PROJECT[0],
            "http_status_code": StatusCode.UNAUTHORIZED.value,
            "res_status": USER_HAS_NO_ACCESS_TO_ADD_PROJECT[1]
        }
        return self.prepare_401_unauthorized_response(
            response_dict=response_dict)

    def get_project_name_already_exists_response(self):
        from ib_iam.constants.exception_messages import \
            PROJECT_NAME_ALREADY_EXISTS
        response_dict = {"response": PROJECT_NAME_ALREADY_EXISTS[0],
                         "http_status_code": StatusCode.BAD_REQUEST.value,
                         "res_status": PROJECT_NAME_ALREADY_EXISTS[1]}
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def get_project_display_id_already_exists_response(self):
        from ib_iam.constants.exception_messages import \
            PROJECT_DISPLAY_ID_ALREADY_EXISTS
        response_dict = {"response": PROJECT_DISPLAY_ID_ALREADY_EXISTS[0],
                         "http_status_code": StatusCode.BAD_REQUEST.value,
                         "res_status": PROJECT_DISPLAY_ID_ALREADY_EXISTS[1]}
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def get_invalid_team_ids_response(self):
        from ib_iam.constants.exception_messages import INVALID_TEAM_IDS
        response_dict = {"response": INVALID_TEAM_IDS[0],
                         "http_status_code": StatusCode.NOT_FOUND.value,
                         "res_status": INVALID_TEAM_IDS[1]}
        return self.prepare_404_not_found_response(
            response_dict=response_dict)

    def get_duplicate_team_ids_response(self):
        from ib_iam.constants.exception_messages import DUPLICATE_TEAM_IDS
        response_dict = {"response": DUPLICATE_TEAM_IDS[0],
                         "http_status_code": StatusCode.BAD_REQUEST.value,
                         "res_status": DUPLICATE_TEAM_IDS[1]}
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)
