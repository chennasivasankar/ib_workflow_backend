from django.db import transaction


def get_team_ids(team_names):
    from ib_iam.models import Team
    teams_ids = list(Team.objects.filter(name__in=team_names).values_list(
        "team_id", flat=True))
    return teams_ids


def get_company_id(company_name):
    from ib_iam.models import Company
    company_id = str(Company.objects.get(name=company_name).company_id)
    return company_id


def get_role_ids_bulk():
    from ib_iam.models import Role
    db_role_ids = list(Role.objects.values_list('id', flat=True))
    return db_role_ids


@transaction.atomic()
def populate_projects(spread_sheet_name: str):
    from ib_iam.populate.add_projects import Project
    project = Project()
    from ib_iam.constants.config import PORJECT_SUBSHEET_NAME
    project.add_projects_to_database(
        spread_sheet_name=spread_sheet_name,
        sub_sheet_name=PORJECT_SUBSHEET_NAME
    )


@transaction.atomic()
def populate(spread_sheet_name: str):
    from ib_iam.populate.add_roles_details import RoleDetails
    # role = RoleDetails()
    # from ib_iam.constants.config import ROLES_SUBSHEET_NAME
    # role.add_roles_details_to_database(spread_sheet_name, ROLES_SUBSHEET_NAME)
    populate_admin_users_with_roles()
    populate_companies()
    populate_teams()
    populate_test_users()


def populate_admin_users_with_roles():
    admin_users = [
        {
            "name": "Pavan",
            "email": "ibadmin@ibhubs.co",
            "password": "Admin123@",
            "is_admin": True
        },
        {
            "name": "Rajesh",
            "email": "cybereyeadmin@ibhubs.co",
            "password": "Admin123@",
            "is_admin": True
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
        populate_user_roles_for_admin_user(admin_user_id=user_id)


def populate_user_roles_for_admin_user(admin_user_id: str):
    """
    Admin User have All roles
    """
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    db_role_ids = get_role_ids_bulk()
    user_storage = UserStorageImplementation()
    user_storage.add_roles_to_the_user(
        user_id=admin_user_id, role_ids=db_role_ids)


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


def populate_test_users():
    users = [
        {
            "email": "vasanth@ibhubs.co",
            "name": "Vasanth",
            "password": "Sample123@",
            "is_admin": False,
            "company_name": "iBHubs",
            "teams": [
                "Tech Team"
            ],
            "roles": [
                "FIN_INVOICE_APPROVER"
            ]
        },
        {
            "email": "thrivikram@ibhubs.co",
            "name": "Thrivikram",
            "password": "Sample123@",
            "is_admin": False,
            "company_name": "Proyuga",
            "teams": [
                "Tech Team"
            ],
            "roles": [
                "FIN_INVOICE_APPROVER"
            ]
        },
        {
            "email": "kavya@ibhubs.co",
            "name": "Kavya",
            "password": "Sample123@",
            "is_admin": False,
            "company_name": "CyberEye",
            "teams": [
                "Tech Team", "Discovery Team"
            ],
            "roles": [
                "FIN_INVOICE_APPROVER", "FIN_FINANCE_RP"
            ]
        },
        {
            "email": "ramganesh@ibhubs.co",
            "name": "Ramganesh",
            "password": "Sample123@",
            "is_admin": False,
            "company_name": "CyberEye",
            "teams": [
                "Tech Team"
            ],
            "roles": [
                "FIN_FINANCE_RP"
            ]
        },
        {
            "email": "vedavidh@ibhubs.co",
            "name": "Vedavidh",
            "password": "Sample123@",
            "is_admin": False,
            "company_name": "iBHubs",
            "teams": [
                "iB Studio Team", "Tech Team"
            ],
            "roles": [
                "FIN_ADMIN", "FIN_PAYMENT_REQUESTER"
            ]
        },
        {
            "email": "revanth@ibhubs.co",
            "name": "Revanth",
            "password": "Sample123@",
            "is_admin": False,
            "company_name": "Proyuga",
            "teams": [
                "Discovery Team"
            ],
            "roles": [
                "FIN_PAYMENT_REQUESTER"
            ]
        },
        {
            "email": "jayakiran@ibhubs.co",
            "name": "Jayakiran",
            "password": "Sample123@",
            "is_admin": False,
            "company_name": "Proyuga",
            "teams": [
                "iB Studio Team"
            ],
            "roles": [
                "FIN_ADMIN"
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
            role_ids=user["roles"],
            company_id=company_id
        )
        interactor.add_new_user(
            user_id=admin_user_id,
            add_user_details_dto=complete_user_details_dto
        )
