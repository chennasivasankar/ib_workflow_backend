import factory

from ib_iam.constants.enums import Searchable
from ib_iam.interactors.dtos.dtos import UserIdWithProjectIdAndStatusDTO
from ib_iam.interactors.storage_interfaces.dtos import (
    TeamWithUserIdDTO, UserCompanyDTO, UserRoleDTO, UserDTO, TeamIdAndNameDTO,
    CompanyIdAndNameDTO, RoleDTO, TeamDTO, UserIdAndNameDTO, MemberDTO,
    TeamMemberLevelDetailsDTO, UserProfileDTO, SearchableDetailsDTO,
    ProjectDTO, MemberIdWithSubordinateMemberIdsDTO, ProjectRoleDTO,
    ProjectWithoutIdDTO, ProjectWithDisplayIdDTO, RoleNameAndDescriptionDTO,
    ProjectRolesDTO, UserIdWithTokenDTO)


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDTO

    user_id = factory.sequence(lambda number: "team%s" % number)
    is_admin = True
    company_id = factory.sequence(lambda number: "company%s" % number)
    cover_page_url = "http://sample.com"


class UserTeamDTOFactory(factory.Factory):
    class Meta:
        model = TeamWithUserIdDTO

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
    role_id = factory.Sequence(lambda n: 'ROLE_%s' % n)
    name = factory.Sequence(lambda n: 'role %s' % n)
    description = factory.Sequence(lambda n: 'role description %s' % n)


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
    TeamWithUserIdsDTO,
    TeamWithTeamIdAndUserIdsDTO,
    CompanyDTO,
    CompanyIdWithEmployeeIdsDTO,
    CompanyNameLogoAndDescriptionDTO,
    CompanyWithUserIdsDTO,
    CompanyWithCompanyIdAndUserIdsDTO
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


class UserIdWithProjectIdAndStatusDTOFactory(factory.Factory):
    class Meta:
        model = UserIdWithProjectIdAndStatusDTO

    user_id = factory.Sequence(
        lambda n: "123e4567-e89b-12d3-a456-42661417400%d" % n)
    project_id = factory.Sequence(
        lambda n: "eca1a0c1-b9ef-4e59-b415-60a28ef17b1%d" % n)
    is_exist = factory.Iterator([True, False])


class ProjectRolesDTOFactory(factory.Factory):
    class Meta:
        model = ProjectRolesDTO

    project_id = factory.Sequence(
        lambda n: "project %d" % n)
    roles = factory.Iterator([["ROLE_1", "ROLE_2"],
                              ["ROLE_3", "ROLE_4"],
                              ["ROLE_5", "ROLE_6"]])


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
    profile_pic_url = "http://sample.com"


class TeamNameAndDescriptionDTOFactory(factory.Factory):
    class Meta:
        model = TeamNameAndDescriptionDTO

    name = factory.sequence(lambda n: "name%d" % n)
    description = factory.sequence(lambda n: "team_description%d" % n)


class TeamWithUserIdsDTOFactory(
    TeamNameAndDescriptionDTOFactory, factory.Factory
):
    class Meta:
        model = TeamWithUserIdsDTO

    user_ids = factory.Iterator([
        [user_ids[0], user_ids[2]],
        [user_ids[2], user_ids[1]],
        [user_ids[2], user_ids[1]]
    ])


class TeamWithTeamIdAndUserIdsDTOFactory(TeamWithUserIdsDTOFactory,
                                         factory.Factory):
    class Meta:
        model = TeamWithTeamIdAndUserIdsDTO

    team_id = factory.sequence(lambda n: "team%d" % n)


# TODO: move to interactor_dtos
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


class UserIdAndNameFactory(factory.Factory):
    class Meta:
        model = UserIdAndNameDTO

    user_id = factory.Iterator(user_ids)
    name = factory.Faker("name")


class CompanyNameLogoAndDescriptionDTOFactory(factory.Factory):
    class Meta:
        model = CompanyNameLogoAndDescriptionDTO

    name = factory.sequence(lambda n: "company%d" % n)
    description = factory.sequence(lambda n: "company_description%d" % n)
    logo_url = "http://sample.com"


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


