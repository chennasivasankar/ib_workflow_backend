import pytest
from ib_iam.tests.factories import (
    TeamDTOFactory, TeamMemberIdsDTOFactory, MemberDTOFactory
)
from ib_iam.tests.factories.presenter_dtos import (
    TeamWithMembersDetailsDTOFactory
)
from ib_iam.interactors.presenter_interfaces.get_companies_presenter_interface import \
    CompanyDetailsWithEmployeesCountDTO

team_ids = [
    "f2c02d98-f311-4ab2-8673-3daa00757002",
    "aa66c40f-6d93-484a-b418-984716514c7b",
    "c982032b-53a7-4dfa-a627-4701a5230765"
]
member_ids = [
    '2bdb417e-4632-419a-8ddd-085ea272c6eb',
    '548a803c-7b48-47ba-a700-24f2ea0d1280',
    '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
    '7ee2c7b4-34c8-4d65-a83a-f87da75db24e'
]


@pytest.fixture()
def get_list_of_team_dtos():
    TeamDTOFactory.reset_sequence(1)
    TeamMemberIdsDTOFactory.reset_sequence(1)
    MemberDTOFactory.reset_sequence(1)

    teams_dtos = [
        TeamDTOFactory(team_id=team_id) for team_id in team_ids
    ]
    team_member_ids_dtos = [
        TeamMemberIdsDTOFactory(team_id=team_id) for team_id in team_ids
    ]
    members_dtos = [
        MemberDTOFactory(member_id=member_id) for member_id in member_ids
    ]

    teams_dto = TeamWithMembersDetailsDTOFactory(
        total_teams_count=3,
        team_dtos=teams_dtos,
        team_member_ids_dtos=team_member_ids_dtos,
        member_dtos=members_dtos
    )
    return teams_dto


@pytest.fixture
def get_company_details_dtos():
    from ib_iam.tests.factories import CompanyDTOFactory, CompanyNameLogoAndDescriptionDTOFactory
    from ib_iam.tests.factories import CompanyWithEmployeesCountDTOFactory
    company_ids = [
        "f2c02d98-f311-4ab2-8673-3daa00757003",
        "aa66c40f-6d93-484a-b418-984716514c7c",
        "c982032b-53a7-4dfa-a627-4701a5230767"
    ]
    CompanyDTOFactory.reset_sequence(1, force=True)
    company_dtos = [
        CompanyDTOFactory(company_id=company_id) for company_id in company_ids
    ]
    company_with_employees_count_dtos = [
        CompanyWithEmployeesCountDTOFactory(
            company_id=company_id,
            no_of_employees=i
        ) for company_id, i in zip(company_ids, range(3, 7, 2))
    ]
    company_details_dtos = CompanyDetailsWithEmployeesCountDTO(
        company_dtos=company_dtos,
        company_with_employees_count_dtos=company_with_employees_count_dtos
    )
    return company_details_dtos
