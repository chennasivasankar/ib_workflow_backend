import factory
from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, GoFIdAndOrderDTO


class GoFIdAndOrderDTOFactory(factory.Factory):
    class Meta:
        model = GoFIdAndOrderDTO

    gof_id = factory.sequence(
        lambda n: "GoF_{}".format(n + 1)
    )
    order = factory.sequence(lambda n: n + 1)
