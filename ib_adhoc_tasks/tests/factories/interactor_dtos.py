import factory

from ib_adhoc_tasks.interactors.dtos.dtos import GroupByDTO


class GroupByDTOFactory(factory.Factory):
    class Meta:
        model = GroupByDTO

    group_by_key = factory.Sequence(lambda n: "group_by_%s" % n)
    order = factory.Sequence(lambda n: n)
