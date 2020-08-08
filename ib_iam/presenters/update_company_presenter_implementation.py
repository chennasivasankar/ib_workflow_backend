from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from ib_iam.constants.enums import StatusCode
from ib_iam.constants.exception_messages import (
    INVALID_COMPANY_ID_FOR_UPDATE_COMPANY,
    USER_HAS_NO_ACCESS_FOR_UPDATE_COMPANY,
    COMPANY_NAME_ALREADY_EXISTS_FOR_UPDATE_COMPANY,
    DUPLICATE_USER_IDS_FOR_UPDATE_COMPANY,
    INVALID_USER_IDS_FOR_UPDATE_COMPANY)
from ib_iam.interactors.presenter_interfaces \
    .update_company_presenter_interface import UpdateCompanyPresenterInterface


class UpdateCompanyPresenterImplementation(UpdateCompanyPresenterInterface,
                                           HTTPResponseMixin):

    def get_success_response_for_update_company(self):
        empty_dict = {}
        return self.prepare_200_success_response(response_dict=empty_dict)

    def get_user_has_no_access_response_for_update_company(self):
        response_dict = {
            "response": USER_HAS_NO_ACCESS_FOR_UPDATE_COMPANY[0],
            "http_status_code": StatusCode.UNAUTHORIZED.value,
            "res_status": USER_HAS_NO_ACCESS_FOR_UPDATE_COMPANY[1]
        }
        return self.prepare_401_unauthorized_response(
            response_dict=response_dict)

    def get_invalid_company_response_for_update_company(self):
        response_dict = {
            "response": INVALID_COMPANY_ID_FOR_UPDATE_COMPANY[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_COMPANY_ID_FOR_UPDATE_COMPANY[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict)

    def get_company_name_already_exists_response_for_update_company(self,
                                                                    exception):
        company_name = exception.company_name
        response_dict = {
            "response": COMPANY_NAME_ALREADY_EXISTS_FOR_UPDATE_COMPANY[
                            0] % company_name,
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": COMPANY_NAME_ALREADY_EXISTS_FOR_UPDATE_COMPANY[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def get_duplicate_users_response_for_update_company(self, exception):
        response_dict = {
            "response": DUPLICATE_USER_IDS_FOR_UPDATE_COMPANY[
                0] % exception.user_ids,
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": DUPLICATE_USER_IDS_FOR_UPDATE_COMPANY[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def get_invalid_users_response_for_update_company(self, exception):
        response_dict = {
            "response": INVALID_USER_IDS_FOR_UPDATE_COMPANY[
                0] % exception.user_ids,
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_USER_IDS_FOR_UPDATE_COMPANY[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict)
