import pytest

from ib_iam.presenters.presenter_implementation import PresenterImplementation
from ib_iam.tests.common_fixtures.presenters import company_dtos, team_dtos, \
    role_dtos


class TestGetUserOptionsDetailsResponse:
    @pytest.fixture
    def set_up(self, company_dtos, team_dtos, role_dtos):
        from ib_iam.interactors.presenter_interfaces.dtos \
            import UserOptionsDetails
        configuration_details_dto = UserOptionsDetails(
            companies=company_dtos,
            teams=team_dtos,
            roles=role_dtos
        )
        return configuration_details_dto

    def test_response_for_get_configuration_details(
            self, set_up, snapshot):
        # Arrange

        presenter = PresenterImplementation()

        # Act
        resonse = presenter.get_user_options_details_response(
            set_up)

        # Assert
        print(resonse)
        snapshot.assert_match(resonse, 'user_options_details')
