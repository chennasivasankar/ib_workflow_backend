import factory

from ib_tasks.constants.enum import FieldTypes
from ib_tasks.models.gof import GoF
from ib_tasks.models.task_template import TaskTemplate
from ib_tasks.models.field import Field


class TaskTemplateFactory(factory.DjangoModelFactory):
    class Meta:
        model = TaskTemplate

    template_id = factory.Iterator(
        [
            "FIN_PR", "FIN_VENDOR"
        ]
    )
    name = factory.Iterator(
        [
            "Payment Request", "Vendor"
        ]
    )


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
