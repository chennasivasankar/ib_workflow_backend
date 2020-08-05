from abc import ABC, abstractmethod
from typing import List

from ib_discussions.interactors.presenter_interfaces.dtos import \
    DiscussionsWithUsersAndDiscussionCountDTO
from ib_iam.interactors.presenter_interfaces.dtos import \
    DiscussionIdWithEditableStatusDTO


class CreateDiscussionPresenterInterface(ABC):
    @abstractmethod
    def raise_exception_for_entity_id_not_found(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_entity_type_for_entity_id(self):
        pass

    @abstractmethod
    def prepare_success_response_for_create_discussion(self):
        pass


class GetDiscussionsPresenterInterface(ABC):
    @abstractmethod
    def raise_exception_for_entity_id_not_found(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_entity_type_for_entity_id(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_offset(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_limit(self):
        pass

    @abstractmethod
    def prepare_response_for_discussions_details_dto(
            self,
            discussions_with_users_and_discussion_count_dto: DiscussionsWithUsersAndDiscussionCountDTO,
            discussion_id_with_editable_status_dtos: List[
                DiscussionIdWithEditableStatusDTO]
    ):
        pass

    @abstractmethod
    def raise_exception_for_invalid_user_id(self):
        pass

    @abstractmethod
    def raise_exception_for_discussion_set_not_found(self):
        pass


class MarkDiscussionClarifiedPresenterInterface(ABC):

    @abstractmethod
    def raise_exception_for_discussion_id_not_found(self):
        pass

    @abstractmethod
    def raise_exception_for_user_cannot_mark_as_clarified(self):
        pass

    @abstractmethod
    def raise_success_response_for_mark_discussion_as_clarified(self):
        pass


class UpdateDiscussionPresenterInterface(ABC):

    @abstractmethod
    def response_for_empty_title(self):
        pass

    @abstractmethod
    def response_for_discussion_id_not_found(self):
        pass

    @abstractmethod
    def response_for_user_cannot_update_discussion(self):
        pass

    @abstractmethod
    def prepare_success_response_for_update_discussion(self):
        pass


class DeleteDiscussionPresenterInterface(ABC):

    @abstractmethod
    def response_for_discussion_id_not_found(self):
        pass

    @abstractmethod
    def response_for_user_cannot_delete_discussion(self):
        pass

    @abstractmethod
    def prepare_success_response_for_delete_discussion(self):
        pass


class CreateCommentPresenterInterface(ABC):

    @abstractmethod
    def response_for_discussion_id_not_found(self):
        pass
