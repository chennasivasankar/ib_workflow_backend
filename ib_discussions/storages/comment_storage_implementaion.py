from typing import List, Optional

from django.db.models import Count

from ib_discussions.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface
from ib_discussions.interactors.storage_interfaces.dtos import CommentDTO, \
    CommentIdWithRepliesCountDTO
from ib_discussions.models import Comment


class CommentStorageImplementation(CommentStorageInterface):

    def is_discussion_id_exists(self, discussion_id: str) -> bool:
        from ib_discussions.models import Discussion
        discussion_objects = Discussion.objects.filter(
            id=discussion_id
        )
        is_discussion_objects_exists = discussion_objects.exists()
        return is_discussion_objects_exists

    def create_comment_for_discussion(self, user_id: str, discussion_id: str,
                                      comment_content: str):
        comment_object = Comment.objects.create(
            user_id=user_id, discussion_id=discussion_id,
            content=comment_content
        )
        return str(comment_object.id)

    def get_comment_details_dto(self, comment_id: str) -> CommentDTO:
        comment_object = Comment.objects.get(id=comment_id)
        comment_dto = CommentDTO(
            comment_id=comment_object.id,
            comment_content=comment_object.content,
            user_id=comment_object.user_id,
            created_at=comment_object.created_at,
            parent_comment_id=comment_object.parent_comment
        )
        return comment_dto

    def get_replies_count_for_comments(
            self, comment_ids: List[str]) -> List[CommentIdWithRepliesCountDTO]:
        comment_id_wise_replies_count_dto_dict = {
            str(comment_id): CommentIdWithRepliesCountDTO(
                comment_id=comment_id, replies_count=0
            )
            for comment_id in comment_ids
        }

        comment_id_with_replies_count_list = Comment.objects.filter(
            parent_comment_id__in=comment_ids
        ).values(
            "parent_comment_id"
        ).annotate(
            replies_count=Count("parent_comment_id")
        )
        for comment_id_with_replies_count_dict in comment_id_with_replies_count_list:
            comment_id = comment_id_with_replies_count_dict[
                "parent_comment_id"]
            comment_id_wise_replies_count_dto_dict[
                str(comment_id)].replies_count = \
                comment_id_with_replies_count_dict["replies_count"]

        return list(comment_id_wise_replies_count_dto_dict.values())

    def get_comments_for_discussion_dtos(self, discussion_id: str) -> \
            List[CommentDTO]:
        comment_objects = Comment.objects.filter(
            discussion_id=discussion_id,
            parent_comment_id=None
        )
        comment_dtos = [
            CommentDTO(
                comment_id=comment_object.id,
                comment_content=comment_object.content,
                user_id=comment_object.user_id,
                created_at=comment_object.created_at,
                parent_comment_id=comment_object.parent_comment_id
            )
            for comment_object in comment_objects
        ]
        return comment_dtos

    def is_comment_id_exists(self, comment_id: str) -> bool:
        comment_objects = Comment.objects.filter(id=comment_id)
        is_comment_objects_exists = comment_objects.exists()
        return is_comment_objects_exists

    def get_parent_comment_id(self, comment_id: str) -> Optional[str]:
        comment_object = Comment.objects.get(id=comment_id)
        if comment_object.parent_comment_id is None:
            return None
        return str(comment_object.parent_comment_id)

    def get_discussion_id(self, comment_id: str) -> str:
        comment_object = Comment.objects.get(id=comment_id)
        return str(comment_object.discussion_id)

    def create_reply_to_comment(
            self, parent_comment_id: str, comment_content: str,
            user_id: str, discussion_id: str) -> str:
        parent_comment_objects = Comment.objects.filter(id=parent_comment_id)
        is_parent_comment_object_exists = parent_comment_objects.exists()
        if is_parent_comment_object_exists:
            comment_object = Comment.objects.create(
                user_id=user_id, discussion_id=discussion_id,
                content=comment_content, parent_comment=parent_comment_objects[0]
            )
        else:
            comment_object = Comment.objects.create(
                user_id=user_id, discussion_id=discussion_id,
                content=comment_content
            )
        return str(comment_object.id)

    def get_replies_dtos(self, comment_id: str) -> List[CommentDTO]:
        comment_objects = Comment.objects.filter(parent_comment_id=comment_id)
        comment_dtos = [
            CommentDTO(
                comment_id=comment_object.id,
                comment_content=comment_object.content,
                user_id=comment_object.user_id,
                created_at=comment_object.created_at,
                parent_comment_id=comment_object.parent_comment_id
            )
            for comment_object in comment_objects
        ]
        return comment_dtos
