def reset_sequence_for_model_factories():
    reset_sequence_user_details_factory()
    reset_sequence_company_factory()
    reset_sequence_role_factory()
    reset_sequence_team_factory()
    reset_sequence_user_team_factory()
    reset_sequence_user_role_factory()
    

def reset_sequence_for_dto_factory():
    reset_sequence_for_user_dto_factory()
    reset_sequence_for_company_dto_factory()
    reset_sequence_for_team_dto_factory()
    reset_sequence_for_role_dto_factory()
    reset_sequence_for_user_role_dto_factory()
    reset_sequence_for_user_profile_dto_factory()
    reset_sequence_for_user_team_dto_factory()
    reset_sequence_for_user_company_dto_factory()


def reset_sequence_for_company_dto_factory():
    from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
    CompanyDTOFactory.reset_sequence(0)


def reset_sequence_for_user_dto_factory():
    from ib_iam.tests.factories.storage_dtos import UserDTOFactory
    UserDTOFactory.reset_sequence(0)


def reset_sequence_for_team_dto_factory():
    from ib_iam.tests.factories.storage_dtos import TeamDTOFactory
    TeamDTOFactory.reset_sequence(0)


def reset_sequence_for_role_dto_factory():
    from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
    RoleDTOFactory.reset_sequence(0)


def reset_sequence_for_user_role_dto_factory():
    from ib_iam.tests.factories.storage_dtos import UserRoleDTOFactory
    UserRoleDTOFactory.reset_sequence(0)


def reset_sequence_for_user_profile_dto_factory():
    from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
    UserProfileDTOFactory.reset_sequence(0)


def reset_sequence_for_user_team_dto_factory():
    from ib_iam.tests.factories.storage_dtos import UserTeamDTOFactory
    UserTeamDTOFactory.reset_sequence(0)


def reset_sequence_for_user_company_dto_factory():
    from ib_iam.tests.factories.storage_dtos import UserCompanyDTOFactory
    UserCompanyDTOFactory.reset_sequence(0)


def reset_sequence_company_factory():
    from ib_iam.tests.factories.models import CompanyFactory
    CompanyFactory.reset_sequence(0)


def reset_sequence_role_factory():
    from ib_iam.tests.factories.models import RoleFactory
    RoleFactory.reset_sequence(0)


def reset_sequence_team_factory():
    from ib_iam.tests.factories.models import TeamFactory
    TeamFactory.reset_sequence(0)


def reset_sequence_user_details_factory():
    from ib_iam.tests.factories.models import UserDetailsFactory
    UserDetailsFactory.reset_sequence(0)


def reset_sequence_user_team_factory():
    from ib_iam.tests.factories.models import UserTeamFactory
    UserTeamFactory.reset_sequence(0)


def reset_sequence_user_role_factory():
    from ib_iam.tests.factories.models import UserRoleFactory
    UserRoleFactory.reset_sequence(0)
