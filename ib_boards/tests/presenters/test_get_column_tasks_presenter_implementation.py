"""
Created on: 17/07/20
Author: Pavankumar Pamuru

"""
import json

from ib_boards.presenters.presenter_implementation import \
    GetColumnTasksPresenterImplementation


class TestGetColumnTasksPresenterImplementation:

    def test_get_response_for_invalid_column_id(self):
        # Arrange
        from ib_boards.constants.exception_messages import \
            INVALID_COLUMN_ID
        expected_response = INVALID_COLUMN_ID[0]
        expected_http_status_code = 404
        expected_res_status = INVALID_COLUMN_ID[1]
        presenter = GetColumnTasksPresenterImplementation()

        # Act
        actual_response = presenter.get_response_for_the_invalid_column_id()

        # Assert
        actual_response_content = json.loads(actual_response.content)

        assert actual_response_content['response'] == expected_response
        assert actual_response_content[
                   'http_status_code'] == expected_http_status_code
        assert actual_response_content['res_status'] == expected_res_status

    def test_get_response_for_user_have_no_access_for_column(self):
        # Arrange
        from ib_boards.constants.exception_messages import \
            USER_NOT_HAVE_ACCESS_TO_COLUMN
        expected_response = USER_NOT_HAVE_ACCESS_TO_COLUMN[0]
        expected_http_status_code = 403
        expected_res_status = USER_NOT_HAVE_ACCESS_TO_COLUMN[1]
        presenter = GetColumnTasksPresenterImplementation()

        # Act
        actual_response = presenter.get_response_for_user_have_no_access_for_column()

        # Assert
        actual_response_content = json.loads(actual_response.content)

        assert actual_response_content['response'] == expected_response
        assert actual_response_content[
                   'http_status_code'] == expected_http_status_code
        assert actual_response_content['res_status'] == expected_res_status
