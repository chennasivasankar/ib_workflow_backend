import factory

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
