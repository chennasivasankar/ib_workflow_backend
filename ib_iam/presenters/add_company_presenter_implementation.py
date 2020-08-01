from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin
from ib_iam.constants.enums import StatusCode
from ib_iam.interactors.presenter_interfaces \
    .add_company_presenter_interface import AddCompanyPresenterInterface
from ib_iam.constants.exception_messages import (
    USER_HAS_NO_ACCESS_FOR_ADD_COMPANY,
    COMPANY_NAME_ALREADY_EXISTS_FOR_ADD_COMPANY,
    INVALID_USERS_FOR_ADD_COMPANY,
    DUPLICATE_USERS_FOR_ADD_COMPANY)


class AddCompanyPresenterImplementation(AddCompanyPresenterInterface,
                                        HTTPResponseMixin):

    def get_response_for_add_company(self, company_id: str):
        return self.prepare_201_created_response(
            response_dict={"company_id": company_id})

    def get_user_has_no_access_response_for_add_company(self):
        response_dict = {
            "response": USER_HAS_NO_ACCESS_FOR_ADD_COMPANY[0],
            "http_status_code": StatusCode.UNAUTHORIZED.value,
            "res_status": USER_HAS_NO_ACCESS_FOR_ADD_COMPANY[1]
        }
        return self.prepare_401_unauthorized_response(
            response_dict=response_dict)

    def get_company_name_already_exists_response_for_add_company(
            self, exception):
        response_dict = {
            "response": COMPANY_NAME_ALREADY_EXISTS_FOR_ADD_COMPANY[
                            0] % exception.company_name,
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": COMPANY_NAME_ALREADY_EXISTS_FOR_ADD_COMPANY[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def get_duplicate_users_response_for_add_company(self):
        response_dict = {
            "response": DUPLICATE_USERS_FOR_ADD_COMPANY[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": DUPLICATE_USERS_FOR_ADD_COMPANY[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict)

    def get_invalid_users_response_for_add_company(self):
        response_dict = {
            "response": INVALID_USERS_FOR_ADD_COMPANY[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_USERS_FOR_ADD_COMPANY[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict)
