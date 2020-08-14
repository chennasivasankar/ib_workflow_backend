import datetime

import factory

from ib_discussions.interactors.presenter_interfaces.dtos import \
    CommentWithRepliesCountAndEditableDTO, CommentIdWithEditableStatusDTO, \
    DiscussionIdWithEditableStatusDTO


class DiscussionIdWithEditableStatusDTOFactory(factory.Factory):
    class Meta:
        model = DiscussionIdWithEditableStatusDTO

    discussion_id = factory.Faker("uuid4")
    is_editable = factory.Iterator([True, False])


class CommentWithRepliesCountAndEditableDTOFactory(factory.Factory):
    class Meta:
        model = CommentWithRepliesCountAndEditableDTO

    comment_id = factory.Faker("uuid4")
    comment_content = factory.LazyAttribute(lambda obj: "content")
    user_id = factory.Faker("uuid4")
    created_at = datetime.datetime(2008, 1, 1)
    is_editable = factory.Iterator([True, False])
    replies_count = factory.Iterator([1, 2, 3])


class CommentIdWithEditableStatusDTOFactory(factory.Factory):
    class Meta:
        model = CommentIdWithEditableStatusDTO

    comment_id = factory.Faker("uuid4")
    is_editable = factory.Iterator([True, False])
