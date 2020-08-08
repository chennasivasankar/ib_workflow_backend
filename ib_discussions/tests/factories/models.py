import datetime

import factory

from ib_discussions.constants.enum import EntityType, MultiMediaFormatEnum
from ib_discussions.models.comment import Comment, CommentWithMultiMedia, \
    CommentWithMentionUserId
from ib_discussions.models.discussion import Discussion
from ib_discussions.models.discussion_set import DiscussionSet
from ib_discussions.models.entity import Entity
from ib_discussions.models.multimedia import MultiMedia


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
    user_id = factory.Iterator(
        [
            "9cc22e39-2390-4d96-b7ac-6bb27816461f",
            "cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a",
            "e597ab2f-a10c-4164-930e-23af375741cb"
        ]
    )
    title = factory.LazyAttribute(
        lambda obj: "title"
    )
    description = factory.LazyAttribute(
        lambda obj: "description"
    )
    created_at = factory.Iterator([
        datetime.datetime(2008, 1, 1),
        datetime.datetime(2020, 5, 1),
        datetime.datetime(2020, 1, 20),
        datetime.datetime(2007, 2, 5)
    ])
    is_clarified = factory.Iterator([True, False])


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    id = factory.Faker("uuid4")
    user_id = factory.Faker("uuid4")
    discussion = factory.SubFactory(DiscussionFactory)
    content = factory.LazyAttribute(lambda obj: "content")
    created_at = factory.Iterator([
        datetime.datetime(2008, 1, 1),
        datetime.datetime(2020, 5, 1),
        datetime.datetime(2020, 1, 20),
        datetime.datetime(2007, 2, 5)
    ])


class ReplyToCommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    id = factory.Faker("uuid4")
    user_id = factory.Faker("uuid4")
    discussion = factory.SubFactory(DiscussionFactory)
    parent_comment = factory.SubFactory(CommentFactory)
    content = factory.LazyAttribute(lambda obj: "content")
    created_at = factory.Iterator([
        datetime.datetime(2008, 1, 1),
        datetime.datetime(2020, 5, 1),
        datetime.datetime(2020, 1, 20),
        datetime.datetime(2007, 2, 5)
    ])


class MultiMediaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MultiMedia

    id = factory.Faker("uuid")
    format_type = factory.Iterator([
        MultiMediaFormatEnum.IMAGE.value,
        MultiMediaFormatEnum.VIDEO.value
    ])
    url = "https://picsum.photos/200"


class CommentWithMultiMediaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CommentWithMultiMedia

    comment = factory.SubFactory(CommentFactory)
    multimedia = factory.SubFactory(MultiMediaFactory)


class CommentWithMentionUserIdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CommentWithMentionUserId

    comment = factory.SubFactory(CommentFactory)
    mention_user_id = factory.Faker("uuid")
