from ib_discussions.constants.enum import EntityType
from ib_discussions.interactors.DTOs.common_dtos import DiscussionDTO
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
