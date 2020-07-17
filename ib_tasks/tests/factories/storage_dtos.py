import factory
from ib_tasks.interactors.storage_interfaces.dtos import (
    CompleteGoFDetailsDTO, GoFDTO, GoFRolesDTO,
    GoFFieldsDTO, FieldDTO, FieldRolesDTO, FieldRoleDTO
)
from ib_tasks.constants.enum import FieldTypes, PermissionTypes


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


class FieldDTOFactory(factory.Factory):
    class Meta:
        model = FieldDTO

    gof_id = "FIN_VENDOR_BASIC_DETAILS"
    field_id = factory.Sequence(lambda n: 'field%d' % n)
    field_display_name = "field name"
    field_type = FieldTypes.DROPDOWN.value
    field_values = '["Mr", "Mrs", "Ms"]'
    required = True
    help_text = None
    tool_tip = None
    placeholder_text = None
    error_message = None
    allowed_formats = None
    validation_regex = None


class FieldRolesDTOFactory(factory.Factory):
    class Meta:
        model = FieldRolesDTO

    field_id = factory.Sequence(lambda n: 'field%d' % n)
    read_permission_roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"]
    write_permission_roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"]


class FieldRoleDTOFactory(factory.Factory):
    class Meta:
        model = FieldRoleDTO

    field_id = factory.Sequence(lambda n: 'field%d' % n)
    role = "FIN_PAYMENT_REQUESTER"
    permission_type = PermissionTypes.READ.value
