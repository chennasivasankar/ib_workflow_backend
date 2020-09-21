import factory


class GroupByResponseDTOFactory(factory.Factory):
    group_by_id = factory.sequence(lambda number: number)
    group_by_display_name = factory.Iterator([
        "ASSIGNEE", "STAGE"
    ])
    order = factory.Iterator([1, 2])
