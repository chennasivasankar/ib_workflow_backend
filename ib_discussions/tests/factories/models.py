import datetime

import factory

from ib_discussions.constants.enum import EntityType
from ib_discussions.models.discussion import Discussion
from ib_discussions.models.discussion_set import DiscussionSet
from ib_discussions.models.entity import Entity


class EntityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Entity

    id = factory.Faker("uuid4")
    entity_type = factory.Iterator([
        EntityType.TASK.value
    ])


class DiscussionSetFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = DiscussionSet

    id = factory.Faker("uuid4")
    entity_id = factory.Faker("uuid4")
    entity_type = factory.Iterator([
        EntityType.TASK.value
    ])


class DiscussionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Discussion

    id = factory.Faker("uuid4")
    discussion_set = factory.SubFactory(DiscussionSetFactory)
    user_id = factory.Iterator(["41a0c18da848", "d3482aaa30e5", "1d42bb68e3ce"])
    title = factory.LazyAttribute(
        lambda obj: "title of {id}".format(id=obj.id)
    )
    description = factory.LazyAttribute(
        lambda obj: "title of {id}".format(id=obj.id)
    )
    created_at = datetime.datetime(2008, 1, 1, tzinfo=datetime.timezone.utc)
    is_clarified = factory.Iterator([True, False])
