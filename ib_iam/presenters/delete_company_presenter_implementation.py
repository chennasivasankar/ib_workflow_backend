from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces \
    .delete_company_presenter_interface import DeleteCompanyPresenterInterface

from ib_iam.constants.enums import StatusCode
from ib_iam.constants.exception_messages import (
    USER_HAS_NO_ACCESS_FOR_DELETE_COMPANY,
    INVALID_COMPANY_FOR_DELETE_COMPANY

)


class DeleteCompanyPresenterImplementation(
    DeleteCompanyPresenterInterface, HTTPResponseMixin
):

    def get_success_response_for_delete_company(self):
        empty_dict = {}
        return self.prepare_200_success_response(response_dict=empty_dict)

    def get_user_has_no_access_response_for_delete_company(self):
        response_dict = {
            "response": USER_HAS_NO_ACCESS_FOR_DELETE_COMPANY[0],
            "http_status_code": StatusCode.UNAUTHORIZED.value,
            "res_status": USER_HAS_NO_ACCESS_FOR_DELETE_COMPANY[1]
        }
        return self.prepare_401_unauthorized_response(
            response_dict=response_dict
        )

    def get_invalid_company_response_for_delete_company(self):
        response_dict = {
            "response": INVALID_COMPANY_FOR_DELETE_COMPANY[0],
            "http_status_code": StatusCode.NOT_FOUND.value,
            "res_status": INVALID_COMPANY_FOR_DELETE_COMPANY[1]
        }
        return self.prepare_404_not_found_response(
            response_dict=response_dict
        )
