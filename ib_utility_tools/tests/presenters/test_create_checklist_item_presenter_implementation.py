import json

from ib_utility_tools.constants.enum import StatusCode
from ib_utility_tools.presenters\
    .create_checklist_item_presenter_implementation import \
    CreateChecklistItemPresenterImplementation


class TestCreateChecklistItemPresenterImplementation:
    def test_whether_it_gives_empty_checklist_item_text_response(self):
        from ib_utility_tools.constants.exception_messages import \
            EMPTY_CHECKLIST_ITEM_TEXT_FOR_CREATE_CHECKLIST_ITEM
        json_presenter = CreateChecklistItemPresenterImplementation()
        expected_response = \
            EMPTY_CHECKLIST_ITEM_TEXT_FOR_CREATE_CHECKLIST_ITEM[0]
        expected_res_status = \
            EMPTY_CHECKLIST_ITEM_TEXT_FOR_CREATE_CHECKLIST_ITEM[1]
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter \
            .get_response_for_empty_checklist_item_text_exception()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_whether_it_returns_checklist_id_http_response(self):
        json_presenter = CreateChecklistItemPresenterImplementation()
        checklist_item_id = "checklist_item_id"
        expected_response = {"checklist_item_id": checklist_item_id}

        result = json_presenter.get_success_response_for_create_checklist_item(
            checklist_item_id=checklist_item_id)

        actual_response = json.loads(result.content)
        assert actual_response == expected_response
