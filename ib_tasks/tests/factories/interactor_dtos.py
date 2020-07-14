import factory
from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, GoFDTO


class GoFDTOFactory(factory.Factory):
    class Meta:
        model = GoFDTO

    gof_id = factory.sequence(
        lambda n: "GOF_{}".format(n + 1)
    )
    order = factory.sequence(lambda n: n + 1)
