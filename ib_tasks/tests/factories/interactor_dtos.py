import factory
from ib_tasks.interactors.dtos import GlobalConstantsDTO, \
    GoFsWithTemplateIdDTO, GoFWithOrderAndAddAnotherDTO


class GlobalConstantsDTOFactory(factory.Factory):
    class Meta:
        model = GlobalConstantsDTO

    constant_name = factory.sequence(lambda n: "Constant_{}".format(n + 1))
    value = factory.sequence(lambda n: n)


class GoFWithOrderAndAddAnotherDTOFactory(factory.Factory):
    class Meta:
        model = GoFWithOrderAndAddAnotherDTO

    gof_id = factory.sequence(lambda n: "gof_{}".format(n + 1))
    order = factory.sequence(lambda n: n)
    enable_add_another_gof = factory.Iterator([True, False])


class GoFsWithTemplateIdDTOFactory(factory.Factory):
    class Meta:
        model = GoFsWithTemplateIdDTO

    template_id = factory.sequence(lambda n: "template_{}".format(n + 1))
    gof_dtos = factory.SubFactory(GoFWithOrderAndAddAnotherDTOFactory)
