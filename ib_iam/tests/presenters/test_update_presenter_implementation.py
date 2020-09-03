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
