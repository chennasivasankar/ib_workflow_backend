def get_team_member_levels_mock(mocker):
    mock = mocker.patch(
        "ib_iam.interactors.get_team_member_levels_interactor.GetTeamMemberLevelsInteractor.get_team_member_levels"
    )
    return mock


def get_team_members_of_level_hierarchy_mock(mocker):
    mock = mocker.patch(
        "ib_iam.interactors.get_team_members_of_level_hierarchy_interactor.GetTeamMembersOfLevelHierarchyInteractor.get_team_members_of_level_hierarchy"
    )
    return mock
