from ib_iam.presenters.delete_company_presenter_implementation import (
    DeleteCompanyPresenterImplementation
)


class TestGetSuccessResponseForDeleteCompany:
    def test_when_it_is_called_it_returns_empty_dict_http_response(self):
        json_presenter = DeleteCompanyPresenterImplementation()
        import json
        expected_response = {}

        result = json_presenter.get_success_response_for_delete_company()

        actual_response = json.loads(result.content)
        assert actual_response == expected_response
