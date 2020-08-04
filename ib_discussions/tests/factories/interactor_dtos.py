import factory

from ib_discussions.constants.enum import EntityType
from ib_discussions.interactors.dtos.dtos import DiscussionWithEntityDetailsDTO, \
    DiscussionIdWithTitleAndDescriptionDTO


class DiscussionWithEntityDetailsDTOFactory(factory.Factory):
    class Meta:
        model = DiscussionWithEntityDetailsDTO

    user_id = factory.Faker("uuid")
    entity_id = factory.Faker("uuid")
    entity_type = factory.Iterator(
        [EntityType.TASK.value, EntityType.COLUMN.value, EntityType.BOARD.value]
    )
    title = factory.LazyAttribute(lambda obj: "title")
    description = factory.LazyAttribute(lambda obj: "description")


class DiscussionIdWithTitleAndDescriptionDTOFactory(factory.Factory):
    class Meta:
        model = DiscussionIdWithTitleAndDescriptionDTO

    discussion_id = factory.Faker("uuid4")
    title = factory.LazyAttribute(lambda obj: "title")
    description = factory.LazyAttribute(lambda obj: "description")
