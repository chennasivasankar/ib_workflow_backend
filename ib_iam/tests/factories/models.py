import factory

from ib_iam.models import UserDetails


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserDetails

    user_id = factory.sequence(lambda n: n)
    is_admin = factory.Iterator([True, False])
