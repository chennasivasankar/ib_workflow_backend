import factory

from ib_iam.interactors.storage_interfaces.dtos \
    import UserTeamDTO, UserCompanyDTO, UserRoleDTO, UserDTO, TeamIdAndNameDTO, \
    CompanyIdAndNameDTO, RoleDTO, TeamDTO


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDTO

    user_id = factory.sequence(lambda number: "team%s" % number)
    is_admin = True
    company_id = factory.sequence(lambda number: "company%s" % number)


class UserTeamDTOFactory(factory.Factory):
    class Meta:
        model = UserTeamDTO

    user_id = factory.sequence(lambda number: "user%s" % number)
    team_id = factory.sequence(lambda number: "team%s" % number)
    team_name = factory.sequence(lambda number: "team %s" % number)


class UserCompanyDTOFactory(factory.Factory):
    class Meta:
        model = UserCompanyDTO

    user_id = factory.sequence(lambda number: "team%s" % number)
    company_id = factory.sequence(lambda number: "company%s" % number)
    company_name = factory.sequence(lambda number: "company %s" % number)


class UserRoleDTOFactory(factory.Factory):
    class Meta:
        model = UserRoleDTO

    user_id = factory.sequence(lambda number: "team%s" % number)
    role_id = factory.Sequence(lambda n: 'PAYMENT%s' % n)
    name = factory.Sequence(lambda n: 'payment %s' % n)
    description = factory.Sequence(lambda n: 'payment_description%s' % n)


class CompanyIdAndNameDTOFactory(factory.Factory):
    class Meta:
        model = CompanyIdAndNameDTO

    company_id = factory.Sequence(lambda n: 'Company%s' % n)
    company_name = factory.Sequence(lambda n: 'company %s' % n)


class RoleDTOFactory(factory.Factory):
    class Meta:
        model = RoleDTO

    role_id = factory.Sequence(lambda n: 'PAYMENT%s' % n)
    name = factory.Sequence(lambda n: 'payment%s' % n)
    description = factory.Sequence(lambda n: 'payment_description%s' % n)


class TeamIdAndNameDTOFactory(factory.Factory):
    class Meta:
        model = TeamIdAndNameDTO

    team_id = factory.sequence(lambda number: "team%s" % number)
    team_name = factory.sequence(lambda number: "team %s" % number)


from ib_iam.interactors.storage_interfaces.dtos import (
    BasicUserDetailsDTO,
    TeamUserIdsDTO,
    TeamNameAndDescriptionDTO,
    PaginationDTO,
    TeamsWithTotalTeamsCountDTO,
    TeamDetailsWithUserIdsDTO,
    TeamWithUserIdsDTO,
    CompanyDTO,
    CompanyIdWithEmployeeIdsDTO,
    CompanyNameLogoAndDescriptionDTO,
    CompanyDetailsWithUserIdsDTO,
    CompanyWithUserIdsDTO
)

team_ids = [
    "f2c02d98-f311-4ab2-8673-3daa00757002",
    "aa66c40f-6d93-484a-b418-984716514c7b",
    "c982032b-53a7-4dfa-a627-4701a5230765"
]

user_ids = [
    '2bdb417e-4632-419a-8ddd-085ea272c6eb',
    '548a803c-7b48-47ba-a700-24f2ea0d1280',
    '4b8fb6eb-fa7d-47c1-8726-cd917901104e'
]

member_ids = user_ids
employee_ids = user_ids



class TeamUserIdsDTOFactory(factory.Factory):
    class Meta:
        model = TeamUserIdsDTO

    team_id = factory.Faker("uuid4")
    user_ids = factory.Iterator([
        [user_ids[1], user_ids[2]],
        [user_ids[0], user_ids[1]],
        [user_ids[0], user_ids[2]]
    ])


