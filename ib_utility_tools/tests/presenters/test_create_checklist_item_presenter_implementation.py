import json
import pytest
from ib_utility_tools.constants.enum import StatusCode


class TestCreateChecklistItemPresenterImplementation:
    @pytest.fixture
    def presenter(self):
        from ib_utility_tools.presenters.create_checklist_item_presenter_implementation import (
            CreateChecklistItemPresenterImplementation)
        presenter = CreateChecklistItemPresenterImplementation()
        return presenter

    def test_whether_it_gives_empty_checklist_item_text_response(
            self, presenter
    ):
        # Arrange
        from ib_utility_tools.constants.exception_messages import (
            EMPTY_CHECKLIST_ITEM_TEXT_FOR_CREATE_CHECKLIST_ITEM
        )

        expected_response = \
            EMPTY_CHECKLIST_ITEM_TEXT_FOR_CREATE_CHECKLIST_ITEM[0]
        expected_res_status = \
            EMPTY_CHECKLIST_ITEM_TEXT_FOR_CREATE_CHECKLIST_ITEM[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        # Act
        result = presenter.response_for_empty_checklist_item_text_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_checklist_id_response(self, presenter):
        # Arrange
        checklist_item_id = "checklist_item_id"
        expected_response = {"checklist_item_id": checklist_item_id}

        # Act
        result = presenter.get_response_for_create_checklist_item(
            checklist_item_id=checklist_item_id
        )

        # Assert
        actual_response = json.loads(result.content)
        assert actual_response == expected_response
