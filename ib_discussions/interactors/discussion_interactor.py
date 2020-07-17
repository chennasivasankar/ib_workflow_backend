from ib_discussions.interactors.DTOs.common_dtos import DiscussionDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_discussions.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class EntityIdNotFound(Exception):
    pass


class InvalidEntityTypeForEntityId(Exception):
    pass


class DiscussionSetNotFound(Exception):
    pass


class DiscussionInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_discussion_wrapper(self, discussion_dto: DiscussionDTO,
                                  presenter: PresenterInterface
                                  ):
        try:
            return self._create_discussion_response(
                discussion_dto=discussion_dto, presenter=presenter
            )
        except EntityIdNotFound:
            return presenter.raise_exception_for_entity_id_not_found()
        except InvalidEntityTypeForEntityId:
            return presenter. \
                raise_exception_for_invalid_entity_type_for_entity_id()

    def _create_discussion_response(self, discussion_dto: DiscussionDTO,
                                    presenter: PresenterInterface
                                    ):
        self.create_discussion(discussion_dto=discussion_dto)
        return presenter.prepare_success_response_for_create_discussion()

    def create_discussion(self, discussion_dto):
        self.storage.validate_entity_id(entity_id=discussion_dto.entity_id)
        self.storage.validate_entity_type_for_entity_id(
            entity_id=discussion_dto.entity_id,
            entity_type=discussion_dto.entity_type
        )
        discussion_set_id = self._get_or_create_the_discussion_set(
            discussion_dto=discussion_dto
        )
        self.storage.create_discussion(
            discussion_dto=discussion_dto,
            discussion_set_id=discussion_set_id
        )
        return

    def _get_or_create_the_discussion_set(
            self, discussion_dto: DiscussionDTO
    ):
        try:
            discussion_set_id = self.storage.get_discussion_set_id_if_exists(
                entity_id=discussion_dto.entity_id,
                entity_type=discussion_dto.entity_type
            )
        except DiscussionSetNotFound:
            discussion_set_id = self.storage.create_discussion_set_return_id(
                entity_id=discussion_dto.entity_id,
                entity_type=discussion_dto.entity_type
            )
        return discussion_set_id

