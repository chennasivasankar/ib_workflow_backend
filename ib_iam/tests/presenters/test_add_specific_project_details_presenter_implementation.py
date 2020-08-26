import pytest

from ib_iam.constants.enums import StatusCode


class TestAddSpecificProjectDetailsPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.add_specific_project_details_presenter_implementation import \
            AddSpecificProjectDetailsPresenterImplementation
        presenter = AddSpecificProjectDetailsPresenterImplementation()
        return presenter

    def test_prepare_success_response_for_add_specific_project_details(
            self, presenter):
        # Act
        response_object = presenter. \
            prepare_success_response_for_add_specific_project_details()

        # Assert
        assert response_object.status_code == StatusCode.SUCCESS_CREATE.value
