import factory

from ib_adhoc_tasks.constants.enum import GroupByType
from ib_adhoc_tasks.interactors.dtos import GroupByValueDTO, \
    TaskIdsForGroupsParameterDTO


class TaskIdsForGroupsParameterDTOFactory(factory.Factory):
    class Meta:
        model = TaskIdsForGroupsParameterDTO

    project_id = factory.Sequence(lambda n: "project_id_%d" % n)
    template_id = factory.Sequence(lambda n: "template_%d" % n)
    user_id = factory.Sequence(lambda n: "user_id_%d" % n)
    groupby_value_dtos = []
    limit = 5
    offset = 0


class GroupByValueDTOFactory(factory.Factory):
    class Meta:
        model = GroupByValueDTO

    key = factory.Iterator([GroupByType.STAGE.value,
                            GroupByType.ASSIGNEE.value,
                            "field_id_1"])
    value = factory.Iterator(["stage_id_1", "assignee_id_1", "field_value_1"])
