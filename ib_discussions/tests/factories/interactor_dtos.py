import factory

from ib_discussions.constants.enum import EntityType, MultiMediaFormatEnum
from ib_discussions.interactors.dtos.dtos import DiscussionWithEntityDetailsDTO, \
    DiscussionIdWithTitleAndDescriptionDTO, MultiMediaDTO


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


class MultiMediaDTOFactory(factory.Factory):
    class Meta:
        model = MultiMediaDTO

    format_type = factory.Iterator([
        MultiMediaFormatEnum.IMAGE.value,
        MultiMediaFormatEnum.VIDEO.value
    ])
    url = "https://picsum.photos/200"
    thumbnail_url = "https://picsum.photos/200"
