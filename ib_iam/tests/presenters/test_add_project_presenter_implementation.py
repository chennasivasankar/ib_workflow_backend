import json

from ib_iam.presenters.add_project_presenter_implementation import \
    AddProjectPresenterImplementation


class TestAddProjectPresenterImplementation:
    def test_given_project_id_it_returns_http_response_with_project_id(self):
        json_presenter = AddProjectPresenterImplementation()
        expected_json_response = {}

        http_response = json_presenter.get_success_response_for_add_project()

        actual_json_response = json.loads(http_response.content)
        assert actual_json_response == expected_json_response

    def test_get_project_name_already_exists_response_returns_name_already_exists_response(
            self):
        json_presenter = AddProjectPresenterImplementation()
        from ib_iam.constants.exception_messages import \
            PROJECT_NAME_ALREADY_EXISTS
        expected_response = PROJECT_NAME_ALREADY_EXISTS[0]
        expected_res_status = PROJECT_NAME_ALREADY_EXISTS[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter.get_project_name_already_exists_response()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_get_project_display_id_already_exists_response_returns_display_id_already_exists_response(
            self):
        json_presenter = AddProjectPresenterImplementation()
        from ib_iam.constants.exception_messages import \
            PROJECT_DISPLAY_ID_ALREADY_EXISTS
        expected_response = PROJECT_DISPLAY_ID_ALREADY_EXISTS[0]
        expected_res_status = PROJECT_DISPLAY_ID_ALREADY_EXISTS[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter \
            .get_project_display_id_already_exists_response()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_get_duplicate_team_ids_response_returns_duplicate_team_ids_response(
            self):
        json_presenter = AddProjectPresenterImplementation()
        from ib_iam.constants.exception_messages import DUPLICATE_TEAM_IDS
        expected_response = DUPLICATE_TEAM_IDS[0]
        expected_res_status = DUPLICATE_TEAM_IDS[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter.get_duplicate_team_ids_response()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_get_invalid_team_ids_response_returns_invalid_team_ids_response(
            self):
        json_presenter = AddProjectPresenterImplementation()
        from ib_iam.constants.exception_messages import INVALID_TEAM_IDS
        expected_response = INVALID_TEAM_IDS[0]
        expected_res_status = INVALID_TEAM_IDS[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        result = json_presenter.get_invalid_team_ids_response()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
