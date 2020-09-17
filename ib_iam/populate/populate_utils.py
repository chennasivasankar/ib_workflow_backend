from typing import List

from django.db import transaction

from ib_iam.models import UserDetails


def get_admin_user_id():
    return UserDetails.objects.first().user_id


def get_team_ids(team_names):
    from ib_iam.models import Team
    teams_ids = list(Team.objects.filter(name__in=team_names).values_list(
        "team_id", flat=True))
    return teams_ids


def get_company_id(company_name):
    from ib_iam.models import Company
    company_id = str(Company.objects.get(name=company_name).company_id)
    return company_id


def get_role_ids_bulk_for_given_project(project_id: str):
    from ib_iam.models import ProjectRole
    role_ids = list(ProjectRole.objects.filter(
        project_id=project_id).values_list('role_id', flat=True))
    return role_ids


def get_team_member_level_id(level_name: str, team_id: str) -> str:
    from ib_iam.models import TeamMemberLevel
    return str(TeamMemberLevel.objects.get(
        team_id=team_id, level_name=level_name).id)


def get_user_ids_for_given_emails(user_emails: List[str]) -> List[str]:
    from ib_users.models import UserAccount
    user_ids = list(UserAccount.objects.filter(
        email__in=user_emails).values_list("user_id", flat=True))
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


