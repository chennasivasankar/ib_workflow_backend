from dataclasses import dataclass

from ib_discussions.constants.enum import EntityType
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_discussions.interactors.storage_interfaces.storage_interface import \
    StorageInterface


@dataclass
class DiscussionDTO:
    user_id: str
    entity_id: str
    entity_type: EntityType
    title: str
    description: str


class NotFoundDiscussionSetForEntityIdAndEntityType(Exception):
    pass


class DiscussionInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_discussion_wrapper(self, discussion_dto: DiscussionDTO,
                                  presenter: PresenterInterface
                                  ):
        try:
            self._create_discussion_response(
                discussion_dto=discussion_dto, presenter=presenter
            )
        except NotFoundDiscussionSetForEntityIdAndEntityType:
            return presenter.raise_exception_for_discussions_not_found()

    def _create_discussion_response(self, discussion_dto: DiscussionDTO,
                                    presenter: PresenterInterface
                                    ):
        self.create_discussion(discussion_dto=discussion_dto)
        return

    def create_discussion(self, discussion_dto):
        self.storage.validate_entity_id_and_entity_type(
            entity_id=discussion_dto.entity_id,
            entity_type=discussion_dto.entity_type
        )
