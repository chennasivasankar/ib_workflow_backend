import abc
from typing import Optional, List

from ib_discussions.constants.enum import EntityType
from ib_discussions.exceptions.custom_exceptions import DiscussionIdNotFound, \
    UserCannotMarkAsClarified
from ib_discussions.interactors.dtos.dtos import \
    DiscussionWithEntityDetailsDTO, \
    OffsetAndLimitDTO, FilterByDTO, SortByDTO, \
    DiscussionIdWithTitleAndDescriptionDTO
from ib_discussions.interactors.storage_interfaces.dtos import \
    DiscussionDTO, DiscussionIdWithCommentsCountDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_discussion_set_id_if_exists(
            self, entity_id: str, entity_type: EntityType
    ) -> Optional[str]:
        pass

    @abc.abstractmethod
    def create_discussion_set_return_id(
            self, entity_id: str, entity_type: EntityType
    ) -> str:
        pass

    @abc.abstractmethod
    def create_discussion(
            self, discussion_set_id: str,
            discussion_with_entity_details_dto: DiscussionWithEntityDetailsDTO
    ):
        pass

    @abc.abstractmethod
    def get_discussion_dtos(
            self, discussion_set_id: str, sort_by_dto: SortByDTO,
            offset_and_limit_dto: OffsetAndLimitDTO, filter_by_dto: FilterByDTO
    ) -> List[DiscussionDTO]:
        pass

    @abc.abstractmethod
    def get_total_discussion_count(self, discussion_set_id: str,
                                   filter_by_dto: FilterByDTO) -> int:
        pass

    @abc.abstractmethod
    def validate_discussion_id(self, discussion_id: str) \
            -> Optional[DiscussionIdNotFound]:
        pass

    @abc.abstractmethod
    def validate_is_user_can_mark_as_clarified(
            self, user_id: str, discussion_id: str
    ) -> Optional[UserCannotMarkAsClarified]:
        pass

    @abc.abstractmethod
    def mark_discussion_clarified(self, discussion_id: str):
        pass

    @abc.abstractmethod
    def is_user_can_edit_discussion(self, user_id: str, discussion_id: str) \
            -> bool:
        pass

    @abc.abstractmethod
    def is_discussion_id_exists(self, discussion_id: str) -> bool:
        pass

    @abc.abstractmethod
    def update_discussion(
            self,
            discussion_id_with_title_and_description_dto: DiscussionIdWithTitleAndDescriptionDTO):
        pass

    @abc.abstractmethod
    def delete_discussion(self, discussion_id: str):
        pass

    @abc.abstractmethod
    def get_comments_count_for_discussions(self, discussion_set_id: str) -> \
            List[DiscussionIdWithCommentsCountDTO]:
        pass
