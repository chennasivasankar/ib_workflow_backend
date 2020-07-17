import pytest
from ib_iam.interactors.storage_interfaces.dtos import (
    BasicTeamDTO, TeamMembersDTO, MemberDTO
)
from ib_iam.adapters.dtos import BasicUserDTO


@pytest.fixture
def expected_get_list_of_teams_details():
    team_details_dict = {
        'list_of_teams': [
            {
                'description': 'team1_description',
                'members': [
                    {
                        'member_id': '2',
                        'name': 'user2',
                        'profile_pic_url': ''
                    },
                    {
                        'member_id': '3',
                        'name': 'user3',
                        'profile_pic_url': ''
                    }
                ],
                'name': 'team_name1',
                'no_of_members': 2,
                'team_id': '1'
            }
        ],
        'total_teams': 1
    }

    return team_details_dict


@pytest.fixture
def expected_list_of_teams_dtos():
    team_dtos = [
        BasicTeamDTO(
            team_id="1",
            name="team_name1",
            description="team1_description"
        )
    ]
    return team_dtos


@pytest.fixture()
def expected_team_member_ids_dtos():
    team_members_dtos = [
        TeamMembersDTO(team_id="1", member_ids=["2", "3"])
    ]
    return team_members_dtos


@pytest.fixture
def expected_list_of_user_dtos():
    user_dtos = [
        BasicUserDTO(
            user_id="2",
            name="user2",
            profile_pic_url=""
        ),
        BasicUserDTO(
            user_id="3",
            name="user3",
            profile_pic_url=""
        )
    ]
    return user_dtos


@pytest.fixture()
def expected_list_of_member_dtos():
    member_dtos = [
        MemberDTO(
            member_id="2",
            name="user2",
            profile_pic_url=""
        ),
        MemberDTO(
            member_id="3",
            name="user3",
            profile_pic_url=""
        )
    ]
    return member_dtos
