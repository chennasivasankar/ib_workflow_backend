import factory

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.storage_interfaces.dtos import (
    CompleteGoFDetailsDTO, GoFDTO, GoFRolesDTO, GoFRoleDTO
)


class GoFDTOFactory(factory.Factory):
    class Meta:
        model = GoFDTO

    gof_id = factory.Iterator(
        [
            'FIN_REQUEST_DETAILS', 'FIN_VENDOR_BASIC_DETAILS'
        ]
    )
    gof_display_name = factory.Iterator(
        [
            'Request Details', 'Vendor Basic Details'
        ]
    )
    task_template_id = factory.Iterator(
        [
            "FIN_PR", "FIN_VENDOR"
        ]
    )
    order = factory.Sequence(lambda counter: counter)
    max_columns = 2
    enable_multiple_gofs = False


class GoFRolesDTOFactory(factory.Factory):
    class Meta:
        model = GoFRolesDTO

    gof_id = factory.Iterator(
        [
            'FIN_REQUEST_DETAILS', 'FIN_VENDOR_BASIC_DETAILS'
        ]
    )
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

    gof_id = factory.Iterator(
        [
            'FIN_REQUEST_DETAILS', 'FIN_VENDOR_BASIC_DETAILS'
        ]
    )
    role = factory.Iterator(
        [
            "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_APPROVER"
        ]
    )
    permission_type = PermissionTypes.READ.value

