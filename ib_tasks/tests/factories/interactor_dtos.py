import factory
from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, GroupOfFieldsDTO


class GroupOfFieldsDTOFactory(factory.Factory):
    class Meta:
        model = GroupOfFieldsDTO

    group_of_fields_id = factory.sequence(
        lambda n: "GOF_{}".format(n + 1)
    )
    order = factory.sequence(lambda n: n + 1)
