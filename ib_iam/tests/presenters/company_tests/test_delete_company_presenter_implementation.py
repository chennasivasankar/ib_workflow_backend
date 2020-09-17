import json
import pytest


class TestDeleteCompanyPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_iam.presenters.delete_company_presenter_implementation import (
            DeleteCompanyPresenterImplementation
        )
        return DeleteCompanyPresenterImplementation()

    def test_when_it_is_called_it_returns_empty_dict_http_response(
            self, presenter
    ):
        # Arrange
        expected_response = {}

        # Act
        result = presenter.get_success_response_for_delete_company()

        # Assert
        actual_response = json.loads(result.content)
        assert actual_response == expected_response

    def test_whether_it_returns_invalid_company_exception_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import \
            INVALID_COMPANY_ID_FOR_DELETE_COMPANY
        expected_response = INVALID_COMPANY_ID_FOR_DELETE_COMPANY[0]
        expected_res_status = INVALID_COMPANY_ID_FOR_DELETE_COMPANY[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        # Act
        result = presenter.response_for_invalid_company_id_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_user_has_no_access_for_delete_company_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import (
            USER_HAS_NO_ACCESS_FOR_DELETE_COMPANY
        )
        expected_response = USER_HAS_NO_ACCESS_FOR_DELETE_COMPANY[0]
        expected_res_status = USER_HAS_NO_ACCESS_FOR_DELETE_COMPANY[1]
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
