from typing import List

from ib_discussions.constants.enum import EntityType
from ib_discussions.interactors.DTOs.common_dtos import DiscussionDTO, \
    EntityIdAndEntityTypeDTO, OffsetAndLimitDTO
from ib_discussions.interactors.storage_interfaces.dtos import \
    CompleteDiscussionDTO
from ib_discussions.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class StorageImplementation(StorageInterface):
    def validate_entity_id(self, entity_id: str):
        pass

    def validate_entity_type_for_entity_id(self, entity_id: str,
                                           entity_type: EntityType
                                           ):
        pass

    def get_discussion_set_id_if_exists(self, entity_id: str,
                                        entity_type: EntityType
                                        ):
        pass

    def create_discussion_set_return_id(self, entity_id: str,
                                        entity_type: EntityType
                                        ):
        pass

    def create_discussion(self, discussion_dto: DiscussionDTO,
                          discussion_set_id: str
                          ):
        pass

    def get_discussion_set_id(
            self, entity_id_and_entity_type_dto: EntityIdAndEntityTypeDTO
    ) -> str:
        pass

    def get_complete_discussion_dtos(
            self, discussion_set_id: str,
            offset_and_limit_dto: OffsetAndLimitDTO
    ) -> List[CompleteDiscussionDTO]:
        pass

    def get_total_discussion_count(self, discussion_set_id: str) -> int:
        pass
