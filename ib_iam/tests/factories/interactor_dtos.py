import factory

from ib_iam.interactors.dtos.dtos import \
    UserWithTeamIdsANDRoleIdsAndCompanyIdsDTO
from ib_iam.interactors.update_user_password_interactor import \
    CurrentAndNewPasswordDTO


class UserDetailsWithTeamRoleAndCompanyIdsDTOFactory(factory.Factory):
    class Meta:
        model = UserWithTeamIdsANDRoleIdsAndCompanyIdsDTO

    name = factory.Faker("name")
    email = factory.Faker("email")
    team_ids = factory.List(['team0', 'team1'])
    role_ids = factory.List(['role0', 'role1'])
    company_id = factory.Faker("uuid")


class CurrentAndNewPasswordDTOFactor(factory.Factory):
    class Meta:
        model = CurrentAndNewPasswordDTO

    current_password = "p@ssword1"
    new_password = "p@ssword2"
