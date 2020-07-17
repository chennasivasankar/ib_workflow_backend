import factory
from ib_tasks.models.field import Field
from ib_tasks.models.field_role import FieldRole
from ib_tasks.models.gof import GoF
from ib_tasks.constants.enum import PermissionTypes, FieldTypes


class GoFFactory(factory.DjangoModelFactory):
    class Meta:
        model = GoF

    gof_id = factory.Iterator(
        "FIN_REQUEST_DETAILS", "FIN_GOF_VENDOR_TYPE",
    )
    order = factory.Sequence(lambda counter: counter)
    #task_template = factory.SubFactory(TaskTemplateFactory)


class FieldFactory(factory.DjangoModelFactory):
    class Meta:
        model = Field

    gof = factory.SubFactory(GoFFactory)
    field_id = factory.Iterator(
        ["FIN_PAYMENT_REQUESTOR", "FIN_TYPE_OF_VENDOR"]
    )
    display_name = factory.Iterator(
        "Saluation", "Type of Vendor"
    )
    field_type = FieldTypes.PLAIN_TEXT
    required = True

    # allowed_formats = None
    # help_text = None
    # tooltip = None
    # placeholder_text = None
    # error_messages = None
    # validation_regex = None
    class Params:
        optional = factory.Trait(
            field_values=["mr", "mrs"],

        )


class FieldRoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = FieldRole

    field_id = factory.SubFactory(FieldFactory)
    role = factory.Iterator(
        ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_APPROVER"]
    )
    permission_type = PermissionTypes.READ.value
