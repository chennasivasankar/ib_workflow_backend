from typing import List, Optional

from django.db.models import Count

from ib_discussions.constants.enum import EntityType, FilterByEnum, SortByEnum
from ib_discussions.exceptions.custom_exceptions import \
    InvalidEntityTypeForEntityId, EntityIdNotFound, DiscussionIdNotFound, \
    UserCannotMarkAsClarified, DiscussionSetNotFound
from ib_discussions.interactors.dtos.dtos import \
    DiscussionWithEntityDetailsDTO, \
    OffsetAndLimitDTO, FilterByDTO, SortByDTO, \
    DiscussionIdWithTitleAndDescriptionDTO
from ib_discussions.interactors.storage_interfaces.dtos import \
    DiscussionDTO, DiscussionIdWithCommentsCountDTO
from ib_discussions.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class StorageImplementation(StorageInterface):
    def validate_entity_id(self, entity_id: str) -> Optional[EntityIdNotFound]:
        from ib_discussions.models import Entity
        try:
            Entity.objects.get(id=entity_id)
        except Entity.DoesNotExist:
            raise EntityIdNotFound
        return

    def validate_entity_type_for_entity_id(
            self, entity_id: str, entity_type: EntityType
    ) -> Optional[InvalidEntityTypeForEntityId]:
        from ib_discussions.models import Entity
        try:
            entity_object = Entity.objects.get(id=entity_id)
        except Entity.DoesNotExist:
            raise EntityIdNotFound
        is_invalid_entity_type_for_entity_object \
            = entity_object.entity_type != entity_type
        if is_invalid_entity_type_for_entity_object:
            raise InvalidEntityTypeForEntityId
        return

    def get_discussion_set_id_if_exists(
            self, entity_id: str, entity_type: EntityType
    ) -> Optional[str]:
        # self.validate_entity_id(entity_id=entity_id)
        # self.validate_entity_type_for_entity_id(
        #     entity_id=entity_id, entity_type=entity_type
        # )
        from ib_discussions.models import DiscussionSet
        try:
            discussion_set_object = DiscussionSet.objects.get(
                entity_id=entity_id, entity_type=entity_type
            )
        except DiscussionSet.DoesNotExist:
            raise DiscussionSetNotFound
        return str(discussion_set_object.id)

    def create_discussion_set_return_id(
            self, entity_id: str, entity_type: EntityType
    ) -> str:
        from ib_discussions.models import DiscussionSet
        discussion_set_object = DiscussionSet.objects.create(
            entity_id=entity_id, entity_type=entity_type
        )
        return discussion_set_object.id

    def create_discussion(
            self, discussion_set_id: str,
            discussion_with_entity_details_dto: DiscussionWithEntityDetailsDTO

    ):
        from ib_discussions.models import Discussion
        Discussion.objects.create(
            discussion_set_id=discussion_set_id,
            user_id=discussion_with_entity_details_dto.user_id,
            description=discussion_with_entity_details_dto.description,
            title=discussion_with_entity_details_dto.title,
        )

    def get_discussion_dtos(
            self, discussion_set_id: str, sort_by_dto: SortByDTO,
            offset_and_limit_dto: OffsetAndLimitDTO, filter_by_dto: FilterByDTO
    ) -> List[DiscussionDTO]:
        from ib_discussions.models import Discussion
        discussion_objects = Discussion.objects.filter(
            discussion_set_id=discussion_set_id
        )
        filter_discussion_objects = self._get_filter_discussion_objects(
            filter_by_dto=filter_by_dto, discussion_objects=discussion_objects
        )
        sort_discussion_objects = self._get_sort_discussion_objects(
            sort_by_dto=sort_by_dto,
            discussion_objects=filter_discussion_objects
        )
        offset = offset_and_limit_dto.offset
        limit = offset_and_limit_dto.limit
        discussion_objects_after_applying_offset_and_limit \
            = sort_discussion_objects[offset: offset + limit]
        complete_discussion_dtos = self._convert_to_discussion_dtos(
            discussion_objects_after_applying_offset_and_limit
        )
        return complete_discussion_dtos

    def get_total_discussion_count(self, discussion_set_id: str,
                                   filter_by_dto: FilterByDTO) -> int:
        from ib_discussions.models import Discussion
        discussion_objects = Discussion.objects.filter(
            discussion_set_id=discussion_set_id
        )
        filter_discussion_objects = self._get_filter_discussion_objects(
            filter_by_dto=filter_by_dto, discussion_objects=discussion_objects
        )
        return filter_discussion_objects.count()

    def validate_discussion_id(self, discussion_id: str) \
            -> Optional[DiscussionIdNotFound]:
        from ib_discussions.models import Discussion
        discussion_objects = Discussion.objects.filter(
            id=discussion_id
        )
        is_discussion_objects_not_exists = not discussion_objects.exists()
        if is_discussion_objects_not_exists:
            raise DiscussionIdNotFound
        return

    def validate_is_user_can_mark_as_clarified(
            self, user_id: str, discussion_id: str
    ) -> Optional[UserCannotMarkAsClarified]:
        from ib_discussions.models import Discussion
        discussion_objects = Discussion.objects.filter(
            id=discussion_id, user_id=user_id
        )
        is_user_cannot_mark_as_clarified = not discussion_objects.exists()
        if is_user_cannot_mark_as_clarified:
            raise UserCannotMarkAsClarified
        return

    def mark_discussion_clarified(self, discussion_id: str):
        from ib_discussions.models import Discussion
        discussion_object = Discussion.objects.get(
            id=discussion_id
        )
        discussion_object.is_clarified = True
        discussion_object.save()
        return

    @staticmethod
    def _get_filter_discussion_objects(filter_by_dto, discussion_objects):
        if filter_by_dto.filter_by == FilterByEnum.ALL.value:
            return discussion_objects

        if filter_by_dto.filter_by == FilterByEnum.POSTED_BY_ME.value:
            return discussion_objects.filter(user_id=filter_by_dto.value)

        if filter_by_dto.filter_by == FilterByEnum.CLARIFIED.value:
            return discussion_objects.filter(is_clarified=filter_by_dto.value)

        if filter_by_dto.filter_by == FilterByEnum.NOT_CLARIFIED.value:
            return discussion_objects.filter(is_clarified=filter_by_dto.value)

    def _convert_to_discussion_dtos(self, discussion_objects):
        discussion_dtos = [
            self._convert_to_disucssion_dto(discussion_object)
            for discussion_object in discussion_objects
        ]
        return discussion_dtos

    @staticmethod
    def _convert_to_disucssion_dto(discussion_object):
        discussion_dto = DiscussionDTO(
            user_id=str(discussion_object.user_id),
            discussion_id=str(discussion_object.id),
            discussion_set_id=str(discussion_object.discussion_set_id),
            description=discussion_object.description,
            title=discussion_object.title,
            created_at=discussion_object.created_at,
            is_clarified=discussion_object.is_clarified
        )
        return discussion_dto

    @staticmethod
    def _get_sort_discussion_objects(sort_by_dto, discussion_objects):
        if sort_by_dto.sort_by == SortByEnum.LATEST.value:
            return discussion_objects.order_by("-created_at")

    def is_user_can_edit_discussion(self, user_id: str, discussion_id: str) \
            -> bool:
        from ib_discussions.models import Discussion
        discussion_objects = Discussion.objects.filter(
            id=discussion_id, user_id=user_id
        )
        is_discussion_objects_not_exists = not discussion_objects.exists()
        if is_discussion_objects_not_exists:
            return False
        return True

    def is_discussion_id_exists(self, discussion_id: str) -> bool:
        from ib_discussions.models import Discussion
        discussion_objects = Discussion.objects.filter(
            id=discussion_id
        )
        is_discussion_objects_not_exists = not discussion_objects.exists()
        if is_discussion_objects_not_exists:
            return False
        return True

    def update_discussion(
            self,
            discussion_id_with_title_and_description_dto: DiscussionIdWithTitleAndDescriptionDTO):
        discussion_id \
            = discussion_id_with_title_and_description_dto.discussion_id
        title = discussion_id_with_title_and_description_dto.title
        description = discussion_id_with_title_and_description_dto.description
        from ib_discussions.models import Discussion
        discussion_object = Discussion.objects.get(id=discussion_id)

        discussion_object.title = title
        discussion_object.description = description
        discussion_object.save()

    def delete_discussion(self, discussion_id: str):
        from ib_discussions.models import Discussion
        Discussion.objects.filter(id=discussion_id).delete()

    def get_comments_count_for_discussions(self, discussion_set_id: str) -> \
            List[DiscussionIdWithCommentsCountDTO]:
        from ib_discussions.models import Discussion
        discussion_ids = Discussion.objects.filter(
            discussion_set_id=discussion_set_id
        ).values_list("id", flat=True)

        discussion_id_wise_comments_count_dto_dict = {
            str(discussion_id): DiscussionIdWithCommentsCountDTO(
                discussion_id=str(discussion_id), comments_count=0
            )
            for discussion_id in discussion_ids
        }

        from ib_discussions.models import Comment
        discussion_id_with_comments_count_list = Comment.objects.filter(
            discussion_id__in=discussion_ids, parent_comment=None
        ).values(
            "discussion_id"
        ).annotate(
            comments_count=Count("id")
        )

        for discussion_id_with_comments_count_dict in discussion_id_with_comments_count_list:
            discussion_id = \
                discussion_id_with_comments_count_dict["discussion_id"]
            discussion_id_wise_comments_count_dto_dict[
                str(discussion_id)].comments_count = \
                discussion_id_with_comments_count_dict["comments_count"]

        return list(discussion_id_wise_comments_count_dto_dict.values())
