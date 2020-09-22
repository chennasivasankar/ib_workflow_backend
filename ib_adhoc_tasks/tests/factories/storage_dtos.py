import factory

from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupByDetailsDTO, GroupDetailsDTO


class GroupByDetailsDTOFactory(factory.Factory):
    class Meta:
        model = GroupByDetailsDTO

    group_by = factory.Iterator(["Stage", "Assignee", "field_id"])
    order = factory.Sequence(lambda counter: counter)


class GroupDetailsDTOFactory(factory.Factory):
    class Meta:
        model = GroupDetailsDTO

    task_ids = factory.Sequence(lambda counter: "task_{}".format(counter))
    total_tasks = factory.Sequence(lambda counter: counter)
    group_by_value = factory.Sequence(
        lambda counter: "value_{}".format(counter))
    group_by_display_name = factory.Sequence(
        lambda counter: "display_name_{}".format(counter))
    child_group_by_value = factory.Sequence(
        lambda counter: "value_{}".format(counter))
    child_group_by_display_name = factory.Sequence(
        lambda counter: "display_name_{}".format(counter))
