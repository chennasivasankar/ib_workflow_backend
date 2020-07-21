from ib_iam.presenters.presenter_implementation import PresenterImplementation
from ib_iam.tests.common_fixtures.storages import configuration_details_dto


class TestGetConfigurationResponse:
    def test_response_for_get_configuration_details(self, configuration_details_dto, snapshot):
        # Arrange
        presenter = PresenterImplementation()

        # Act
        resonse = presenter.response_for_get_configuration_details(configuration_details_dto)

        # Assert
        snapshot.assert_match(resonse, 'get_configuration_details')