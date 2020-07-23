import factory

from ib_iam.adapters.dtos import UserProfileDTO


class UserProfileDTOFactory(factory.Factory):
    class Meta:
        model = UserProfileDTO

    user_id = factory.sequence(lambda number: "user%s" % number)
    name = factory.sequence(lambda number: "name%s" % number)
    email = factory.LazyAttribute(lambda user: "%s@gmail.com" % user.name)
    profile_pic_url = factory.sequence(lambda n: "url%d" % n)