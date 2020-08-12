import factory

from ib_discussions.constants.enum import EntityType, MultimediaFormat
from ib_discussions.interactors.dtos.dtos import DiscussionWithEntityDetailsDTO, \
    DiscussionIdWithTitleAndDescriptionDTO, MultimediaDTO, \
    UpdateCompleteCommentDTO, CreateCompleteCommentDTO


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


class MultimediaDTOFactory(factory.Factory):
    class Meta:
        model = MultimediaDTO

    format_type = factory.Iterator([
        MultimediaFormat.IMAGE.value,
        MultimediaFormat.VIDEO.value
    ])
    url = "https://picsum.photos/200"
    thumbnail_url = "https://picsum.photos/200"


class UpdateCompleteCommentDTOFactory(factory.Factory):
    class Meta:
        model = UpdateCompleteCommentDTO

    comment_id = factory.Faker("uuid4")
    user_id = factory.Faker("uuid4")
    comment_content = "content"
    mention_user_ids = factory.List([
        "10be920b-7b4c-49e7-8adb-41a0c18da848",
        "20be920b-7b4c-49e7-8adb-41a0c18da848"
    ])
    multimedia_dtos = factory.List([])


class CreateCompleteCommentDTOFactory(factory.Factory):
    class Meta:
        model = CreateCompleteCommentDTO

    discussion_id = factory.Faker("uuid4")
    user_id = factory.Faker("uuid4")
    comment_content = "content"
    mention_user_ids = factory.List([
        "10be920b-7b4c-49e7-8adb-41a0c18da848",
        "20be920b-7b4c-49e7-8adb-41a0c18da848"
    ])
    multimedia_dtos = factory.List([])