class BasicUserDetailsDTOFactory(factory.Factory):
    class Meta:
        model = BasicUserDetailsDTO

    user_id = factory.sequence(lambda n: "user%d" % n)
    name = factory.sequence(lambda n: "name%d" % n)
    profile_pic_url = factory.sequence(lambda n: "url%d" % n)


class TeamNameAndDescriptionDTOFactory(factory.Factory):
    class Meta:
        model = TeamNameAndDescriptionDTO

    name = factory.sequence(lambda n: "team%d" % n)
    description = factory.sequence(lambda n: "team_description%d" % n)


class TeamDetailsWithUserIdsDTOFactory(
    TeamNameAndDescriptionDTOFactory, factory.Factory
):
    class Meta:
        model = TeamDetailsWithUserIdsDTO

    user_ids = factory.Iterator([
        [user_ids[0], user_ids[2]],
        [user_ids[2], user_ids[1]],
        [user_ids[2], user_ids[1]]
    ])


class TeamWithUserIdsDTOFactory(TeamDetailsWithUserIdsDTOFactory,
                                factory.Factory):
    class Meta:
        model = TeamWithUserIdsDTO

    team_id = factory.sequence(lambda n: "team%d" % n)


class PaginationDTOFactory(factory.Factory):
    class Meta:
        model = PaginationDTO

    limit = factory.Iterator([5, 6, 3])
    offset = factory.Iterator([4, 3, 10])


class TeamDTOFactory(factory.Factory):
    class Meta:
        model = TeamDTO

    team_id = factory.sequence(lambda number: "team %s" % number)
    name = factory.sequence(lambda number: "team %s" % number)
    description = factory.sequence(lambda n: "team_description %d" % n)


team_dtos = [
    TeamDTOFactory(team_id=team_id) for team_id in team_ids
]


class TeamsWithTotalTeamsCountDTOFactory(factory.Factory):
    class Meta:
        model = TeamsWithTotalTeamsCountDTO

    teams = factory.Iterator([
        [team_dtos[0], team_dtos[1]],
        [team_dtos[1], team_dtos[2]]
    ])
    total_teams_count = 2


class CompanyNameLogoAndDescriptionDTOFactory(factory.Factory):
    class Meta:
        model = CompanyNameLogoAndDescriptionDTO

    name = factory.sequence(lambda n: "company1")
    description = factory.sequence(lambda n: "company_description%d" % n)
    logo_url = factory.sequence(lambda n: "logo_url%d" % n)


class CompanyDTOFactory(
    CompanyNameLogoAndDescriptionDTOFactory, factory.Factory
):
    class Meta:
        model = CompanyDTO

    company_id = factory.Faker("uuid4")


class CompanyIdWithEmployeeIdsDTOFactory(factory.Factory):
    class Meta:
        model = CompanyIdWithEmployeeIdsDTO

    company_id = factory.Faker("uuid4")
    employee_ids = factory.Iterator([
        [employee_ids[0], employee_ids[1]],
        [employee_ids[1], employee_ids[2]],
        [employee_ids[0], employee_ids[2]]
    ])


class CompanyDetailsWithUserIdsDTOFactory(
    CompanyNameLogoAndDescriptionDTOFactory, factory.Factory
):
    class Meta:
        model = CompanyDetailsWithUserIdsDTO

    user_ids = factory.Iterator([
        [user_ids[0], user_ids[2]],
        [user_ids[2], user_ids[1]],
        [user_ids[2], user_ids[1]]
    ])


class CompanyWithUserIdsDTOFactory(
    CompanyDetailsWithUserIdsDTOFactory, factory.Factory
):
    class Meta:
        model = CompanyWithUserIdsDTO

    company_id = factory.Faker("uuid4")


class EmployeeDTOFactory(factory.Factory):
    class Meta:
        model = EmployeeDTO

    employee_id = factory.sequence(lambda n: "user_id-%d" % n)
    name = factory.sequence(lambda n: "user%d" % n)
    profile_pic_url = factory.sequence(lambda n: "url%d" % n)
