import factory

from ib_iam.models.role import Role


class RoleFactory(factory.Factory):
    class Meta:
        model = Role

    role_id = factory.Sequence(lambda n: 'PAYMENT%s' % n)
    role_name = factory.Sequence(lambda n: 'payment%s' % n)
    role_description = factory.Sequence(lambda n: 'payment_description%s' % n)