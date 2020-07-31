from abc import ABC, abstractmethod
from typing import Optional, List

from ib_discussions.constants.enum import EntityType
from ib_discussions.exception.custom_exceptions import DiscussionIdNotFound, \
    UserCannotMarkAsClarified
from ib_discussions.exceptions.custom_exceptions import EntityIdNotFound, \
    InvalidEntityTypeForEntityId
from ib_discussions.interactors.DTOs.common_dtos import DiscussionDTO, \
    OffsetAndLimitDTO, FilterByDTO, SortByDTO
from ib_discussions.interactors.storage_interfaces.dtos import \
    CompleteDiscussionDTO


class StorageInterface(ABC):

    @abstractmethod
    def validate_entity_id(self, entity_id: str) -> Optional[EntityIdNotFound]:
        pass

    @abstractmethod
    def validate_entity_type_for_entity_id(
            self, entity_id: str, entity_type: EntityType
    ) -> Optional[InvalidEntityTypeForEntityId]:
        pass

    @abstractmethod
    def get_discussion_set_id_if_exists(
            self, entity_id: str, entity_type: EntityType
    ) -> Optional[str]:
        pass

    @abstractmethod
    def create_discussion_set_return_id(
            self, entity_id: str, entity_type: EntityType
    ) -> str:
        pass

    @abstractmethod
    def create_discussion(self, discussion_dto: DiscussionDTO,
                          discussion_set_id: str
                          ):
        pass

    @abstractmethod
    def get_complete_discussion_dtos(
            self, discussion_set_id: str, sort_by_dto: SortByDTO,
            offset_and_limit_dto: OffsetAndLimitDTO, filter_by_dto: FilterByDTO
    ) -> List[CompleteDiscussionDTO]:
        pass

    @abstractmethod
    def get_total_discussion_count(self, discussion_set_id: str,
                                   filter_by_dto: FilterByDTO) -> int:
        pass

    @abstractmethod
    def validate_discussion_id(self, discussion_id: str) \
            -> Optional[DiscussionIdNotFound]:
        pass

    @abstractmethod
    def validate_is_user_can_mark_as_clarified(
            self, user_id: str, discussion_id: str
    ) -> Optional[UserCannotMarkAsClarified]:
        pass

    @abstractmethod
    def mark_discussion_clarified(self, discussion_id: str):
        pass
