from abc import ABC, abstractmethod
from typing import Optional

from ib_discussions.constants.enum import EntityType
from ib_discussions.interactors.DTOs.common_dtos import DiscussionDTO
from ib_discussions.interactors.discussion_interactor import \
    EntityIdAndEntityTypeDTO, EntityIdNotFound, InvalidEntityTypeForEntityId
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
    def get_discussion_set_id(
            self, entity_id_and_entity_type_dto: EntityIdAndEntityTypeDTO
    ) -> str:
        pass

    @abstractmethod
    def get_complete_discussion_dtos(
            self, discussion_set_id: str
    ) -> CompleteDiscussionDTO:
        pass
