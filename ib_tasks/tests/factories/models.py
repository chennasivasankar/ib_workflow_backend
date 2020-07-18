import factory

from ib_tasks.models import (
    Stage, ActionPermittedRoles, StageAction, TaskStatusVariable,
    TaskTemplateGlobalConstants, TaskTemplate)


class TaskTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskTemplate

    template_id = factory.Sequence(lambda n: "template%d" % n)
    name = factory.Sequence(lambda n: "name_%d" % n)


class StageModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Stage

    stage_id = factory.Sequence(lambda n: "stage_id_%d" % n)
    display_name = factory.Sequence(lambda n: "name_%d" % n)
    value = factory.Iterator([-1, 0, 1, 2, 3, 4, 5, 6])
    display_logic = factory.Sequence(lambda n: "status_id_%d==stage_id_%d" % n)


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

    task_template_id = factory.SubFactory()
    variable = factory.Sequence(lambda n: "variable%d" % n)
    value = factory.Sequence(lambda n: "value%d" % n)
    data_type = factory.Sequence(lambda n: "data_type_%d" % n)
