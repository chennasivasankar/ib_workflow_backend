from typing import List

from django.db import transaction

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.models import ProjectRole, ProjectTeam

USERS = [
    {
        "name": "Payment Requester",
        "email": "paymentrequester@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Payment Requester"],
        "project_id": "FIN_MAN"
    },
    {
        "name": "Payment POC",
        "email": "paymentpoc@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Payment POC"],
        "project_id": "FIN_MAN"
    },
    {
        "name": "Payment Approver",
        "email": "paymentapprover@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Payment Approver"],
        "project_id": "FIN_MAN"
    },
    {
        "name": "Payments Level One Verifier",
        "email": "payment_level1_verifier@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Payments Level-1 Verifier"],
        "project_id": "FIN_MAN"
    }, {
        "name": "Payments Level Two Verifier",
        "email": "payment_level2_verifier@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Payments Level-2 Verifier"],
        "project_id": "FIN_MAN"
    }, {
        "name": "Payments Level Three Verifier",
        "email": "payment_level3_verifier@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Payments Level-3 Verifier"],
        "project_id": "FIN_MAN"
    }, {
        "name": "Payments RP",
        "email": "payment_rp@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Payments RP"],
        "project_id": "FIN_MAN"
    }, {
        "name": "Finance RP",
        "email": "finance_rp@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Finance RP"],
        "project_id": "FIN_MAN"
    }, {
        "name": "Accounts Level One Verifier",
        "email": "accounts_level1_verifier@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Accounts Level-1 Verifier"],
        "project_id": "FIN_MAN"
    }, {
        "name": "Accounts Level Two Verifier",
        "email": "accounts_level2_verifier@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Accounts Level-2 Verifier"],
        "project_id": "FIN_MAN"
    }, {
        "name": "Accounts Level Three Verifier",
        "email": "accounts_level3_verifier@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Accounts Level-3 Verifier"],
        "project_id": "FIN_MAN"
    }, {
        "name": "Accounts Level Four Verifier",
        "email": "account_level4_verifier@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Accounts Level-4 Verifier"],
        "project_id": "FIN_MAN"
    }, {
        "name": "Accounts Level Five Verifier",
        "email": "account_level5_verifier@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Accounts Level-5 Verifier"],
        "project_id": "FIN_MAN"
    }, {
        "name": "Compliance Verifier",
        "email": "compliance_verifier@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Compliance Verifier"],
        "project_id": "FIN_MAN"
    }, {
        "name": "Compliance Approver",
        "email": "compliance_approver@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Compliance Approver"],
        "project_id": "FIN_MAN"
    }, {
        "name": "Invoice Verifer",
        "email": "invoice_verifier@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Invoice Verifer"],
        "project_id": "FIN_MAN"
    }, {
        "name": "Invoice Approver",
        "email": "invoice_approver@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Invoice Approver"],
        "project_id": "FIN_MAN"
    },
    {
        "name": "Finance Admin",
        "email": "finance_admin@gmail.com",
        "company": "iBHubs",
        "teams": [
            "Tech Team",
            "Discovery Team",
            "iB Studio Team",
            "Assert Management Team"
        ],
        "is_admin": False,
        "roles": ["Finance Admin"],
        "project_id": "FIN_MAN"
    }
]


@transaction.atomic()
def populate_complete_user_details_bulk(users: List[dict]):
    for user in users:
        company_id = get_company_id(company_name=user["company"])
        password = user.get("password", None)
        user_id = create_user(
            company_id=company_id, email=user["email"],
            name=user["name"], is_admin=user["is_admin"], password=password
        )
        assign_user_roles(user_id=user_id, roles=user["roles"])
        team_ids = get_team_ids(team_names=user["teams"])
        assign_user_teams(user_id=user_id, team_ids=team_ids)
        assign_project_teams(project_id=user["project_id"], team_ids=team_ids)


