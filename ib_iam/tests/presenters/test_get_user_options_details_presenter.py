import json

import pytest

from ib_iam.presenters.presenter_implementation import PresenterImplementation
from ib_iam.tests.common_fixtures.storages import reset_sequence


class TestGetUserOptionsDetailsResponse:

    @pytest.fixture()
    def company_dtos(self):
        reset_sequence()
        from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
        company_dtos = CompanyDTOFactory.create_batch(3)
        return company_dtos

    @pytest.fixture()
    def team_dtos(self):
        reset_sequence()
        from ib_iam.tests.factories.storage_dtos import TeamIdAndNameDTOFactory
        team_dtos = TeamIdAndNameDTOFactory.create_batch(3)
        return team_dtos

    @pytest.fixture()
    def role_dtos(self):
        reset_sequence()
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        role_dtos = RoleDTOFactory.create_batch(3)
        return role_dtos

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
        print(set_up)
        # Arrange

        presenter = PresenterImplementation()

        # Act
        resonse = presenter.get_user_options_details_response(
            set_up)

        # Assert
        response_dict = json.loads(resonse.content)
        snapshot.assert_match(response_dict, 'user_options_details')
