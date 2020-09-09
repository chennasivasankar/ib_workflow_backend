import json

import pytest

from ib_utility_tools.constants.enum import StatusCode


class TestUpdateChecklistItemPresenterImplementation:
    @pytest.fixture
    def presenter(self):
        from ib_utility_tools.presenters.update_checklist_item_presenter_implementation import (
            UpdateChecklistItemPresenterImplementation
        )
        presenter = UpdateChecklistItemPresenterImplementation()
        return presenter

    def test_whether_it_gives_empty_checklist_item_id_not_found_response(
            self, presenter
    ):
        # Arrange
        from ib_utility_tools.constants.exception_messages import (
            CHECKLIST_ITEM_ID_NOT_FOUND_FOR_UPDATE_CHECKLIST_ITEM as checklist_item_id_not_found
        )
        expected_response = checklist_item_id_not_found[0]
        expected_res_status = checklist_item_id_not_found[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = presenter.get_checklist_item_id_not_found_response()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_with_valid_details_then_returns_checklist_id_response(
            self, presenter
    ):
        # Arrange
        expected_response = {}

        # Act
        result = presenter.get_response_for_update_checklist_item()

        # Assert
        actual_response = json.loads(result.content)
        assert actual_response == expected_response
