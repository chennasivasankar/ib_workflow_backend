from typing import List

from django.db import transaction

from ib_iam.models import UserDetails
from ib_iam.populate.populate_complete_user_details_bulk import get_team_ids, \
    populate_complete_user_details_bulk

TEAMS = [
    {
        "name": "Tech Team",
        "description": "Technology Teams are formed to deliver a unique set of solutions and services within your organization.",
        "created_by_id": "f2c02d98-f311-4ab2-8673-3daa00757002"
    },
    {
        "name": "Discovery Team",
        "description": "The discovery team is formed by those who can help to lead the discovery work and who has knowledge in if it is feasible (developer), usable",
        "created_by_id": "f2c02d98-f311-4ab2-8673-3daa00757002"
    },
    {
        "name": "iB Studio Team",
        "description": "We have an in-house Studio team of strength 20+ which includes passionate designers and artists and we are looking forward to invite more.",
        "created_by_id": "f2c02d98-f311-4ab2-8673-3daa00757002"
    },
    {
        "name": "Assert Management Team",
        "description": "A team assessment is an exercise that allows you to evaluate a team's strengths and weaknesses.",
        "created_by_id": "f2c02d98-f311-4ab2-8673-3daa00757002"
    },
]

COMPANIES = [
    {
        "name": "iBHubs",
        "description": "iB Hubs fosters and enables the adoption of 4.0 technologies among individuals, companies and countries.",
        "logo_url": "https://dynamic.placementindia.com/recruiter_comp_logo/621380.png"
    },
    {
        "name": "CyberEye",
        "description": "CyberEye Research Labs & Security Solutions Pvt. Ltd. envisions to create a 'Smart, Secure and Sustainable Planet'",
        "logo_url": "https://s3-ap-southeast-1.amazonaws.com/ibhubs-media-files/iBHubs+_+Startups/StartupCards/logo-cybereye.png"
    },
    {
        "name": "Proyuga",
        "description": "Proyuga Advanced Technologies Ltd. develops transformative products in VR, AR & MR.",
        "logo_url": "https://res.cloudinary.com/due4dmz2b/image/fetch/dpr_auto,w_auto,f_auto,q_auto/https://proyuga-media-assets.s3.ap-south-1.amazonaws.com/ib-cricket-logo-reg.png"
    }
]

INITIAL_USERS = [
    {
        "name": "Pavan",
        "email": "ibadmin@ibhubs.co",
        "is_admin": True,
        "password": "Admin123@",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "company": "iBHubs",
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    },
    {
        "name": "Lavanya",
        "email": "cybereyeadmin@ibhubs.co",
        "is_admin": True,
        "password": "Admin123@",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "company": "CyberEye",
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    }, {
        "email": "vasanth@ibhubs.co",
        "name": "Vasanth",
        "is_admin": False,
        "company": "iBHubs",
        "teams": [
            "Tech Team"
        ],
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    },
    {
        "email": "thrivikram@ibhubs.co",
        "name": "Thrivikram",
        "is_admin": False,
        "company": "Proyuga",
        "teams": [
            "Tech Team"
        ],
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    },
    {
        "email": "kavya@ibhubs.co",
        "name": "Kavya",
        "is_admin": False,
        "company": "CyberEye",
        "teams": [
            "Tech Team", "Discovery Team"
        ],
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    },
    {
        "email": "ramganesh@ibhubs.co",
        "name": "Ramganesh",
        "is_admin": False,
        "company": "CyberEye",
        "teams": [
            "Tech Team"
        ],
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    },
    {
        "email": "vedavidh@ibhubs.co",
        "name": "Vedavidh",
        "is_admin": False,
        "company": "iBHubs",
        "teams": [
            "iB Studio Team", "Tech Team"
        ],
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    },
    {
        "email": "revanth@ibhubs.co",
        "name": "Revanth",
        "is_admin": False,
        "company": "Proyuga",
        "teams": [
            "Discovery Team", "Tech Team"
        ],
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    },
    {
        "email": "jayakiran@ibhubs.co",
        "name": "Jayakiran",
        "is_admin": False,
        "company": "Proyuga",
        "teams": [
            "iB Studio Team"
        ],
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    },
    {
        "email": "durga@ibhubs.co",
        "name": "Durga",
        "is_admin": False,
        "company": "iBHubs",
        "teams": [
            "Tech Team"
        ],
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    },
    {
        "email": "rajesh@ibhubs.co",
        "name": "Rajesh",
        "is_admin": False,
        "company": "iBHubs",
        "teams": [
            "Tech Team"
        ],
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    },
    {
        "email": "anilkumar@ibhubs.co",
        "name": "Anil Kumar",
        "is_admin": False,
        "company": "iBHubs",
        "teams": [
            "Tech Team"
        ],
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    },
    {
        "email": "sankar@ibhubs.co",
        "name": "Sankar",
        "is_admin": False,
        "company": "iBHubs",
        "teams": [
            "Tech Team"
        ],
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    },
    {
        "email": "rakesh@ibhubs.co",
        "name": "Rakesh",
        "is_admin": False,
        "company": "iBHubs",
        "teams": [
            "Tech Team"
        ],
        "roles": ["ALL_ROLES"],
        "project_id": "FIN_MAN"
    }
]

