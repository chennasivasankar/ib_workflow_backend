import factory

from ib_iam.interactors.dtos.dtos import TeamMemberLevelDTO, AddUserDetailsDTO, \
    TeamMemberLevelIdWithMemberIdsDTO, ImmediateSuperiorUserIdWithUserIdsDTO, \
    CompleteUserProfileDTO, CompleteTeamMemberLevelsDetailsDTO, \
    UserIdWithRoleIdsDTO
from ib_iam.interactors.auth.update_user_password_interactor import \
    CurrentAndNewPasswordDTO
from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
from ib_iam.tests.factories.storage_dtos import MemberDTOFactory, \
    TeamMemberLevelDetailsDTOFactory, MemberIdWithSubordinateMemberIdsDTOFactory


class AddUserDetailsDTOFactory(factory.Factory):
    class Meta:
        model = AddUserDetailsDTO

    name = factory.Faker("name")
    email = factory.Faker("email")
    team_ids = factory.List(['team0', 'team1'])
    # role_ids = factory.List(['role0', 'role1'])
    company_id = factory.Faker("uuid")


class CurrentAndNewPasswordDTOFactory(factory.Factory):
    class Meta:
        model = CurrentAndNewPasswordDTO

    current_password = "p@ssword1"
    new_password = "p@ssword2"


class CompleteUserProfileDTOFactory(factory.Factory):
    class Meta:
        model = CompleteUserProfileDTO

    user_id = factory.sequence(lambda number: "user%s" % number)
    name = factory.sequence(lambda number: "name%s" % number)
    email = factory.LazyAttribute(lambda user: "%s@gmail.com" % user.name)
    profile_pic_url = "http://sample.com"
    cover_page_url = "http://sample.com"


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


class CompleteTeamMemberLevelsDetailsDTOFactory(factory.Factory):
    class Meta:
        model = CompleteTeamMemberLevelsDetailsDTO

    member_dtos = factory.List(
        [factory.SubFactory(MemberDTOFactory),
         factory.SubFactory(MemberDTOFactory)]
    )
    user_profile_dtos = factory.List(
        [factory.SubFactory(UserProfileDTOFactory),
         factory.SubFactory(UserProfileDTOFactory)]
    )
    team_member_level_details_dtos = factory.List(
        [factory.SubFactory(TeamMemberLevelDetailsDTOFactory),
         factory.SubFactory(TeamMemberLevelDetailsDTOFactory)]
    )
    team_member_level_id_with_member_ids_dtos = factory.List(
        [factory.SubFactory(TeamMemberLevelIdWithMemberIdsDTOFactory),
         factory.SubFactory(TeamMemberLevelIdWithMemberIdsDTOFactory)]
    )
    member_id_with_subordinate_member_ids_dtos = factory.List(
        [factory.SubFactory(MemberIdWithSubordinateMemberIdsDTOFactory),
         factory.SubFactory(MemberIdWithSubordinateMemberIdsDTOFactory)]
    )


class UserIdWithRoleIdsDTOFactory(factory.Factory):
    class Meta:
        model = UserIdWithRoleIdsDTO

    user_id = factory.Faker("uuid4")
    role_ids = factory.Iterator([
        "ROLE_1", "ROLE_2", "ROLE_3"
    ])
