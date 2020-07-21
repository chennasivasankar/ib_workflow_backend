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
