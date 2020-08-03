import json
from ib_iam.presenters.add_company_presenter_implementation import (
    AddCompanyPresenterImplementation
)


class TestGetResponseForAddCompany:
    def test_given_company_id_it_return_http_response_with_company_id(self):
        json_presenter = AddCompanyPresenterImplementation()
        company_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
        expected_json_response = {"company_id": company_id}

        http_response = json_presenter.get_response_for_add_company(
            company_id=company_id
        )

        actual_json_response = json.loads(http_response.content)
        assert actual_json_response == expected_json_response
