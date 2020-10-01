import factory

from ib_discussions.constants.enum import EntityType, MultimediaFormat, \
    FilterByEnum, SortByEnum, OrderByEnum
from ib_discussions.interactors.dtos.dtos import DiscussionWithEntityDetailsDTO, \
    DiscussionIdWithTitleAndDescriptionDTO, MultimediaDTO, \
    UpdateCompleteCommentDTO, CreateCompleteCommentDTO, \
    CreateCompleteReplyToCommentDTO, FilterByDTO, SortByDTO, \
    GetProjectDiscussionsInputDTO, EntityIdAndEntityTypeDTO, OffsetAndLimitDTO


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


class CreateCompleteReplyToCommentDTOFactory(factory.Factory):
    class Meta:
        model = CreateCompleteReplyToCommentDTO

    comment_id = factory.Faker("uuid4")
    user_id = factory.Faker("uuid4")
    comment_content = "content"
    mention_user_ids = factory.List([
        "10be920b-7b4c-49e7-8adb-41a0c18da848",
        "20be920b-7b4c-49e7-8adb-41a0c18da848"
    ])
    multimedia_dtos = factory.List([])


class FilterByDTOFactory(factory.Factory):
    class Meta:
        model = FilterByDTO

    filter_by = factory.Iterator([
        FilterByEnum.ALL.value,
        FilterByEnum.POSTED_BY_ME.value,
        FilterByEnum.CLARIFIED.value,
        FilterByEnum.NOT_CLARIFIED.value
    ]
    )
    value = factory.Iterator([True, False])


class SortByDTOFactory(factory.Factory):
    class Meta:
        model = SortByDTO

    sort_by = factory.Iterator([
        SortByEnum.LATEST.value, SortByEnum.TOP.value])
    order = factory.Iterator([
        OrderByEnum.ASC.value, OrderByEnum.DESC.value
    ])


class EntityIdAndEntityTypeDTOFactory(factory.Factory):
    class Meta:
        model = EntityIdAndEntityTypeDTO

    entity_id = factory.sequence(lambda n: "entity_{}".format(n))
    entity_type = factory.Iterator([
        EntityType.TASK.value, EntityType.COLUMN.value,
        EntityType.BOARD.value, EntityType.PROJECT.value
    ])


class OffsetAndLimitDTOFactory(factory.Factory):
    class Meta:
        model = OffsetAndLimitDTO

    offset = 0
    limit = 5


class GetProjectDiscussionsInputDTOFactory(factory.Factory):
    class Meta:
        model = GetProjectDiscussionsInputDTO

    user_id = factory.sequence(lambda n: "user_id_{}".format(n))
    project_id = factory.sequence(lambda n: "project_id_{}".format(n))
    entity_id_and_entity_type_dto = factory.SubFactory(
        EntityIdAndEntityTypeDTOFactory)
    offset_and_limit_dto = factory.SubFactory(OffsetAndLimitDTOFactory)
    filter_by_dto = factory.SubFactory(FilterByDTOFactory)
    sort_by_dto = factory.SubFactory(SortByDTOFactory)
