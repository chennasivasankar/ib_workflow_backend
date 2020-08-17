import factory

from ib_iam.interactors.dtos.dtos import TeamMemberLevelDTO, AddUserDetailsDTO, \
    TeamMemberLevelIdWithMemberIdsDTO, ImmediateSuperiorUserIdWithUserIdsDTO
from ib_iam.interactors.update_user_password_interactor import \
    CurrentAndNewPasswordDTO


class AddUserDetailsDTOFactory(factory.Factory):
    class Meta:
        model = AddUserDetailsDTO

    name = factory.Faker("name")
    email = factory.Faker("email")
    team_ids = factory.List(['team0', 'team1'])
    role_ids = factory.List(['role0', 'role1'])
    company_id = factory.Faker("uuid")


class CurrentAndNewPasswordDTOFactory(factory.Factory):
    class Meta:
        model = CurrentAndNewPasswordDTO

    current_password = "p@ssword1"
    new_password = "p@ssword2"


class TeamMemberLevelDTOFactory(factory.Factory):
    class Meta:
        model = TeamMemberLevelDTO

    team_member_level_name = factory.Faker("name")
    level_hierarchy = factory.Iterator([1, 2, 3, 4, 5, 6, 7, 8, 9])


class TeamMemberLevelIdWithMemberIdsDTOFactory(factory.Factory):
    class Meta:
        model = TeamMemberLevelIdWithMemberIdsDTO

    team_member_level_id = factory.Faker("uuid4")
    member_ids = factory.List(
        [factory.Faker("uuid4"), factory.Faker("uuid4"), factory.Faker("uuid4")]
    )


class ImmediateSuperiorUserIdWithUserIdsDTOFactory(factory.Factory):
    class Meta:
        model = ImmediateSuperiorUserIdWithUserIdsDTO

    immediate_superior_user_id = factory.Faker("uuid4")
    member_ids = factory.List(
        [factory.Faker("uuid4"), factory.Faker("uuid4"), factory.Faker("uuid4")]
    )
