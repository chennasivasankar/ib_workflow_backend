import json

from ib_iam.presenters.update_project_presenter_implementation import \
    UpdateProjectPresenterImplementation


class TestUpdateProjectPresenterImplementation:
    def test_whether_it_returns_empty_http_success_response(self):
        json_presenter = UpdateProjectPresenterImplementation()
        expected_json_response = {}

        response = json_presenter.get_success_response_for_update_project()

        actual_json_response = json.loads(response.content)
        assert actual_json_response == expected_json_response

    def test_get_user_has_no_access_response_returns_user_has_no_access_response(
            self):
        json_presenter = UpdateProjectPresenterImplementation()
        from ib_iam.constants.exception_messages import \
            USER_HAS_NO_ACCESS_TO_ADD_PROJECT
        expected_response = USER_HAS_NO_ACCESS_TO_ADD_PROJECT[0]
        expected_res_status = USER_HAS_NO_ACCESS_TO_ADD_PROJECT[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.UNAUTHORIZED.value

        result = json_presenter.get_user_has_no_access_response()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_get_invalid_project_response_returns_invalid_project_id_response(
            self):
        json_presenter = UpdateProjectPresenterImplementation()
        from ib_iam.constants.exception_messages import INVALID_PROJECT_ID
        expected_response = INVALID_PROJECT_ID[0]
        expected_res_status = INVALID_PROJECT_ID[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        result = json_presenter.get_invalid_project_response()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_get_project_name_already_exists_response_returns_name_already_exists_response(
            self):
        json_presenter = UpdateProjectPresenterImplementation()
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

    def test_get_duplicate_team_ids_response_returns_duplicate_team_ids_response(
            self):
        json_presenter = UpdateProjectPresenterImplementation()
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
        json_presenter = UpdateProjectPresenterImplementation()
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

    def test_get_duplicate_role_ids_response_returns_duplicate_role_ids_response(
            self):
        json_presenter = UpdateProjectPresenterImplementation()
        from ib_iam.constants.exception_messages import \
            DUPLICATE_ROLE_IDS_FOR_UPDATE_PROJECT
        expected_response = DUPLICATE_ROLE_IDS_FOR_UPDATE_PROJECT[0]
        expected_res_status = DUPLICATE_ROLE_IDS_FOR_UPDATE_PROJECT[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter.get_duplicate_role_ids_response()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_get_invalid_role_ids_response_returns_invalid_role_ids_response(
            self):
        json_presenter = UpdateProjectPresenterImplementation()
        from ib_iam.constants.exception_messages import INVALID_ROLE_IDS
        expected_response = INVALID_ROLE_IDS[0]
        expected_res_status = INVALID_ROLE_IDS[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        result = json_presenter.get_invalid_role_ids_response()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
