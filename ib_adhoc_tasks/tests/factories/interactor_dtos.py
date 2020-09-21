import factory

from ib_adhoc_tasks.interactors.dtos.dtos import GroupByDTO, \
    TaskOffsetAndLimitValuesDTO


class GroupByDTOFactory(factory.Factory):
    class Meta:
        model = GroupByDTO

    group_by_value = factory.Sequence(lambda n: "group_by_%s" % n)
    order = factory.Sequence(lambda n: n)
    limit = 5
    offset = 0


class TaskOffsetAndLimitValuesDTOFactory(factory.Factory):
    class Meta:
        model = TaskOffsetAndLimitValuesDTO

    limit = 5
    offset = 0
