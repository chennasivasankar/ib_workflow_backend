from typing import List, Optional

from ib_discussions.constants.enum import EntityType, FilterByEnum
from ib_discussions.exceptions.custom_exceptions import \
    InvalidEntityTypeForEntityId, EntityIdNotFound
from ib_discussions.interactors.DTOs.common_dtos import DiscussionDTO, \
    OffsetAndLimitDTO, FilterByDTO, SortByDTO
from ib_discussions.interactors.storage_interfaces.dtos import \
    CompleteDiscussionDTO
from ib_discussions.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class StorageImplementation(StorageInterface):
    def validate_entity_id(self, entity_id: str) -> Optional[EntityIdNotFound]:
        try:
            from ib_discussions.models import Entity
            Entity.objects.get(id=entity_id)
        except Exception:
            raise EntityIdNotFound
        return

    def validate_entity_type_for_entity_id(
            self, entity_id: str, entity_type: EntityType
    ) -> Optional[InvalidEntityTypeForEntityId]:
        try:
            from ib_discussions.models import Entity
            entity_object = Entity.objects.get(id=entity_id)
        except Exception:
            raise EntityIdNotFound
        is_invalid_entity_type_for_entity_object \
            = entity_object.entity_type != entity_type
        if is_invalid_entity_type_for_entity_object:
            raise InvalidEntityTypeForEntityId
        return

    def get_discussion_set_id_if_exists(
            self, entity_id: str, entity_type: EntityType
    ) -> Optional[str]:
        self.validate_entity_id(entity_id=entity_id)
        self.validate_entity_type_for_entity_id(
            entity_id=entity_id, entity_type=entity_type
        )
        try:
            from ib_discussions.models import DiscussionSet
            discussion_set_object = DiscussionSet.objects.get(
                entity_id=entity_id, entity_type=entity_type
            )
        except Exception:
            from ib_discussions.interactors.discussion_interactor import \
                DiscussionSetNotFound
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

    def create_discussion(self, discussion_dto: DiscussionDTO,
                          discussion_set_id: str
                          ):
        from ib_discussions.models import Discussion
        Discussion.objects.create(
            discussion_set_id=discussion_set_id,
            user_id=discussion_dto.user_id,
            description=discussion_dto.description,
            title=discussion_dto.title,
        )

    def get_complete_discussion_dtos(
            self, discussion_set_id: str, sort_by_dto: SortByDTO,
            offset_and_limit_dto: OffsetAndLimitDTO, filter_by_dto: FilterByDTO
    ) -> List[CompleteDiscussionDTO]:
        from ib_discussions.models import Discussion
        discussion_objects = Discussion.objects.filter(
            discussion_set_id=discussion_set_id
        )
        filter_discussion_objects = self._get_filter_discussion_objects(
            filter_by_dto=filter_by_dto, discussion_objects=discussion_objects
        )
        complete_discussion_dtos = self._convert_to_discussion_dtos(
            filter_discussion_objects
        )
        return complete_discussion_dtos

    def get_total_discussion_count(self, discussion_set_id: str) -> int:
        from ib_discussions.models import Discussion
        count = Discussion.objects.filter(
            discussion_set_id=discussion_set_id
        ).count()
        return count

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
        discussion_dto = CompleteDiscussionDTO(
            user_id=discussion_object.user_id,
            discussion_id=str(discussion_object.id),
            discussion_set_id=str(discussion_object.discussion_set_id),
            description=discussion_object.description,
            title=discussion_object.title,
            created_at=discussion_object.created_at,
            is_clarified=discussion_object.is_clarified
        )
        return discussion_dto

