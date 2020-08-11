from ib_discussions.exceptions.custom_exceptions import DiscussionSetNotFound, \
    DiscussionIdNotFound
from ib_discussions.interactors.dtos.dtos import \
    DiscussionWithEntityDetailsDTO, DiscussionIdWithTitleAndDescriptionDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    CreateDiscussionPresenterInterface, UpdateDiscussionPresenterInterface, \
    DeleteDiscussionPresenterInterface
from ib_discussions.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class EmptyTitle(Exception):
    pass


class UserCannotEditDiscussion(Exception):
    pass


class DiscussionInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_discussion_wrapper(
            self,
            discussion_with_entity_details_dto: DiscussionWithEntityDetailsDTO,
            presenter: CreateDiscussionPresenterInterface
    ):
        from ib_discussions.exceptions.custom_exceptions import \
            EntityIdNotFound, InvalidEntityTypeForEntityId
        try:
            response = self._create_discussion_response(
                discussion_with_entity_details_dto \
                    =discussion_with_entity_details_dto,
                presenter=presenter
            )
        except EntityIdNotFound:
            response = presenter.raise_exception_for_entity_id_not_found()
        except InvalidEntityTypeForEntityId:
            response = presenter. \
                raise_exception_for_invalid_entity_type_for_entity_id()
        return response

    def _create_discussion_response(
            self,
            discussion_with_entity_details_dto: DiscussionWithEntityDetailsDTO,
            presenter: CreateDiscussionPresenterInterface
    ):
        self.create_discussion(
            discussion_with_entity_details_dto \
                =discussion_with_entity_details_dto
        )
        return presenter.prepare_success_response_for_create_discussion()

    def create_discussion(
            self,
            discussion_with_entity_details_dto: DiscussionWithEntityDetailsDTO
    ):
        discussion_set_id = self._get_or_create_the_discussion_set(
            discussion_with_entity_details_dto \
                =discussion_with_entity_details_dto
        )
        self.storage.create_discussion(
            discussion_with_entity_details_dto \
                =discussion_with_entity_details_dto,
            discussion_set_id=discussion_set_id
        )
        return

    def _get_or_create_the_discussion_set(
            self,
            discussion_with_entity_details_dto: DiscussionWithEntityDetailsDTO
    ):
        entity_id = discussion_with_entity_details_dto.entity_id
        entity_type = discussion_with_entity_details_dto.entity_type
        try:
            discussion_set_id = self.storage.get_discussion_set_id_if_exists(
                entity_id=entity_id,
                entity_type=entity_type
            )
        except DiscussionSetNotFound:
            discussion_set_id = self.storage.create_discussion_set_return_id(
                entity_id=entity_id,
                entity_type=entity_type
            )
        return discussion_set_id

    def update_discussion_wrapper(
            self,
            discussion_id_with_title_and_description_dto: DiscussionIdWithTitleAndDescriptionDTO,
            user_id: str, presenter: UpdateDiscussionPresenterInterface
    ):
        try:
            self.update_discussion(
                user_id=user_id,
                discussion_id_with_title_and_description_dto \
                    =discussion_id_with_title_and_description_dto
            )
            response = presenter.prepare_success_response_for_update_discussion()
        except EmptyTitle:
            response = presenter.response_for_empty_title()
        except DiscussionIdNotFound:
            response = presenter.response_for_discussion_id_not_found()
        except UserCannotEditDiscussion:
            response = presenter.response_for_user_cannot_update_discussion()
        return response

    def update_discussion(
            self,
            discussion_id_with_title_and_description_dto: DiscussionIdWithTitleAndDescriptionDTO,
            user_id: str
    ):
        title = discussion_id_with_title_and_description_dto.title
        discussion_id \
            = discussion_id_with_title_and_description_dto.discussion_id
        is_title_empty = not title
        if is_title_empty:
            raise EmptyTitle
        self._validate_discussion_id(discussion_id)
        self._validate_is_user_cannot_edit_discussion(discussion_id, user_id)
        self.storage.update_discussion(
            discussion_id_with_title_and_description_dto
        )
        return

    def _validate_is_user_cannot_edit_discussion(self, discussion_id,
                                                 user_id):
        is_user_cannot_update = not self.storage.is_user_can_edit_discussion(
            user_id=user_id, discussion_id=discussion_id
        )
        if is_user_cannot_update:
            raise UserCannotEditDiscussion

    def _validate_discussion_id(self, discussion_id):
        is_discussion_id_not_exists = not self.storage.is_discussion_id_exists(
            discussion_id=discussion_id
        )
        if is_discussion_id_not_exists:
            raise DiscussionIdNotFound

    def delete_discussion_wrapper(self, discussion_id: str, user_id: str,
                                  presenter: DeleteDiscussionPresenterInterface):
        try:
            self.delete_discussion(discussion_id=discussion_id, user_id=user_id)
            response \
                = presenter.prepare_success_response_for_delete_discussion()
        except DiscussionIdNotFound:
            response = presenter.response_for_discussion_id_not_found()
        except UserCannotEditDiscussion:
            response = presenter.response_for_user_cannot_delete_discussion()
        return response

    def delete_discussion(self, discussion_id, user_id):
        self._validate_discussion_id(discussion_id)
        self._validate_is_user_cannot_edit_discussion(discussion_id, user_id)
        self.storage.delete_discussion(discussion_id=discussion_id)
