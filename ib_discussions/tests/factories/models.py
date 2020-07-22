import datetime

import factory

from ib_discussions.constants.enum import EntityType
from ib_discussions.models.discussion import Discussion
from ib_discussions.models.discussion_set import DiscussionSet
from ib_discussions.models.entity import Entity


class EntityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Entity

    id = factory.Faker("uuid")
    entity_type = factory.Iterator([
        EntityType.TASK.value,
        EntityType.BOARD.value,
        EntityType.COLUMN.value
    ])


class DiscussionSetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DiscussionSet

    id = factory.Faker("uuid")
    entity_id = factory.Faker("uuid")
    entity_type = factory.Iterator([
        EntityType.TASK.value,
        EntityType.BOARD.value,
        EntityType.COLUMN.value
    ])


class DiscussionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Discussion

    id = factory.Faker("uuid")
    discussion_set_id = factory.Faker("uuid")
    title = factory.LazyFunction(
        lambda obj: "title of {id}".format(id=obj.id)
    )
    description = factory.LazyFunction(
        lambda obj: "title of {id}".format(id=obj.id)
    )
    created_at = datetime.datetime(2008, 1, 1, tzinfo=datetime.timezone.utc)
    is_clarified = factory.Iterator([True, False])