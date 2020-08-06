from abc import ABC, abstractmethod
from typing import List

from ib_discussions.interactors.storage_interfaces.dtos import \
    CommentIdWithRepliesCountDTO


class CommentStorageInterface(ABC):

    @abstractmethod
    def is_discussion_id_exists(self, discussion_id: str) -> bool:
        pass

    @abstractmethod
    def create_comment_for_discussion(self, user_id: str, discussion_id: str,
                                      comment_content: str):
        pass

    @abstractmethod
    def get_comment_details_dto(self, comment_id: str):
        pass

    @abstractmethod
    def get_replies_count_for_comments(
            self, comment_ids: List[str]) -> List[CommentIdWithRepliesCountDTO]:
        pass

    @abstractmethod
    def get_comments_for_discussion(self, discussion_id: str):
        pass
