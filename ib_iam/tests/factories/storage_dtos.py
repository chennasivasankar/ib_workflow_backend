import factory
from ib_iam.interactors.storage_interfaces.dtos import RoleDto

class RoleDTOFactory(factory.Factory):
    class Meta:
        model = RoleDto
    role_id = factory.Sequence(lambda n: 'PAYMENT%s' % n)
    role_name = factory.Sequence(lambda n: 'payment%s' % n)
    role_description = factory.Sequence(lambda n: 'payment_description%s' % n)