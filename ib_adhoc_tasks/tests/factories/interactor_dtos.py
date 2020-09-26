import factory

from ib_adhoc_tasks.constants.enum import GroupByKey, ViewType
from ib_adhoc_tasks.interactors.dtos.dtos import GroupByDTO, \
    TaskOffsetAndLimitValuesDTO, TaskIdsForGroupsParameterDTO, GroupByValueDTO, \
    OffsetLimitDTO, GroupByInfoKanbanViewDTO, GroupByInfoListViewDTO, \
    GetSubtasksParameterDTO, GetTaskDetailsInGroupInputDTO, \
    GetChildGroupsInGroupInputDTO, GroupByParameter, GroupBYKeyDTO


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


class GroupBYKeyDTOFactory(factory.Factory):
    class Meta:
        model = GroupBYKeyDTO

    group_by_key = factory.Iterator(["ASSIGNEE", "STAGE"])
    order = factory.Iterator([1, 2])


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

    key = factory.Iterator([GroupByKey.STAGE.value,
                            GroupByKey.ASSIGNEE.value,
                            "field_id_1"])
    value = factory.Iterator(["stage_id_1", "assignee_id_1", "field_value_1"])


class OffsetLimitDTOFactory(factory.Factory):
    class Meta:
        model = OffsetLimitDTO

    offset = factory.sequence(lambda counter: counter)
    limit = factory.sequence(lambda counter: counter + 1)


class GroupByInfoKanbanViewDTOFactory(factory.Factory):
    class Meta:
        model = GroupByInfoKanbanViewDTO

    project_id = factory.sequence(lambda counter: "project_{}".format(counter))
    user_id = factory.sequence((lambda counter: "user_{}".format(counter)))
    group_by_details = GroupBYKeyDTOFactory.create_batch(2)

    @factory.lazy_attribute
    def task_offset_limit_dto(self):
        return OffsetLimitDTOFactory()

    @factory.lazy_attribute
    def group1_offset_limit_dto(self):
        return OffsetLimitDTOFactory()

    @factory.lazy_attribute
    def group2_offset_limit_dto(self):
        return OffsetLimitDTOFactory()


class GroupByInfoListViewDTOFactory(factory.Factory):
    class Meta:
        model = GroupByInfoListViewDTO

    project_id = factory.sequence(lambda counter: "project_{}".format(counter))
    user_id = factory.sequence((lambda counter: "user_{}".format(counter)))
    group_by_key = factory.Sequence(lambda counter: "group_by_key_{}".format(counter))

    @factory.lazy_attribute
    def task_offset_limit_dto(self):
        return OffsetLimitDTOFactory()

    @factory.lazy_attribute
    def group_offset_limit_dto(self):
        return OffsetLimitDTOFactory()


class GetTaskDetailsInGroupInputDTOFactory(factory.Factory):
    class Meta:
        model = GetTaskDetailsInGroupInputDTO

    project_id = factory.Sequence(lambda n: "project_id_%d" % n)
    view_type = factory.Iterator([ViewType.LIST.value, ViewType.KANBAN.value])
    limit = 5
    offset = 0
    group_by_values = factory.Iterator(
        ["GROUP_BY_VALUE_1", "GROUP_BY_VALUE_1"]
    )
    user_id = factory.sequence((lambda counter: "user_{}".format(counter)))


class GetSubtasksParameterDTOFactory(factory.Factory):
    class Meta:
        model = GetSubtasksParameterDTO

    user_id = factory.Sequence(lambda n: "user_id_%d" % n)
    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
    view_type = factory.Iterator(["LIST", "KANBAN"])


class GetChildGroupsInGroupInputDTOFactory(factory.Factory):
    class Meta:
        model = GetChildGroupsInGroupInputDTO

    user_id = factory.Sequence(lambda n: "user_id_%d" % n)
    project_id = factory.Sequence(lambda n: "project_id_%d" % n)
    limit = 5
    offset = 0
    group_limit = 5
    group_offset = 0
    group_by_value = factory.Iterator(["GROUP_BY_VALUE_1", "GROUP_BY_VALUE_1"])


class GroupByParameterFactory(factory.Factory):
    class Meta:
        model = GroupByParameter

    project_id = factory.Sequence(lambda n: "project_id_%d" % n)
    user_id = factory.Sequence(lambda n: "user_id_%d" % n)
    view_type = factory.Iterator(["LIST", "KANBAN"])

