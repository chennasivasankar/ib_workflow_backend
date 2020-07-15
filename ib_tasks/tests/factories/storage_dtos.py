import factory
from ib_tasks.interactors.storage_interfaces.dtos import GoFCompleteDetailsDTO, \
    GoFDTO, GoFRolesDTO


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

    read_permission_roles = ['ALL_ROLES']
    write_permission_roles = ['ALL_ROLES']


class GoFCompleteDetailsDTOFactory(factory.Factory):
    class Meta:
        model = GoFCompleteDetailsDTO
    field_ids = ['FIN_PAYMENT_REQUESTOR']
