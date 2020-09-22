import factory

from ib_adhoc_tasks.constants.enum import ViewType
from ib_adhoc_tasks.models import GroupByInfo


class GroupByInfoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GroupByInfo

    user_id = factory.sequence(lambda number: "user%s" % number)
    group_by = factory.Iterator([
        "ASSIGNEE", "STAGE"
    ])
    order = factory.Iterator([1, 2])
    view_type = factory.Iterator([
        ViewType.LIST.value, ViewType.KANBAN.value
    ])
