from abc import ABC, abstractmethod

from ib_discussions.constants.enum import EntityType


class StorageInterface(ABC):

    @abstractmethod
    def validate_entity_id_and_entity_type(
            self, entity_id: str, entity_type: EntityType
    ):
        pass
