import factory

from ib_iam.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    user_id = factory.sequence(lambda n: n)
    is_admin = factory.Iterator([True, False])
