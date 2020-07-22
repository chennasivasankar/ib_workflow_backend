import factory

from ib_iam.models import Role


class RoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Role

    role_id = factory.Sequence(lambda n: 'PAYMENT%s' % n)
    name = factory.Sequence(lambda n: 'payment%s' % n)
    description = factory.Sequence(lambda n: 'payment_description%s' % n)
