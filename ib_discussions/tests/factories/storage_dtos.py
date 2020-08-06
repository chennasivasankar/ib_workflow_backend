import datetime

import factory

from ib_discussions.interactors.storage_interfaces.dtos import \
    DiscussionDTO, CommentDTO, CommentIdWithRepliesCountDTO


class DiscussionDTOFactory(factory.Factory):
    class Meta:
        model = DiscussionDTO

    user_id = factory.Faker("uuid4")
    discussion_id = factory.Faker("uuid4")
    discussion_set_id = factory.Faker("uuid4")
    description = factory.LazyAttribute(
        lambda obj: "description".format(
            discussion_id=obj.discussion_id
        )
    )
    title = factory.LazyAttribute(
        lambda obj: "title".format(
            discussion_id=obj.discussion_id
        )
    )
    created_at = datetime.datetime(2008, 1, 1)
    is_clarified = factory.Iterator([True, False])


class CommentDTOFactory(factory.Factory):
    class Meta:
        model = CommentDTO

    comment_id = factory.Faker("uuid4")
    parent_comment_id = factory.Faker("uuid4")
    comment_content = factory.LazyAttribute(lambda obj: "content")
    user_id = factory.Faker("uuid4")
    created_at = datetime.datetime(2008, 1, 1)


class CommentIdWithRepliesCountDTOFactory(factory.Factory):
    class Meta:
        model = CommentIdWithRepliesCountDTO

    comment_id = factory.Faker("uuid4")
    replies_count = factory.Iterator([1, 2, 3, 4])
