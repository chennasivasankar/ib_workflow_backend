import factory
from ib_tasks.interactors.dtos import GlobalConstantsDTO, GoFIdAndOrderDTO


class GoFIdAndOrderDTOFactory(factory.Factory):
    class Meta:
        model = GoFIdAndOrderDTO

    gof_id = factory.sequence(
        lambda n: "GoF_{}".format(n + 1)
    )
    order = factory.sequence(lambda n: n + 1)


class GlobalConstantsDTOFactory(factory.Factory):
    class Meta:
        model = GlobalConstantsDTO

    constant_name = factory.sequence(lambda n: "Constant_{}".format(n + 1))
    value = factory.sequence(lambda n: n)
