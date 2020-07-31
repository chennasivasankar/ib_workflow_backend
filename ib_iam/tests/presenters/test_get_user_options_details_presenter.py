import json

import pytest

from ib_iam.presenters.get_user_options_presenter_implementation \
    import GetUserOptionsPresenterImplementation


class TestGetUserOptionsDetailsResponse:

    @pytest.fixture()
    def company_dtos(self):
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_for_company_dto_factory
        reset_sequence_for_company_dto_factory()
        from ib_iam.tests.factories.storage_dtos import CompanyIdAndNameDTOFactory
        company_dtos = CompanyIdAndNameDTOFactory.create_batch(3)
        return company_dtos

    @pytest.fixture()
    def team_dtos(self):
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_for_team_dto_factory
        reset_sequence_for_team_dto_factory()
        from ib_iam.tests.factories.storage_dtos import TeamIdAndNameDTOFactory
        team_dtos = TeamIdAndNameDTOFactory.create_batch(3)
        return team_dtos

    @pytest.fixture()
    def role_dtos(self):
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_for_role_dto_factory
        reset_sequence_for_role_dto_factory()
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        role_dtos = RoleDTOFactory.create_batch(3)
        return role_dtos

    @pytest.fixture
    def set_up(self, company_dtos, team_dtos, role_dtos):
        from ib_iam.interactors.presenter_interfaces.dtos \
            import UserOptionsDetailsDTO
        configuration_details_dto = UserOptionsDetailsDTO(
            companies=company_dtos,
            teams=team_dtos,
            roles=role_dtos
        )
        return configuration_details_dto

    def test_response_for_get_configuration_details(
            self, set_up, snapshot):
        # Arrange
        presenter = GetUserOptionsPresenterImplementation()

        # Act
        resonse = presenter.get_user_options_details_response(
            set_up)

        # Assert
        response_dict = json.loads(resonse.content)
        snapshot.assert_match(response_dict, 'user_options_details')
