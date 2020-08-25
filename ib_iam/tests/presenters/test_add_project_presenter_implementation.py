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
