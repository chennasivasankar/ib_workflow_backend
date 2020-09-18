import json

from ib_iam.constants.exception_messages import (
    COMPANY_NAME_ALREADY_EXISTS_FOR_ADD_COMPANY
)
from ib_iam.exceptions.custom_exceptions import CompanyNameAlreadyExists
from ib_iam.presenters.add_company_presenter_implementation import (
    AddCompanyPresenterImplementation
)


class TestRaiseExceptionIfCompanyNameAlreadyExistsForAddCompany:
    def test_whether_it_returns_company_name_already_exists_http_response(
            self
    ):
        # Arrange
        json_presenter = AddCompanyPresenterImplementation()
        company_name = "company_name1"
        expected_response = COMPANY_NAME_ALREADY_EXISTS_FOR_ADD_COMPANY[
            0].format(company_name=company_name)
        expected_res_status = COMPANY_NAME_ALREADY_EXISTS_FOR_ADD_COMPANY[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = json_presenter \
            .get_company_name_already_exists_response_for_add_company(
            err=CompanyNameAlreadyExists(company_name=company_name)
        )

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
