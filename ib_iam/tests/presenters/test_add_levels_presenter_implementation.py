import pytest

from ib_iam.constants.enums import StatusCode


class TestAddLevelsPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.add_levels_presenter_implementation import \
            AddTeamMemberLevelsPresenterImplementation
        presenter = AddTeamMemberLevelsPresenterImplementation()
        return presenter

    def test_prepare_success_response_for_add_levels_to_team(self, presenter):
        # Act
        response_object = presenter. \
            prepare_success_response_for_add_team_member_levels_to_team()

        # Assert
        assert response_object.status_code == StatusCode.SUCCESS_CREATE.value

