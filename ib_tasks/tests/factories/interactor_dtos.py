import factory
from ib_tasks.interactors.dtos import FieldDTO
from ib_tasks.constants.enum import FieldTypes


class FieldDTOFactory(factory.Factory):
    class Meta:
        model = FieldDTO

    gof_id = "FIN_VENDOR_BASIC_DETAILS"
    field_id = factory.Sequence(lambda n: 'field%d' % n)
    field_display_name = "field name"
    field_type = "DROPDOWN"
    field_values = ["Mr", "Mrs", "Ms"]
    required = True
    read_permissions_to_roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"]
    write_permissions_to_roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"]
    help_text = "Verify the code"
    tool_tip = "Request"
    placeholder_text = "select vendor"
    error_message = "error message"
    allowed_formats = None
    validation_regex = None
