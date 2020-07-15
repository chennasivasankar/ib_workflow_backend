import factory
from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, GoFIDAndOrderDTO


class GoFIDAndOrderDTOFactory(factory.Factory):
    class Meta:
        model = GoFIDAndOrderDTO

    gof_id = factory.sequence(
        lambda n: "GoF_{}".format(n + 1)
    )
    order = factory.sequence(lambda n: n + 1)
