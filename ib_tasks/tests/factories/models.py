import factory

from ib_tasks.constants.enum import FieldTypes, PermissionTypes
from ib_tasks.models.gof import GoF
from ib_tasks.models.task_template import TaskTemplate
from ib_tasks.models.field import Field
from ib_tasks.models.gof_role import GoFRole
from ib_tasks.models.global_constant import GlobalConstant


class TaskTemplateFactory(factory.DjangoModelFactory):
    class Meta:
        model = TaskTemplate

    template_id = factory.sequence(lambda n: "template_{}".format(n + 1))
    name = factory.sequence(lambda n: "Template {}".format(n + 1))


class GoFFactory(factory.DjangoModelFactory):
    class Meta:
        model = GoF

    gof_id = factory.Iterator(
        [
            "FIN_REQUEST_DETAILS", "FIN_GOF_VENDOR_TYPE",
            "FIN_VENDOR_BASIC_DETAILS"
        ]
    )
    display_name = factory.Iterator(
        [
            "Request Details", "Vendor Type", "Vendor Basic Details"
        ]
    )
    task_template = factory.SubFactory(TaskTemplateFactory)
    order = factory.Sequence(lambda counter: counter)
    max_columns = 2


class FieldFactory(factory.DjangoModelFactory):
    class Meta:
        model = Field

    field_id = factory.Iterator(
        ["FIN_PAYMENT_REQUESTOR", "FIN_TYPE_OF_VENDOR"]
    )
    display_name = factory.Iterator(
        ["Payment Requester", "Type of Vendor"]
    )
    field_type = factory.Iterator(
        [FieldTypes.PLAIN_TEXT, FieldTypes.GOF_SELECTOR]
    )


class GoFRoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = GoFRole

    gof = factory.SubFactory(GoFFactory)
    role = factory.Iterator(
        ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_APPROVER"]
    )
    permission_type = PermissionTypes.READ.value


class GlobalConstantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GlobalConstant

    name = factory.sequence(lambda n: "constant_{}".format(n + 1))
    value = factory.sequence(lambda n: (n + 1))
    task_template = factory.SubFactory(TaskTemplateFactory)
