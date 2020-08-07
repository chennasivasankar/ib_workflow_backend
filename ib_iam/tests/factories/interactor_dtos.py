import factory

from ib_iam.interactors.DTOs.common_dtos import \
    UserDetailsWithTeamRoleAndCompanyIdsDTO


class UserDetailsWithTeamRoleAndCompanyIdsDTOFactory(factory.Factory):
    class Meta:
        model = UserDetailsWithTeamRoleAndCompanyIdsDTO

    name = factory.Faker("name")
    email = factory.Faker("email")
    team_ids = factory.List(['team0', 'team1'])
    role_ids = factory.List(['role0', 'role1'])
    company_id = factory.Faker("uuid")
