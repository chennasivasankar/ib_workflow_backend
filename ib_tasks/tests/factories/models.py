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

    stage = factory.SubFactory(StageModelFactory)
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
from ib_tasks.models.global_constant import GlobalConstant


class TaskTemplateFactory(factory.DjangoModelFactory):
    class Meta:
        model = TaskTemplate

    template_id = factory.Sequence(
        lambda counter: "TEMPLATE_ID-{}".format(counter)
    )
    name = factory.Sequence(lambda counter: "TEMPLATE_NAME-{}".format(counter))


class GoFFactory(factory.DjangoModelFactory):
    class Meta:
        model = GoF

    gof_id = factory.Sequence(lambda counter: "GOF_ID-{}".format(counter))
    display_name = factory.Sequence(
        lambda counter: "GOF_DISPLAY_NAME-{}".format(counter)
    )
    max_columns = 2


class FieldFactory(factory.DjangoModelFactory):
    class Meta:
        model = Field

    field_id = factory.Sequence(lambda counter: "FIELD_ID-{}".format(counter))
    display_name = factory.Sequence(
        lambda counter: "DISPLAY_NAME-{}".format(counter)
    )
    field_type = factory.Sequence(
        lambda counter: "FIELD_TYPE-{}".format(counter)
    )


class GoFRoleFactory(factory.DjangoModelFactory):
    class Meta:
        model = GoFRole

    gof = factory.SubFactory(GoFFactory)
    role = factory.Sequence(lambda counter: "ROLE-{}".format(counter))
    permission_type = PermissionTypes.READ.value


class GlobalConstantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GlobalConstant

    name = factory.sequence(lambda n: "constant_{}".format(n + 1))
    value = factory.sequence(lambda n: (n + 1))
    task_template = factory.SubFactory(TaskTemplateFactory)
