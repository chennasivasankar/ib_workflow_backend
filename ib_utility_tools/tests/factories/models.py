import uuid
from datetime import datetime

import factory

from ib_utility_tools.constants.enum import EntityType, TimerEntityType
from ib_utility_tools.models import Checklist, ChecklistItem, Timer


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
    created_at = factory.LazyFunction(datetime.now)


class TimerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Timer

    timer_id = factory.LazyFunction(uuid.uuid4)
    entity_id = factory.LazyFunction(uuid.uuid4)
    entity_type = TimerEntityType.STAGE_TASK.value
    start_datetime = factory.LazyFunction(datetime.now)
    duration_in_seconds = factory.Iterator([1000, 3000, 5000])
    is_running = False
