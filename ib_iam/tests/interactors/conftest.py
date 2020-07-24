import pytest


@pytest.fixture
def expected_list_of_teams_dtos():
    from ib_iam.tests.factories.storage_dtos import TeamDTOFactory
    TeamDTOFactory.reset_sequence(1)
    team_dtos = [TeamDTOFactory(team_id="1")]
    return team_dtos


@pytest.fixture()
def expected_team_user_ids_dtos():
    from ib_iam.tests.factories.storage_dtos import TeamUserIdsDTOFactory
    team_user_ids_dtos = [
        TeamUserIdsDTOFactory(team_id="1", user_ids=["2", "3"])
    ]
    return team_user_ids_dtos


@pytest.fixture
def expected_list_of_user_dtos():
    from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
    UserProfileDTOFactory.reset_sequence(2)
    user_profile_dtos = [
        UserProfileDTOFactory() for _ in range(2)
    ]
    return user_profile_dtos


@pytest.fixture()
def expected_list_of_member_dtos():
    from ib_iam.tests.factories.storage_dtos import BasicUserDetailsDTOFactory
    BasicUserDetailsDTOFactory.reset_sequence(2)
    member_dtos = [
        BasicUserDetailsDTOFactory() for _ in range(2)
    ]
    return member_dtos
