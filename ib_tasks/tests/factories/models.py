import factory

from ib_tasks.constants.enum import FieldTypes, PermissionTypes
from ib_tasks.models.gof import GoF
from ib_tasks.models.task_template import TaskTemplate
from ib_tasks.models.field import Field
from ib_tasks.models.gof_role import GoFRole
from ib_tasks.models import (
    Stage, ActionPermittedRoles, StageAction, TaskStatusVariable,
    TaskTemplateGlobalConstants)


class StageModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Stage

    stage_id = factory.Sequence(lambda n: "stage_id_%d" % n)
    display_name = factory.Sequence(lambda n: "name_%d" % n)
    task_template_id = factory.Sequence(lambda n: "task_template_id_%d" % n)
    value = factory.Sequence(lambda n: n)
    display_logic = factory.Sequence(lambda n: "status_id_%d==stage_id" % n)


class StageActionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = StageAction

    stage_id = factory.SubFactory(StageModelFactory)
    name = factory.Sequence(lambda n: "name_%d" % n)
    button_text = "hey"
    button_color = "#fafafa"
    logic = "Status1 = PR_PAYMENT_REQUEST_DRAFTS"
    py_function_import_path = "path"


class ActionPermittedRolesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ActionPermittedRoles

    action_id = factory.SubFactory(StageActionFactory)
    role_id = factory.Sequence(lambda n: "role_%d" % n)


class TaskStatusVariableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskStatusVariable

    task_id = factory.Sequence(lambda n: n)
    variable = factory.Sequence(lambda n: "variable%d" % n)
    value = factory.Sequence(lambda n: n)


class TaskTemplateGlobalConstantsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskTemplateGlobalConstants

    task_template_id = factory.Sequence(lambda n: n)
    variable = factory.Sequence(lambda n: "variable%d" % n)
    value = factory.Sequence(lambda n: "value%d" % n)
    data_type = factory.Sequence(lambda n: "data_type_%d" % n)


class TaskTemplateFactory(factory.DjangoModelFactory):
    class Meta:
        model = TaskTemplate

    template_id = factory.Sequence(lambda n: "task_template_id_%d" % n)
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


class GoFRoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = GoFRole

    gof = factory.SubFactory(GoFFactory)
    role = factory.Iterator(
        ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_APPROVER"]
    )
    permission_type = PermissionTypes.READ.value
