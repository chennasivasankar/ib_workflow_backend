import datetime

import factory
from ib_discussions.interactors.storage_interfaces.dtos import \
    CompleteDiscussionDTO


class CompleteDiscussionFactory(factory.Factory):
    class Meta:
        model = CompleteDiscussionDTO

    user_id = factory.Faker("uuid4")
    discussion_id = factory.Faker("uuid4")
    discussion_set_id = factory.Faker("uuid4")
    description = factory.LazyAttribute(
        lambda obj: "Description of discussion id is {discussion_id}".format(
            discussion_id=obj.discussion_id
        )
    )
    title = factory.LazyAttribute(
        lambda obj: "Title of discussion id is {discussion_id}".format(
            discussion_id=obj.discussion_id
        )
    )
    created_at = datetime.datetime(2008, 1, 1, tzinfo=datetime.timezone.utc)
    is_clarified = factory.Iterator([True, False])
