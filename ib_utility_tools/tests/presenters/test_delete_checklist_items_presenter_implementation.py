import json

from ib_utility_tools.constants.enum import StatusCode
from ib_utility_tools.presenters \
    .delete_checklist_items_presenter_implementation import \
    DeleteChecklistItemsPresenterImplementation


class TestUpdateChecklistItemPresenterImplementation:
    def test_with_invalid_checklist_item_ids_then_raise_not_found_response(
            self):
        from ib_utility_tools.constants.exception_messages import \
            INVALID_CHECKLIST_ITEM_IDS
        json_presenter = DeleteChecklistItemsPresenterImplementation()
        expected_response = INVALID_CHECKLIST_ITEM_IDS[0]
        expected_res_status = INVALID_CHECKLIST_ITEM_IDS[1]
        expected_http_status_code = StatusCode.NOT_FOUND.value

        result = json_presenter \
            .raise_invalid_checklist_item_ids_exception()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_with_duplicate_checklist_item_ids_then_raise_duplicate_checklist_items_response(
            self):
        from ib_utility_tools.constants.exception_messages import \
            DUPLICATE_CHECKLIST_ITEM_IDS
        json_presenter = DeleteChecklistItemsPresenterImplementation()
        expected_response = DUPLICATE_CHECKLIST_ITEM_IDS[0]
        expected_res_status = DUPLICATE_CHECKLIST_ITEM_IDS[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter \
            .raise_duplicate_checklist_item_ids_exception()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_with_valid_details_then_returns_success_http_response(self):
        json_presenter = DeleteChecklistItemsPresenterImplementation()
        expected_response = {}

        result = \
            json_presenter.get_success_response_for_delete_checklist_items()

        actual_response = json.loads(result.content)
        assert actual_response == expected_response
