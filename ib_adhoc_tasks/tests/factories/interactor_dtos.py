import factory

from ib_adhoc_tasks.constants.enum import GroupByType
from ib_adhoc_tasks.interactors.dtos import GroupByDTO, ApplyGroupByDTO


class ApplyGroupByDTOFactory(factory.Factory):
    class Meta:
        model = ApplyGroupByDTO

    project_id = factory.Sequence(lambda n: "project_id_%d" % n)
    template_id = factory.Sequence(lambda n: "template_%d" % n)
    user_id = factory.Sequence(lambda n: "user_id_%d" % n)
    groupby_dtos = []
    limit = 5
    offset = 0


class GroupByDTOFactory(factory.Factory):
    class Meta:
        model = GroupByDTO

    key = factory.Iterator([GroupByType.STAGE.value,
                            GroupByType.ASSIGNEE.value,
                            "field_id_1"])
    value = factory.Iterator(["stage_id_1", "assignee_id_1", "field_value_1"])
