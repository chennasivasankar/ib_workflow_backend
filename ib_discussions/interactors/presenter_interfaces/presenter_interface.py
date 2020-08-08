from abc import ABC, abstractmethod
from typing import List

from ib_discussions.adapters.auth_service import UserProfileDTO
from ib_discussions.interactors.presenter_interfaces.dtos import \
    DiscussionsWithUsersAndDiscussionCountDTO, \
    CommentWithRepliesCountAndEditableDTO, CommentIdWithEditableStatusDTO
from ib_discussions.interactors.storage_interfaces.dtos import CommentDTO, \
    DiscussionIdWithCommentsCountDTO, CommentIdWithMultiMediaDTO, \
    CommentIdWithMentionUserIdDTO
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
                DiscussionIdWithEditableStatusDTO],
            discussion_id_with_comments_count_dtos: List[DiscussionIdWithCommentsCountDTO]
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

    @abstractmethod
    def prepare_response_for_comment(
            self,
            comment_with_replies_count_and_editable_dto: CommentWithRepliesCountAndEditableDTO,
            user_profile_dtos: List[UserProfileDTO],
            comment_id_with_multimedia_dtos: List[CommentIdWithMultiMediaDTO],
            comment_id_with_mention_user_id_dtos: List[CommentIdWithMentionUserIdDTO]
    ):
        pass


class GetCommentsForDiscussionPresenterInterface(ABC):

    @abstractmethod
    def response_for_discussion_id_not_found(self):
        pass

    @abstractmethod
    def prepare_response_for_comments_with_users_dtos(
            self,
            comment_with_replies_count_and_editable_dtos: List[
                CommentWithRepliesCountAndEditableDTO],
            user_profile_dtos: List[UserProfileDTO],
            comment_id_with_multimedia_dtos: List[CommentIdWithMultiMediaDTO],
            comment_id_with_mention_user_id_dtos: List[
                CommentIdWithMentionUserIdDTO]
    ):
        pass


class CreateReplyPresenterInterface(ABC):

    @abstractmethod
    def response_for_comment_id_not_found(self):
        pass

    @abstractmethod
    def prepare_response_for_reply(
            self, comment_dto: CommentDTO,
            comment_with_editable_status_dto: CommentIdWithEditableStatusDTO,
            user_profile_dto: UserProfileDTO
    ):
        pass


class GetRepliesForCommentPresenterInterface(ABC):

    @abstractmethod
    def response_for_comment_id_not_found(self):
        pass

    @abstractmethod
    def prepare_response_for_replies_with_users_dtos(
            self, user_profile_dtos: List[UserProfileDTO],
            comment_with_editable_status_dtos: List[
                CommentIdWithEditableStatusDTO],
            comment_dtos: List[CommentDTO]
    ):
        pass
