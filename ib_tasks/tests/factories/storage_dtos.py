import factory
from ib_tasks.interactors.storage_interfaces.dtos import GOFDTO


class GoFDTOFactory(factory.Factory):
    class Meta:
        model = GOFDTO

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
    read_permission_roles = ['ALL_ROLES']
    write_permission_roles = ['ALL_ROLES']
    field_ids = ['FIN_PAYMENT_REQUESTOR']
