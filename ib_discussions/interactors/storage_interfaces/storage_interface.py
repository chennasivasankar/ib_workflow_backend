from abc import ABC, abstractmethod

from ib_discussions.constants.enum import EntityType
from ib_discussions.interactors.DTOs.common_dtos import DiscussionDTO


class StorageInterface(ABC):

    @abstractmethod
    def validate_entity_id(self, entity_id: str):
        pass

    @abstractmethod
    def validate_entity_type_for_entity_id(self, entity_id: str,
                                           entity_type: EntityType
                                           ):
        pass

    @abstractmethod
    def get_discussion_set_id_if_exists(self, entity_id: str,
                                        entity_type: EntityType
                                        ):
        pass

    @abstractmethod
    def create_discussion_set_return_id(self, entity_id: str,
                                        entity_type: EntityType
                                        ):
        pass

    @abstractmethod
    def create_discussion(self, discussion_dto: DiscussionDTO,
                          discussion_set_id: str
                          ):
        pass
