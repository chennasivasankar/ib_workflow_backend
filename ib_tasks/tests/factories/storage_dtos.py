import factory

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.storage_interfaces.dtos import (
    CompleteGoFDetailsDTO, GoFDTO, GoFRolesDTO, GoFRoleDTO
)


class GoFDTOFactory(factory.Factory):
    class Meta:
        model = GoFDTO

    gof_id = factory.Sequence(lambda counter: "GOF_ID-{}".format(counter))
    gof_display_name = factory.Sequence(
        lambda counter: "GOF_DISPLAY_NAME-{}".format(counter)
    )
    max_columns = 2


class GoFRolesDTOFactory(factory.Factory):
    class Meta:
        model = GoFRolesDTO

    gof_id = factory.Sequence(lambda counter: "GOF_ID-{}".format(counter))
    read_permission_roles = ['ALL_ROLES']
    write_permission_roles = ['ALL_ROLES']


class CompleteGoFDetailsDTOFactory(factory.Factory):
    class Meta:
        model = CompleteGoFDetailsDTO

    gof_dto = GoFDTOFactory()
    gof_roles_dto = GoFRolesDTOFactory()


class GoFRoleDTOFactory(factory.Factory):
    class Meta:
        model = GoFRoleDTO

    gof_id = factory.Sequence(lambda counter: "GOF_ID-{}".format(counter))
    role = factory.Sequence(lambda counter: "ROLE-{}".format(counter))
    permission_type = PermissionTypes.READ.value

