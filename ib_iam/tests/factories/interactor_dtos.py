import factory

from ib_iam.interactors.dtos.dtos import \
    AddUserDetailsDTO, CompleteUserProfileDTO
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


class CompleteUserProfileDTOFactory(factory.Factory):
    class Meta:
        model = CompleteUserProfileDTO

    user_id = factory.sequence(lambda number: "user%s" % number)
    name = factory.sequence(lambda number: "name%s" % number)
    email = factory.LazyAttribute(lambda user: "%s@gmail.com" % user.name)
    profile_pic_url = factory.sequence(lambda n: "url%d" % n)
    cover_page_url = factory.sequence(lambda n: "url%d" % n)
