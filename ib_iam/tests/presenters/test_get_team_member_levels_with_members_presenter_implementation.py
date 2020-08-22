import pytest


class TestGetTeamMemberLevelsWithMembersPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.get_team_member_levels_with_members_presenter_implementation import \
            GetTeamMemberLevelsWithMembersPresenterImplementation
        presenter = GetTeamMemberLevelsWithMembersPresenterImplementation()
        return presenter

    def test_prepare_success_response_for_team_member_levels_with_members(
            self, presenter
    ):
        pass
