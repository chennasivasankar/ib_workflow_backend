import factory

from ib_iam.adapters.dtos import UserDTO


class UserDTOFactory(factory.Factory):
    class Meta:
        model = UserDTO

    user_id = factory.sequence(lambda number: "user%s" % number)
    name = factory.sequence(lambda number: "name%s" % number)
    email = factory.LazyAttribute(lambda user: "%s@gmail.com" % user.name)
