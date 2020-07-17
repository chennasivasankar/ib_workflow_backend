import factory
from ib_tasks.models.task_template import TaskTemplate
from ib_tasks.models.gof import GoF


class TaskTemplateFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TaskTemplate

    template_id = factory.sequence(lambda n: "template_{}".format(n + 1))
    name = factory.sequence(lambda n: "Template {}".format(n + 1))


class GoFFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GoF
    gof_id = factory.sequence(lambda n: "gof_{}".format(n + 1))
    display_name = factory.sequence(lambda n: "GoF {}".format(n + 1))
    task_template = factory.SubFactory(TaskTemplateFactory)
    order = factory.sequence(lambda n: (n + 1))
    max_columns = 2
