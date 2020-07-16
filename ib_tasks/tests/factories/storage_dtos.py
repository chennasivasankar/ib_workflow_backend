import factory

from ib_tasks.constants.enum import PermissionTypes
from ib_tasks.interactors.storage_interfaces.dtos import CompleteGoFDetailsDTO, \
    GoFDTO, GoFRolesDTO, GoFFieldsDTO, GoFRoleDTO, GoFFieldDTO


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


class GoFFieldsDTOFactory(factory.Factory):
    class Meta:
        model = GoFFieldsDTO

    gof_id = factory.Iterator(
        [
            'FIN_REQUEST_DETAILS', 'FIN_VENDOR_BASIC_DETAILS'
        ]
    )
    field_ids = ['FIN_PAYMENT_REQUESTOR', "FIN_PAYMENT_APPROVER"]


class CompleteGoFDetailsDTOFactory(factory.Factory):
    class Meta:
        model = CompleteGoFDetailsDTO

    gof_dto = GoFDTOFactory()
    gof_roles_dto = GoFRolesDTOFactory()
    gof_fields_dto = GoFFieldsDTOFactory()


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


class GoFFieldDTOFactory(factory.Factory):
    class Meta:
        model = GoFFieldDTO

    gof_id = factory.Iterator(
        [
            'FIN_REQUEST_DETAILS', 'FIN_VENDOR_BASIC_DETAILS'
        ]
    )
    field_id = factory.Iterator(
        ['FIN_PAYMENT_REQUESTOR', "FIN_PAYMENT_APPROVER"]
    )
