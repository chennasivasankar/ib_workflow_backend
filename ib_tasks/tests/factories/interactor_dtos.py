import factory
from ib_tasks.interactors.dtos.dtos import FieldDTO
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
    read_permissions_to_roles = ["FIN_PAYMENTS_RP", "FIN_PAYMENTS_LEVEL1_VERIFIER"]
    write_permissions_to_roles = ["FIN_PAYMENTS_RP"]
    help_text = "Verify the code"
    tool_tip = "Request"
    placeholder_text = "select vendor"
    error_message = "error message"
