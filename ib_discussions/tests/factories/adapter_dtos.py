import factory

from ib_discussions.adapters.auth_service import UserProfileDTO


class UserProfileDTOFactory(factory.Factory):
    class Meta:
        model = UserProfileDTO
    user_id = factory.Faker("uuid4")
    name = factory.LazyAttribute(lambda obj: "name")
    profile_pic_url = 'https://graph.ib_users.com/'