def populate_teams():
    teams = [
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
    from ib_iam.storages.team_storage_implementation import \
        TeamStorageImplementation
    from ib_iam.interactors.storage_interfaces.dtos import \
        TeamNameAndDescriptionDTO
    for team in teams:
        team_name_and_description_dto = TeamNameAndDescriptionDTO(
            name=team["name"], description=team["description"])
        team_storage = TeamStorageImplementation()
        team_storage.add_team(
            user_id=team["created_by_id"],
            team_name_and_description_dto=team_name_and_description_dto)


def populate_companies():
    companies = [
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
    from ib_iam.interactors.storage_interfaces.dtos import \
        CompanyNameLogoAndDescriptionDTO
    from ib_iam.storages.company_storage_implementation import \
        CompanyStorageImplementation
    for company in companies:
        company_dto = CompanyNameLogoAndDescriptionDTO(
            name=company["name"], description=company["description"],
            logo_url=company["logo_url"])

        company_storage = CompanyStorageImplementation()
        company_storage.add_company(
            company_name_logo_and_description_dto=company_dto)


def populate_project_teams_for_given_project(project_id: str):
    from ib_iam.models import Team
    teams_ids = list(Team.objects.all().values_list('team_id', flat=True))
    from ib_iam.models import ProjectTeam
    project_team_objects = [ProjectTeam(
        project_id=project_id, team_id=team_id
    ) for team_id in teams_ids]
    ProjectTeam.objects.bulk_create(project_team_objects)


def populate_user_roles_for_admin_user(admin_user_id: str, project_id: str):
    """
    Admin User have All roles
    """
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    role_ids = get_role_ids_bulk_for_given_project(project_id=project_id)
    user_storage = UserStorageImplementation()
    user_storage.add_roles_to_the_user(
        user_id=admin_user_id, role_ids=role_ids)


def populate_user_roles_for_normal_user(user_id: str, project_id: str):
    """
    Normal User have All roles
    """
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    user_storage = UserStorageImplementation()
    db_role_ids = get_role_ids_bulk_for_given_project(project_id=project_id)
    user_storage.add_roles_to_the_user(
        user_id=user_id, role_ids=db_role_ids)


def populate_admin_users_with_project_roles_and_teams(project_id: str):
    admin_users = [
        {
            "name": "Pavan",
            "email": "ibadmin@ibhubs.co",
            "password": "Admin123@",
            "is_admin": True,
            "teams": [
                "Tech Team",
                "Discovery Team",
                "iB Studio Team",
                "Assert Management Team"
            ]
        },
        {
            "name": "Lavanya",
            "email": "cybereyeadmin@ibhubs.co",
            "password": "Admin123@",
            "is_admin": True,
            "teams": [
                "Tech Team",
                "Discovery Team",
                "iB Studio Team",
                "Assert Management Team"
            ]
        }
    ]
    from ib_iam.adapters.dtos import UserProfileDTO
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    from ib_iam.adapters.service_adapter import get_service_adapter
    service_adapter = get_service_adapter()
    for admin_user in admin_users:
        user_id = service_adapter.user_service.create_user_account_with_email(
            email=admin_user["email"], password=admin_user["password"])
        user_profile_dto = UserProfileDTO(
            user_id=user_id, name=admin_user["name"],
            email=admin_user["email"])
        service_adapter.user_service.create_user_profile(
            user_id=user_id, user_profile_dto=user_profile_dto)
        user_storage = UserStorageImplementation()
        user_storage.create_user(is_admin=admin_user["is_admin"],
                                 name=admin_user["name"], user_id=user_id)
        team_ids = get_team_ids(team_names=admin_user["teams"])
        user_storage.add_user_to_the_teams(user_id=user_id, team_ids=team_ids)
        populate_user_roles_for_admin_user(
            admin_user_id=user_id, project_id=project_id)
        from ib_iam.storages.elastic_storage_implementation import \
            ElasticStorageImplementation
        elastic_storage = ElasticStorageImplementation()
        elastic_user_id = elastic_storage.create_elastic_user(
            user_id=user_id, name=admin_user["name"], email=admin_user["email"]
        )
        elastic_storage.create_elastic_user_intermediary(
            elastic_user_id=elastic_user_id, user_id=user_id
        )


def populate_test_users_for_given_project(project_id: str):
    users = [
        {
            "email": "vasanth@ibhubs.co",
            "name": "Vasanth",
            "is_admin": False,
            "company_name": "iBHubs",
            "teams": [
                "Tech Team"
            ]
        },
        {
            "email": "thrivikram@ibhubs.co",
            "name": "Thrivikram",
            "is_admin": False,
            "company_name": "Proyuga",
            "teams": [
                "Tech Team"
            ]
        },
        {
            "email": "kavya@ibhubs.co",
            "name": "Kavya",
            "is_admin": False,
            "company_name": "CyberEye",
            "teams": [
                "Tech Team", "Discovery Team"
            ]
        },
        {
            "email": "ramganesh@ibhubs.co",
            "name": "Ramganesh",
            "is_admin": False,
            "company_name": "CyberEye",
            "teams": [
                "Tech Team"
            ]
        },
        {
            "email": "vedavidh@ibhubs.co",
            "name": "Vedavidh",
            "is_admin": False,
            "company_name": "iBHubs",
            "teams": [
                "iB Studio Team", "Tech Team"
            ]
        },
        {
            "email": "revanth@ibhubs.co",
            "name": "Revanth",
            "is_admin": False,
            "company_name": "Proyuga",
            "teams": [
                "Discovery Team", "Tech Team"
            ]
        },
        {
            "email": "jayakiran@ibhubs.co",
            "name": "Jayakiran",
            "is_admin": False,
            "company_name": "Proyuga",
            "teams": [
                "iB Studio Team"
            ],
        },
        {
            "email": "durga@ibhubs.co",
            "name": "Durga",
            "is_admin": False,
            "company_name": "iBHubs",
            "teams": [
                "Tech Team"
            ]
        },
        {
            "email": "rajesh@ibhubs.co",
            "name": "Rajesh",
            "is_admin": False,
            "company_name": "iBHubs",
            "teams": [
                "Tech Team"
            ]
        },
        {
            "email": "anilkumar@ibhubs.co",
            "name": "Anil Kumar",
            "is_admin": False,
            "company_name": "iBHubs",
            "teams": [
                "Tech Team"
            ]
        },
        {
            "email": "sankar@ibhubs.co",
            "name": "Sankar",
            "is_admin": False,
            "company_name": "iBHubs",
            "teams": [
                "Tech Team"
            ]
        },
        {
            "email": "rakesh@ibhubs.co",
            "name": "Rakesh",
            "is_admin": False,
            "company_name": "iBHubs",
            "teams": [
                "Tech Team"
            ]
        },
    ]
    from ib_iam.interactors.add_new_user_interactor import \
        AddNewUserInteractor
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    from ib_iam.interactors.dtos.dtos import \
        AddUserDetailsDTO
    from ib_users.models import UserAccount
    admin_user_id = UserAccount.objects.get(email="ibadmin@ibhubs.co").user_id
    for user in users:
        team_ids = get_team_ids(team_names=user["teams"])
        company_id = get_company_id(company_name=user["company_name"])
        user_storage = UserStorageImplementation()
        from ib_iam.storages.elastic_storage_implementation import \
            ElasticStorageImplementation
        elastic_storage = ElasticStorageImplementation()
        interactor = AddNewUserInteractor(
            user_storage=user_storage, elastic_storage=elastic_storage)

        complete_user_details_dto = AddUserDetailsDTO(
            name=user["name"], email=user["email"], team_ids=team_ids,
            company_id=company_id
        )
        interactor.add_new_user(
            user_id=admin_user_id,
            add_user_details_dto=complete_user_details_dto
        )
        user_id = UserAccount.objects.get(email=user["email"]).user_id
        populate_user_roles_for_normal_user(
            user_id=user_id, project_id=project_id
        )


def populate_team_member_levels_for_tech_team():
    team_member_levels = [
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
    team_id = get_team_ids(team_names=["Tech Team"])[0]
    from ib_iam.interactors.dtos.dtos import TeamMemberLevelDTO
    team_member_level_dtos = [
        TeamMemberLevelDTO(
            team_member_level_name=team_member_level["level_name"],
            level_hierarchy=team_member_level["level_hierarchy"]
        )
        for team_member_level in team_member_levels
    ]

    from ib_iam.storages.team_member_level_storage_implementation import \
        TeamMemberLevelStorageImplementation
    team_member_level_storage = TeamMemberLevelStorageImplementation()
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    user_storage = UserStorageImplementation()

    from ib_iam.interactors.levels.add_team_member_levels_interactor import \
        AddTeamMemberLevelsInteractor
    interactor = AddTeamMemberLevelsInteractor(
        team_member_level_storage=team_member_level_storage,
        user_storage=user_storage
    )
    interactor.add_team_member_levels(
        team_id=team_id, team_member_level_dtos=team_member_level_dtos,
        user_id=get_admin_user_id()
    )


def populate_users_to_team_member_levels_for_tech_team():
    team_id = get_team_ids(team_names=["Tech Team"])[0]
    levels_wise_users = [
        {
            "level_name": "Senior RP",
            "users": ["vasanth@ibhubs.co", "thrivikram@ibhubs.co",
                      "kavya@ibhubs.co"]
        },
        {
            "level_name": "RP",
            "users": ["vedavidh@ibhubs.co", "revanth@ibhubs.co"]
        },
        {
            "level_name": "Support RP",
            "users": ["durga@ibhubs.co", "rajesh@ibhubs.co"]
        },
        {
            "level_name": "Developers",
            "users": ["anilkumar@ibhubs.co", "sankar@ibhubs.co",
                      "rakesh@ibhubs.co"]
        }
    ]
    from ib_iam.interactors.dtos.dtos import TeamMemberLevelIdWithMemberIdsDTO
    levels_wise_users = [
        TeamMemberLevelIdWithMemberIdsDTO(
            team_member_level_id=get_team_member_level_id(
                level_name=level_wise_users["level_name"], team_id=team_id),
            member_ids=get_user_ids_for_given_emails(
                user_emails=level_wise_users["users"])
        )
        for level_wise_users in levels_wise_users
    ]

    from ib_iam.storages.team_member_level_storage_implementation import \
        TeamMemberLevelStorageImplementation
    team_member_level_storage = TeamMemberLevelStorageImplementation()
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    user_storage = UserStorageImplementation()

    from ib_iam.interactors.levels.add_members_to_team_member_levels_interactor import \
        AddMembersToTeamMemberLevelsInteractor
    interactor = AddMembersToTeamMemberLevelsInteractor(
        team_member_level_storage=team_member_level_storage,
        user_storage=user_storage
    )
    interactor.add_members_to_team_member_levels(
        team_id=team_id, user_id=get_admin_user_id(),
        team_member_level_id_with_member_ids_dtos=levels_wise_users)


def populate_superior_users_and_subordinate_users_with_level_hierarchy_for_tech_team():
    team_id = get_team_ids(team_names=["Tech Team"])[0]
    superior_users_with_subordinate_users = [
        {
            "level_hierarchy": 2,
            "superior_user": "vasanth@ibhubs.co",
            "subordinate_users": ["vedavidh@ibhubs.co", "revanth@ibhubs.co"]
        },
        {
            "level_hierarchy": 1,
            "superior_user": "vedavidh@ibhubs.co",
            "subordinate_users": ["durga@ibhubs.co"]
        },
        {
            "level_hierarchy": 1,
            "superior_user": "revanth@ibhubs.co",
            "subordinate_users": ["rajesh@ibhubs.co"]
        },
        {
            "level_hierarchy": 0,
            "superior_user": "rajesh@ibhubs.co",
            "subordinate_users": ["anilkumar@ibhubs.co", "sankar@ibhubs.co", ]
        },
        {
            "level_hierarchy": 0,
            "superior_user": "durga@ibhubs.co",
            "subordinate_users": ["rakesh@ibhubs.co"]
        }
    ]
    for superior_with_subordinate_users in superior_users_with_subordinate_users:
        from ib_iam.interactors.dtos.dtos import \
            ImmediateSuperiorUserIdWithUserIdsDTO
        immediate_superior_user_id_with_member_ids_dtos = [
            ImmediateSuperiorUserIdWithUserIdsDTO(
                immediate_superior_user_id=get_user_ids_for_given_emails(
                    user_emails=[
                        superior_with_subordinate_users["superior_user"]]
                )[0],
                member_ids=get_user_ids_for_given_emails(
                    user_emails=superior_with_subordinate_users[
                        "subordinate_users"])
            )
        ]

        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        team_member_level_storage = TeamMemberLevelStorageImplementation()
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()

        from ib_iam.interactors.levels.add_members_to_superiors_interactor import \
            AddMembersToSuperiorsInteractor
        interactor = AddMembersToSuperiorsInteractor(
            team_member_level_storage=team_member_level_storage,
            user_storage=user_storage
        )
        interactor.add_members_to_superiors(
            team_id=team_id, user_id=get_admin_user_id(),
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_user_id_with_member_ids_dtos,
            member_level_hierarchy=superior_with_subordinate_users[
                "level_hierarchy"]
        )


@transaction.atomic()
def populate(spread_sheet_name: str):
    project_id = "FIN_MAN"
    populate_companies()
    populate_teams()
    populate_project_teams_for_given_project(project_id=project_id)
    populate_admin_users_with_project_roles_and_teams(project_id=project_id)
    populate_test_users_for_given_project(project_id=project_id)
    populate_team_member_levels_for_tech_team()
    populate_users_to_team_member_levels_for_tech_team()
    populate_superior_users_and_subordinate_users_with_level_hierarchy_for_tech_team()
