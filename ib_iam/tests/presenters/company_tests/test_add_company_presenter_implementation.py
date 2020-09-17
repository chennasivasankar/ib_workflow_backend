import pytest
import json


class TestAddCompanyPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_iam.presenters.add_company_presenter_implementation import (
            AddCompanyPresenterImplementation
        )
        return AddCompanyPresenterImplementation()

    def test_when_it_is_called_it_returns_http_response(self, presenter):
        # Arrange
        from ib_iam.constants.exception_messages import (
            USER_HAS_NO_ACCESS_FOR_ADD_COMPANY
        )
        expected_response = USER_HAS_NO_ACCESS_FOR_ADD_COMPANY[0]
        expected_res_status = USER_HAS_NO_ACCESS_FOR_ADD_COMPANY[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.UNAUTHORIZED.value

        # Act
        result = presenter.response_for_user_has_no_access_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_given_company_id_it_return_http_response_with_company_id(
            self, presenter
    ):
        # Arrange
        company_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
        expected_json_response = {"company_id": company_id}

        # Act
        http_response = presenter.get_response_for_add_company(
            company_id=company_id
        )

        # Assert
        actual_json_response = json.loads(http_response.content)
        assert actual_json_response == expected_json_response

    def test_whether_it_returns_invalid_users_http_response(self, presenter):
        # Arrange
        from ib_iam.constants.exception_messages import \
            INVALID_USER_IDS_FOR_ADD_COMPANY
        expected_response = INVALID_USER_IDS_FOR_ADD_COMPANY[0]
        expected_res_status = INVALID_USER_IDS_FOR_ADD_COMPANY[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        # Act
        result = presenter.response_for_invalid_user_ids_exception()

        # Arrange
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_duplicate_users_exception_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import (
            DUPLICATE_USER_IDS_FOR_ADD_COMPANY
        )
        expected_response = DUPLICATE_USER_IDS_FOR_ADD_COMPANY[0]
        expected_res_status = DUPLICATE_USER_IDS_FOR_ADD_COMPANY[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = presenter.response_for_duplicate_user_ids_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_company_name_already_exists_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import (
            COMPANY_NAME_ALREADY_EXISTS_FOR_ADD_COMPANY
        )
        from ib_iam.exceptions.custom_exceptions import \
            CompanyNameAlreadyExists
        company_name = "company_name1"
        expected_response = COMPANY_NAME_ALREADY_EXISTS_FOR_ADD_COMPANY[
            0].format(company_name=company_name)
        expected_res_status = COMPANY_NAME_ALREADY_EXISTS_FOR_ADD_COMPANY[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = presenter.response_for_company_name_already_exists_exception(
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
