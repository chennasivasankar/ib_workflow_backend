from abc import ABC, abstractmethod
from typing import List, Optional

from ib_discussions.interactors.dtos.dtos import MultiMediaDTO
from ib_discussions.interactors.storage_interfaces.dtos import \
    CommentIdWithRepliesCountDTO, CommentDTO, CommentIdWithMentionUserIdDTO, \
    CommentIdWithMultiMediaDTO


class CommentStorageInterface(ABC):

    @abstractmethod
    def is_discussion_id_exists(self, discussion_id: str) -> bool:
        pass

    @abstractmethod
    def create_comment_for_discussion(self, user_id: str, discussion_id: str,
                                      comment_content: str):
        pass

    @abstractmethod
    def get_comment_details_dto(self, comment_id: str) -> CommentDTO:
        pass

    @abstractmethod
    def get_replies_count_for_comments(
            self, comment_ids: List[str]) -> List[CommentIdWithRepliesCountDTO]:
        pass

    @abstractmethod
    def get_comments_for_discussion_dtos(self, discussion_id: str) -> \
            List[CommentDTO]:
        pass

    @abstractmethod
    def is_comment_id_exists(self, comment_id: str) -> bool:
        pass

    @abstractmethod
    def get_parent_comment_id(self, comment_id: str) -> Optional[str]:
        pass

    @abstractmethod
    def get_discussion_id(self, comment_id: str) -> str:
        pass

    @abstractmethod
    def create_reply_to_comment(
            self, parent_comment_id: str, comment_content: str,
            user_id: str, discussion_id: str) -> str:
        pass

    @abstractmethod
    def get_replies_dtos(self, comment_id: str) -> List[CommentDTO]:
        pass

    @abstractmethod
    def add_mention_users_to_comment(self, comment_id: str,
                                     mention_user_ids: List[str]):
        pass

    @abstractmethod
    def add_multimedia_to_comment(self, comment_id,
                                   multimedia_dtos: List[MultiMediaDTO]):
        pass

    @abstractmethod
    def get_mention_user_ids(self, comment_ids: List[str]) -> List[str]:
        pass

    @abstractmethod
    def get_comment_id_with_mention_user_id_dtos(self, comment_ids: List[str]) \
            -> List[CommentIdWithMentionUserIdDTO]:
        pass

    @abstractmethod
    def get_multimedia_dtos(self, comment_ids: List[str]) -> \
            List[CommentIdWithMultiMediaDTO]:
        pass