class CompanyWithUserIdsDTOFactory(
    CompanyNameLogoAndDescriptionDTOFactory, factory.Factory
):
    class Meta:
        model = CompanyWithUserIdsDTO

    user_ids = factory.Iterator([
        [user_ids[0], user_ids[2]],
        [user_ids[2], user_ids[1]],
        [user_ids[2], user_ids[1]]
    ])


class CompanyWithCompanyIdAndUserIdsDTOFactory(
    CompanyWithUserIdsDTOFactory, factory.Factory
):
    class Meta:
        model = CompanyWithCompanyIdAndUserIdsDTO

    company_id = factory.Faker("uuid4")


class UserIdNameEmailAndProfilePicUrlDTOFactory(factory.Factory):
    class Meta:
        model = UserProfileDTO

    user_id = factory.Faker("uuid4")
    name = factory.Iterator(["username", "testuser", "dummyuser"])
    email = factory.sequence(lambda n: "email%d@gmail.com" % n)
    profile_pic_url = "http://sample.com"


class TeamMemberLevelDetailsDTOFactory(factory.Factory):
    class Meta:
        model = TeamMemberLevelDetailsDTO

    team_member_level_id = factory.Faker("uuid4")
    team_member_level_name = factory.Faker("name")
    level_hierarchy = factory.Iterator([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


class MemberDTOFactory(factory.Factory):
    class Meta:
        model = MemberDTO

    member_id = factory.Faker("uuid4")
    immediate_superior_team_user_id = factory.Faker("uuid4")


class ProjectDTOFactory(factory.Factory):
    class Meta:
        model = ProjectDTO

    project_id = factory.Sequence(lambda n: 'project %s' % n)
    name = factory.Sequence(lambda n: 'name %s' % n)
    description = factory.Sequence(lambda n: 'description %s' % n)
    logo_url = "http://sample.com"


class ProjectWithDisplayIdDTOFactory(factory.Factory):
    class Meta:
        model = ProjectWithDisplayIdDTO

    project_id = factory.Sequence(lambda n: 'project %s' % n)
    display_id = factory.Sequence(lambda n: 'display_id %s' % n)
    name = factory.Sequence(lambda n: 'name %s' % n)
    description = factory.Sequence(lambda n: 'description %s' % n)
    logo_url = "http://sample.com"


class ProjectWithoutIdDTOFactory(factory.Factory):
    class Meta:
        model = ProjectWithoutIdDTO

    name = factory.Sequence(lambda n: 'name %s' % n)
    display_id = factory.Sequence(lambda n: 'display_id %s' % n)
    description = factory.Sequence(lambda n: 'description %s' % n)
    logo_url = "http://sample.com"


class SearchableDetailsDTOFactory(factory.Factory):
    class Meta:
        model = SearchableDetailsDTO

    search_type = factory.Iterator(
        [
            Searchable.CITY.value,
            Searchable.STATE.value,
            Searchable.COUNTRY.value,
            Searchable.USER.value
        ]
    )
    id = factory.sequence(lambda counter: counter)
    value = factory.sequence(lambda counter: "name{}".format(counter))


class MemberIdWithSubordinateMemberIdsDTOFactory(factory.Factory):
    class Meta:
        model = MemberIdWithSubordinateMemberIdsDTO

    member_id = factory.Faker("uuid4")
    subordinate_member_ids = factory.Iterator(
        [factory.Faker("uuid4"), factory.Faker("uuid4"),
         factory.Faker("uuid4")]
    )


class ProjectRoleDTOFactory(factory.Factory):
    class Meta:
        model = ProjectRoleDTO

    project_id = factory.Sequence(lambda n: 'project %s' % n)
    role_id = factory.sequence(lambda number: "ROLE_%s" % number)
    name = factory.sequence(lambda number: "role %s" % number)
    description = factory.Sequence(lambda n: 'role description %s' % n)


class RoleNameAndDescriptionDTOFactory(factory.Factory):
    class Meta:
        model = RoleNameAndDescriptionDTO

    name = factory.sequence(lambda number: "role %s" % number)
    description = factory.Sequence(lambda n: 'role description %s' % n)


class UserIdWithTokenDTOFactory(factory.Factory):
    class Meta:
        model = UserIdWithTokenDTO

    user_id = factory.Sequence(lambda n: 'user_id_%s' % n)
    token = factory.Sequence(lambda n: 'user_token_%s' % n)