SUPERIOR_WITH_SUBORDINATE_USERS = [
    {
        "level_hierarchy": 2,
        "superior_email": "vasanth@ibhubs.co",
        "subordinate_emails": ["vedavidh@ibhubs.co", "revanth@ibhubs.co"]
    },
    {
        "level_hierarchy": 1,
        "superior_email": "vedavidh@ibhubs.co",
        "subordinate_emails": ["durga@ibhubs.co"]
    },
    {
        "level_hierarchy": 1,
        "superior_email": "revanth@ibhubs.co",
        "subordinate_emails": ["rajesh@ibhubs.co"]
    },
    {
        "level_hierarchy": 0,
        "superior_email": "rajesh@ibhubs.co",
        "subordinate_emails": ["anilkumar@ibhubs.co", "sankar@ibhubs.co", ]
    },
    {
        "level_hierarchy": 0,
        "superior_email": "durga@ibhubs.co",
        "subordinate_emails": ["rakesh@ibhubs.co"]
    }
]

TEAM_USERS_LEVELS = [
    {
        "team_name": "Tech Team",
        "level_name": "Senior RP",
        "level_hierarchy": 3
    },
    {
        "team_name": "Tech Team",
        "level_name": "RP",
        "level_hierarchy": 2
    },
    {
        "team_name": "Tech Team",
        "level_name": "Support RP",
        "level_hierarchy": 1
    },
    {
        "team_name": "Tech Team",
        "level_name": "Developers",
        "level_hierarchy": 0
    }
]

LEVELS_WISE_USERS = [
    {
        "level_name": "Senior RP",
        "user_emails": [
            "vasanth@ibhubs.co", "thrivikram@ibhubs.co", "kavya@ibhubs.co"
        ]
    },
    {
        "level_name": "RP",
        "user_emails": ["vedavidh@ibhubs.co", "revanth@ibhubs.co"]
    },
    {
        "level_name": "Support RP",
        "user_emails": ["durga@ibhubs.co", "rajesh@ibhubs.co"]
    },
    {
        "level_name": "Developers",
        "user_emails": [
            "anilkumar@ibhubs.co", "sankar@ibhubs.co", "rakesh@ibhubs.co"
        ]
    }
]


def get_admin_user_id():
    return UserDetails.objects.first().user_id


def get_team_member_level_id(level_name: str, team_id: str) -> str:
    from ib_iam.models import TeamMemberLevel
    return str(
        TeamMemberLevel.objects.get(team_id=team_id, level_name=level_name).id
    )


def get_user_ids_for_given_emails(user_emails: List[str]) -> List[str]:
    from ib_users.models import UserAccount
    user_ids = list(UserAccount.objects.filter(
        email__in=user_emails
    ).values_list("user_id", flat=True))
    return list(map(str, user_ids))


@transaction.atomic()
def populate_projects(spread_sheet_name: str):
    from ib_iam.populate.add_projects import Project
    project = Project()
    from ib_iam.constants.config import PROJECT_SUBSHEET_NAME
    project.add_projects_to_database(
        spread_sheet_name=spread_sheet_name,
        sub_sheet_name=PROJECT_SUBSHEET_NAME
    )


def populate_teams(teams: List[dict]):
    from ib_iam.storages.team_storage_implementation import (
        TeamStorageImplementation
    )
    from ib_iam.interactors.storage_interfaces.dtos import (
        TeamNameAndDescriptionDTO
    )
    for team in teams:
        team_name_and_description_dto = TeamNameAndDescriptionDTO(
            name=team["name"], description=team["description"]
        )
        team_storage = TeamStorageImplementation()
        team_storage.add_team(
            user_id=team["created_by_id"],
            team_name_and_description_dto=team_name_and_description_dto
        )


def populate_companies(companies: List[dict]):
    from ib_iam.interactors.storage_interfaces.dtos import (
        CompanyNameLogoAndDescriptionDTO
    )
    from ib_iam.storages.company_storage_implementation import (
        CompanyStorageImplementation
    )
    for company in companies:
        company_dto = CompanyNameLogoAndDescriptionDTO(
            name=company["name"], description=company["description"],
            logo_url=company["logo_url"]
        )
        company_storage = CompanyStorageImplementation()
        company_storage.add_company(
            company_name_logo_and_description_dto=company_dto
        )


