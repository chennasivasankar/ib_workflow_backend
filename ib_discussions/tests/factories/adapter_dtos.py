import factory

from ib_discussions.adapters.auth_service import UserProfileDTO


class UserProfileFactory(factory.Factory):
    class Meta:
        model = UserProfileDTO
    user_id = factory.Faker("uuid4")
    name = factory.LazyAttribute(
        lambda obj: "name of user_id is {user_id}".format(
            user_id=obj.user_id
        )
    )
    profile_pic_url = factory.LazyAttribute(
        lambda obj: "https://graph.ib_users.com/{user_id}/picture".format(
            user_id=obj.user_id
        )
    )