import factory

from ib_discussions.constants.enum import EntityType
from ib_discussions.interactors.DTOs.common_dtos import DiscussionDTO


class DiscussionDTOFactory(factory.Factory):
    class Meta:
        model = DiscussionDTO

    user_id = factory.Faker("uuid")
    entity_id = factory.Faker("uuid")
    entity_type = factory.Iterator(
        [EntityType.TASK.value, EntityType.COLUMN.value, EntityType.BOARD.value]
    )
    title = factory.LazyAttribute(lambda obj: "title")
    description = factory.LazyAttribute(lambda obj: "description")
