import factory
from ib_tasks.interactors.dtos.dtos import FieldDTO
from ib_tasks.constants.enum import FieldTypes


class FieldDTOFactory(factory.Factory):
    class Meta:
        model = FieldDTO

    field_id = factory.Sequence(lambda n: 'field%d' % n)
    field_display_name = "field name"
    field_type = "DROPDOWN"
    field_values = ["Mr", "Mrs", "Ms"]
    required = True
    read_permissions_to_roles = ["admin", "user"]
    write_permissions_to_roles = ["admin"]
    help_text = "Verify the code"
    tool_tip = "Request"
    placeholder_text = "select vendor"
    error_message = "error message"