def populate_team_user_levels(team_name: str, team_user_levels: List[dict]):
    team_id = get_team_ids(team_names=[team_name])[0]
    from ib_iam.interactors.dtos.dtos import TeamMemberLevelDTO
    team_member_level_dtos = [
        TeamMemberLevelDTO(
            team_member_level_name=team_user_level["level_name"],
            level_hierarchy=team_user_level["level_hierarchy"]
        )
        for team_user_level in team_user_levels
    ]

    from ib_iam.storages.team_member_level_storage_implementation import (
        TeamMemberLevelStorageImplementation
    )
    team_member_level_storage = TeamMemberLevelStorageImplementation()
    from ib_iam.storages.user_storage_implementation import (
        UserStorageImplementation
    )
    user_storage = UserStorageImplementation()

    from ib_iam.interactors.add_team_member_levels_interactor import (
        AddTeamMemberLevelsInteractor
    )
    interactor = AddTeamMemberLevelsInteractor(
        team_member_level_storage=team_member_level_storage,
        user_storage=user_storage
    )
    interactor.add_team_member_levels(
        team_id=team_id, team_member_level_dtos=team_member_level_dtos,
        user_id=get_admin_user_id()
    )


def populate_users_to_team_user_levels(
        team_name: str, levels_wise_users: List[dict]
):
    team_id = get_team_ids(team_names=[team_name])[0]
    from ib_iam.interactors.dtos.dtos import TeamMemberLevelIdWithMemberIdsDTO
    levels_wise_users = [
        TeamMemberLevelIdWithMemberIdsDTO(
            team_member_level_id=get_team_member_level_id(
                level_name=level_wise_users["level_name"], team_id=team_id
            ),
            member_ids=get_user_ids_for_given_emails(
                user_emails=level_wise_users["user_emails"]
            )
        )
        for level_wise_users in levels_wise_users
    ]

    from ib_iam.storages.team_member_level_storage_implementation import (
        TeamMemberLevelStorageImplementation
    )
    team_member_level_storage = TeamMemberLevelStorageImplementation()
    from ib_iam.storages.user_storage_implementation import (
        UserStorageImplementation
    )
    user_storage = UserStorageImplementation()

    from ib_iam.interactors.add_members_to_team_member_levels_interactor import (
        AddMembersToTeamMemberLevelsInteractor
    )
    interactor = AddMembersToTeamMemberLevelsInteractor(
        team_member_level_storage=team_member_level_storage,
        user_storage=user_storage
    )
    interactor.add_members_to_team_member_levels(
        team_id=team_id, user_id=get_admin_user_id(),
        team_member_level_id_with_member_ids_dtos=levels_wise_users
    )


def populate_superior_users_and_subordinate_users_with_level_hierarchy(
        superior_with_subordinate_users: List[dict],
        team_name: str
):
    team_id = get_team_ids(team_names=[team_name])[0]
    for superior_with_subordinates in superior_with_subordinate_users:
        from ib_iam.interactors.dtos.dtos import (
            ImmediateSuperiorUserIdWithUserIdsDTO
        )
        immediate_superior_user_id_with_member_ids_dtos = [
            ImmediateSuperiorUserIdWithUserIdsDTO(
                immediate_superior_user_id=get_user_ids_for_given_emails(
                    user_emails=[
                        superior_with_subordinates["superior_email"]]
                )[0],
                member_ids=get_user_ids_for_given_emails(
                    user_emails=superior_with_subordinates[
                        "subordinate_emails"]
                )
            )
        ]

        from ib_iam.storages.team_member_level_storage_implementation import (
            TeamMemberLevelStorageImplementation
        )
        team_member_level_storage = TeamMemberLevelStorageImplementation()
        from ib_iam.storages.user_storage_implementation import (
            UserStorageImplementation
        )
        user_storage = UserStorageImplementation()

        from ib_iam.interactors.add_members_to_superiors_interactor import (
            AddMembersToSuperiorsInteractor
        )
        interactor = AddMembersToSuperiorsInteractor(
            team_member_level_storage=team_member_level_storage,
            user_storage=user_storage
        )
        interactor.add_members_to_superiors(
            team_id=team_id, user_id=get_admin_user_id(),
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_user_id_with_member_ids_dtos,
            member_level_hierarchy=superior_with_subordinates[
                "level_hierarchy"]
        )


@transaction.atomic()
def populate_companies_and_teams(companies: List[dict], teams: List[dict]):
    populate_companies(companies=companies)
    populate_teams(teams=teams)


@transaction.atomic()
def populate_initial_users(users: List[dict]):
    populate_complete_user_details_bulk(users=users)


@transaction.atomic()
def populate_levels(
        team_name: str, superior_with_subordinate_users: List[dict],
        team_user_levels: List[dict], levels_wise_users: List[dict]
):
    populate_team_user_levels(
        team_name=team_name, team_user_levels=team_user_levels
    )
    populate_users_to_team_user_levels(
        team_name=team_name, levels_wise_users=levels_wise_users
    )
    populate_superior_users_and_subordinate_users_with_level_hierarchy(
        team_name=team_name,
        superior_with_subordinate_users=superior_with_subordinate_users
    )
