import json
import pytest


class TestUpdateCompanyPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_iam.presenters.update_company_presenter_implementation import (
            UpdateCompanyPresenterImplementation
        )
        return UpdateCompanyPresenterImplementation()

    def test_whether_it_returns_company_name_already_exists_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import (
            COMPANY_NAME_ALREADY_EXISTS_FOR_UPDATE_COMPANY
        )
        from ib_iam.exceptions.custom_exceptions import \
            CompanyNameAlreadyExists
        company_name = "company_name1"
        expected_response = COMPANY_NAME_ALREADY_EXISTS_FOR_UPDATE_COMPANY[
            0].format(company_name=company_name)
        expected_res_status = COMPANY_NAME_ALREADY_EXISTS_FOR_UPDATE_COMPANY[1]
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

    def test_when_it_is_called_it_returns_empty_dict_http_response(
            self, presenter
    ):
        # Arrange
        expected_response = {}

        result = presenter.get_response_for_update_company()

        actual_response = json.loads(result.content)
        assert actual_response == expected_response

    def test_whether_it_returns_user_has_no_access_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import (
            USER_HAS_NO_ACCESS_FOR_UPDATE_COMPANY
        )
        expected_response = USER_HAS_NO_ACCESS_FOR_UPDATE_COMPANY[0]
        expected_res_status = USER_HAS_NO_ACCESS_FOR_UPDATE_COMPANY[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.UNAUTHORIZED.value

        result = \
            presenter.response_for_user_has_no_access_exception()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_when_it_is_called_it_returns_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import \
            DUPLICATE_USER_IDS_FOR_UPDATE_COMPANY
        expected_response = DUPLICATE_USER_IDS_FOR_UPDATE_COMPANY[0]
        expected_res_status = DUPLICATE_USER_IDS_FOR_UPDATE_COMPANY[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = presenter \
            .response_for_duplicate_user_ids_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_error_object(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import \
            INVALID_COMPANY_ID_FOR_UPDATE_COMPANY
        expected_response = INVALID_COMPANY_ID_FOR_UPDATE_COMPANY[0]
        expected_res_status = INVALID_COMPANY_ID_FOR_UPDATE_COMPANY[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        result = presenter.response_for_invalid_company_id_exception()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_invalid_users_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import \
            INVALID_USER_IDS_FOR_UPDATE_COMPANY
        expected_response = INVALID_USER_IDS_FOR_UPDATE_COMPANY[0]
        expected_res_status = INVALID_USER_IDS_FOR_UPDATE_COMPANY[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        # Act
        result = presenter.response_for_invalid_user_ids_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
