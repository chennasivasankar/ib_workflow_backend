import uuid

import factory

from ib_utility_tools.constants.enum import EntityType
from ib_utility_tools.models import Checklist, ChecklistItem


class ChecklistFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Checklist

    checklist_id = factory.LazyFunction(uuid.uuid4)
    entity_id = factory.sequence(lambda number: "entity%s" % number)
    entity_type = EntityType.TASK.value


class ChecklistItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ChecklistItem

    checklist_item_id = factory.LazyFunction(uuid.uuid4)
    checklist = factory.SubFactory(ChecklistFactory)
    text = factory.sequence(lambda number: "text%s" % number)
    is_checked = False
