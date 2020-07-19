import factory, factory.django

from ib_iam.adapters.dtos import UserProfileDTO


class UserProfileDTOFactory(factory.Factory):
    class Meta:
        model = UserProfileDTO

    user_id = factory.sequence(lambda n: "user_id-%d" % n)
    name = factory.sequence(lambda n: "user%d" % n)
    profile_pic_url = factory.sequence(lambda n: "url%d" % n)