def assign_project_teams(project_id: str, team_ids: List[str]):
    valid_project_team_ids = ProjectTeam.objects.filter(
        project_id=project_id, team_id__in=team_ids
    ).values_list('team_id', flat=True)
    valid_team_ids = list(map(str, valid_project_team_ids))
    remaining_team_ids = list(set(team_ids) - set(valid_team_ids))
    if remaining_team_ids:
        project_team_objects = [
            ProjectTeam(project_id=project_id, team_id=team_id)
            for team_id in remaining_team_ids
        ]
        ProjectTeam.objects.bulk_create(project_team_objects)


def create_user(
        email: str, name: str, is_admin: bool, company_id: str,
        password: str = None
):
    user_id = create_user_in_ib_users(
        email=email, name=name, password=password
    )
    create_user_in_ib_iam(
        name=name, user_id=user_id, is_admin=is_admin, company_id=company_id
    )
    return user_id


def assign_user_roles(user_id: str, roles: List[str]):
    from ib_iam.models import UserRole
    role_ids = get_role_ids(role_names=roles)
    UserRole.objects.filter(
        user_id=user_id, project_role_id__in=role_ids
    ).delete()
    user_role_objects = [
        UserRole(user_id=user_id, project_role_id=role_id)
        for role_id in role_ids
    ]
    UserRole.objects.bulk_create(user_role_objects)


def get_role_ids(role_names: List[str]) -> List[str]:
    role_ids = ProjectRole.objects.filter(
        name__in=role_names
    ).values_list("role_id", flat=True)
    return list(role_ids)


def create_user_in_ib_iam(
        user_id: str, name: str, is_admin: bool, company_id: str
):
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    user_storage = UserStorageImplementation()
    user_storage.create_user(
        is_admin=is_admin, company_id=company_id,
        user_id=user_id, name=name
    )
    create_elastic_user(user_id=user_id, name=name)


def get_company_id(company_name: str) -> str:
    from ib_iam.models import Company
    company_id = Company.objects.get(name=company_name).company_id
    return str(company_id)


def assign_user_teams(user_id: str, team_ids: List[str]):
    from ib_iam.storages.user_storage_implementation import \
        UserStorageImplementation
    user_storage = UserStorageImplementation()
    user_storage.add_user_to_the_teams(user_id=user_id, team_ids=team_ids)


def get_team_ids(team_names: List[str]) -> List[str]:
    from ib_iam.models import Team
    team_ids = Team.objects.filter(name__in=team_names).values_list(
        "team_id", flat=True)
    team_ids = list(map(str, team_ids))
    return team_ids


def create_user_in_ib_users(email: str, name: str, password: str = None):
    new_user_id = create_user_account_with_email(
        email=email, password=password
    )
    create_user_profile(user_id=new_user_id, email=email, name=name)
    return new_user_id


def create_user_account_with_email(email: str, password: str = None) -> str:
    from ib_iam.adapters.service_adapter import get_service_adapter
    service_adapter = get_service_adapter()
    user_id = service_adapter.user_service.create_user_account_with_email(
        email=email, password=password
    )
    return str(user_id)


def create_user_profile(user_id: str, email: str, name: str):
    from ib_iam.adapters.service_adapter import get_service_adapter
    service_adapter = get_service_adapter()
    user_profile_dto = create_user_profile_dto(
        name=name, email=email, user_id=user_id
    )
    service_adapter.user_service.create_user_profile(
        user_id=user_id, user_profile_dto=user_profile_dto
    )


def create_user_profile_dto(
        name: str, email: str, user_id: str
) -> UserProfileDTO:
    user_profile_dto = UserProfileDTO(
        name=name,
        email=email,
        user_id=user_id
    )
    return user_profile_dto


def create_elastic_user(user_id: str, name: str):
    from ib_iam.storages.elastic_storage_implementation import \
        ElasticStorageImplementation
    elastic_storage = ElasticStorageImplementation()
    elastic_storage.create_elastic_user(user_id=user_id, name=name)
