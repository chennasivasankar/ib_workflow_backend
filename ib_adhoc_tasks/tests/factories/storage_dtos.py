import factory
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupByDetailsDTO, GroupDetailsDTO

from ib_adhoc_tasks.constants.enum import ViewType
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupByResponseDTO, AddOrEditGroupByParameterDTO


class GroupByResponseDTOFactory(factory.Factory):
    class Meta:
        model = GroupByResponseDTO

    group_by_id = factory.sequence(lambda number: number)
    group_by_display_name = factory.Iterator([
        "ASSIGNEE", "STAGE"
    ])
    order = factory.Iterator([1, 2])


class AddOrEditGroupByParameterDTOFactory(factory.Factory):
    class Meta:
        model = AddOrEditGroupByParameterDTO

    project_id = factory.sequence(lambda number: "project_id_%s" % number)
    user_id = factory.sequence(lambda number: "user_id_%s" % number)
    view_type = factory.Iterator([
        ViewType.LIST.value, ViewType.KANBAN.value
    ])
    group_by_display_name = factory.Iterator([
        "ASSIGNEE", "STAGE"
    ])
    order = factory.Iterator([1, 2])
    group_by_id = factory.sequence(lambda number: number)


class GroupByDetailsDTOFactory(factory.Factory):
    class Meta:
        model = GroupByDetailsDTO

    group_by = factory.Iterator(["Stage", "Assignee", "field_id"])
    order = factory.Sequence(lambda counter: counter)


class GroupDetailsDTOFactory(factory.Factory):
    class Meta:
        model = GroupDetailsDTO

    task_ids = factory.Iterator(
        [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9],
         [10, 11, 12, 13, 14]])
    total_tasks = factory.Sequence(lambda counter: counter)
    group_by_value = factory.Sequence(
        lambda counter: "value_{}".format(counter))
    group_by_display_name = factory.Sequence(
        lambda counter: "display_name_{}".format(counter))
    child_group_by_value = factory.Sequence(
        lambda counter: "value_{}".format(counter))
    child_group_by_display_name = factory.Sequence(
        lambda counter: "display_name_{}".format(counter))
