from ib_iam.presenters.team_presenter_implementation import TeamPresenterImplementation


class TestMakeEmptyHttpSuccessResponse:
    def test_when_it_is_called_it_returns_empty_dict_http_response(self, snapshot):
        json_presenter = TeamPresenterImplementation()
        import json
        expected_response = {}

        result = json_presenter.make_empty_http_success_response()

        actual_response = json.loads(result.content)
        assert actual_response == expected_response
