import factory
from ib_tasks.models.field import Field
from ib_tasks.models.field_role import FieldRole
from ib_tasks.models.gof import GoF
from ib_tasks.constants.enum import PermissionTypes, FieldTypes
from ib_tasks.models.task_template import TaskTemplate


class TaskTemplateFactory(factory.DjangoModelFactory):
    class Meta:
        model = TaskTemplate

    template_id = factory.Sequence(lambda n: "template%d" %n )
    name = factory.Iterator(
        ["Payment Request", "Vendor"]
    )


class GoFFactory(factory.DjangoModelFactory):
    class Meta:
        model = GoF

    gof_id = factory.Sequence(lambda n: "gof%d" %n )
    display_name = factory.Iterator(
        ["Request Details", "Vendor Type", "Vendor Basic Details"]
    )
    order = factory.Sequence(lambda counter: counter)
    task_template = factory.SubFactory(TaskTemplateFactory)
    max_columns = 2


class FieldFactory(factory.DjangoModelFactory):
    class Meta:
        model = Field

    gof = factory.SubFactory(GoFFactory)
    field_id = factory.Sequence(lambda n: "field%d" %n )
    display_name = factory.Iterator(
        "Saluation", "Type of Vendor"
    )
    field_type = FieldTypes.PLAIN_TEXT
    required = True

    class Params:
        optional = factory.Trait(
            field_values='["mr", "mrs"]'
        )


class FieldRoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = FieldRole

    field = factory.SubFactory(FieldFactory)
    role = factory.Iterator(
        ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_APPROVER"]
    )
    permission_type = PermissionTypes.READ.value
