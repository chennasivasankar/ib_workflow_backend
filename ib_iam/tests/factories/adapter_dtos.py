import factory

from ib_iam.adapters.auth_service import UserTokensDTO
from ib_iam.adapters.dtos import UserProfileDTO


class UserProfileDTOFactory(factory.Factory):
    class Meta:
        model = UserProfileDTO

    user_id = factory.sequence(lambda number: "user%s" % number)
    name = factory.sequence(lambda number: "name%s" % number)
    email = factory.LazyAttribute(lambda user: "%s@gmail.com" % user.name)
    profile_pic_url = factory.sequence(lambda n: "url%d" % n)
    is_email_verify = False


class UserTokensDTOFactory(factory.Factory):
    class Meta:
        model = UserTokensDTO

    access_token = factory.sequence(lambda n: "access_token_%s" % n)
    refresh_token = factory.sequence(lambda n: "refresh_token_token_%s" % n)
    expires_in_seconds = 10000000000
    user_id = factory.Faker("uuid4")
