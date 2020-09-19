from typing import List

from ib_discussions.adapters.auth_service import UserProfileDTO
from ib_discussions.exceptions.custom_exceptions import \
    EmptyCommentAndMultiMediaException
from ib_discussions.interactors.dtos.dtos import \
    CreateCompleteReplyToCommentDTO
from ib_discussions.interactors.dtos.dtos import \
    MultimediaDTO
from ib_discussions.interactors.presenter_interfaces.dtos import \
    CommentIdWithEditableStatusDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    CreateReplyPresenterInterface
from ib_discussions.interactors.storage_interfaces.comment_storage_interface import \
    CommentStorageInterface
from ib_discussions.interactors.storage_interfaces.dtos import CommentDTO


class CreateReplyToCommentInteractor:

    def __init__(self, storage: CommentStorageInterface):
        self.storage = storage

    def reply_to_comment_wrapper(
            self, presenter: CreateReplyPresenterInterface,
            create_complete_reply_to_comment_dto: CreateCompleteReplyToCommentDTO
    ):
        from ib_discussions.adapters.auth_service import InvalidUserIds
        from ib_discussions.exceptions.custom_exceptions import \
            CommentIdNotFound

        try:
            response = self._reply_to_comment_response(
                presenter=presenter,
                reply_details_dto=create_complete_reply_to_comment_dto
            )
        except EmptyCommentAndMultiMediaException:
            response = \
                presenter.response_for_comment_or_multimedia_should_be_provided()
        except CommentIdNotFound:
            response = presenter.response_for_comment_id_not_found()
        except InvalidUserIds as err:
            response = presenter.response_for_invalid_user_ids(err)
        return response

    def _reply_to_comment_response(
            self, presenter: CreateReplyPresenterInterface,
            reply_details_dto: CreateCompleteReplyToCommentDTO
    ):
        comment_dto, comment_with_editable_status_dto, user_profile_dtos, \
        comment_id_with_mention_user_id_dtos, comment_id_with_multimedia_dtos = \
            self.reply_to_comment(
                reply_details_dto=reply_details_dto
            )
        response = presenter.prepare_response_for_reply(
            comment_dto=comment_dto, user_profile_dtos=user_profile_dtos,
            comment_with_editable_status_dto=comment_with_editable_status_dto,
            comment_id_with_mention_user_id_dtos=comment_id_with_mention_user_id_dtos,
            comment_id_with_multimedia_dtos=comment_id_with_multimedia_dtos
        )
        return response

    def reply_to_comment(
            self, reply_details_dto: CreateCompleteReplyToCommentDTO
    ):
        self._validate_reply_details(reply_dto=reply_details_dto)
        parent_comment_id = self.storage.get_parent_comment_id(
            comment_id=reply_details_dto.comment_id
        )
        if parent_comment_id is None:
            parent_comment_id = reply_details_dto.comment_id
        discussion_id = self.storage.get_discussion_id(
            comment_id=reply_details_dto.comment_id
        )
        reply_comment_id = self.storage.create_reply_to_comment(
            parent_comment_id=parent_comment_id, discussion_id=discussion_id,
            comment_content=reply_details_dto.comment_content,
            user_id=reply_details_dto.user_id,
        )
        self._add_mention_user_and_multimedia_dtos_for_comment(
            comment_id=reply_comment_id,
            mention_user_ids=reply_details_dto.mention_user_ids,
            multimedia_dtos=reply_details_dto.multimedia_dtos
        )
        comment_dto, comment_with_editable_status_dto, user_profile_dtos, \
        comment_id_with_mention_user_id_dtos, comment_id_with_multimedia_dtos = \
            self.get_reply_details(
                reply_comment_id=reply_comment_id,
                user_id=reply_details_dto.user_id
            )
        return (
            comment_dto, comment_with_editable_status_dto, user_profile_dtos,
            comment_id_with_mention_user_id_dtos,
            comment_id_with_multimedia_dtos
        )

    def _validate_reply_details(
            self, reply_dto: CreateCompleteReplyToCommentDTO
    ):
        self._validate_empty_comment_content_and_multimedia(
            create_complete_reply_to_comment_dto=reply_dto
        )
        self._validate_comment_id_and_mention_user_ids(
            create_complete_reply_to_comment_dto=reply_dto
        )

    def _add_mention_user_and_multimedia_dtos_for_comment(
            self, comment_id: str, mention_user_ids: List[str],
            multimedia_dtos: List[MultimediaDTO]
    ):
        self.storage.add_mention_users_to_comment(
            comment_id=comment_id,
            mention_user_ids=mention_user_ids
        )
        self.storage.add_multimedia_to_comment(
            comment_id=comment_id,
            multimedia_dtos=multimedia_dtos
        )

    @staticmethod
    def _validate_empty_comment_content_and_multimedia(
            create_complete_reply_to_comment_dto: CreateCompleteReplyToCommentDTO
    ):
        comment_content = create_complete_reply_to_comment_dto.comment_content
        multimedia_dtos = create_complete_reply_to_comment_dto.multimedia_dtos
        is_empty_comment_content_and_multimedia = not (
                comment_content or multimedia_dtos
        )
        if is_empty_comment_content_and_multimedia:
            raise EmptyCommentAndMultiMediaException

    def _validate_comment_id_and_mention_user_ids(
            self,
            create_complete_reply_to_comment_dto: CreateCompleteReplyToCommentDTO
    ):
        from ib_discussions.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        service_adapter.auth_service.validate_user_ids(
            user_ids=create_complete_reply_to_comment_dto.mention_user_ids)
        is_comment_id_not_exists = not self.storage.is_comment_id_exists(
            comment_id=create_complete_reply_to_comment_dto.comment_id
        )
        from ib_discussions.exceptions.custom_exceptions import \
            CommentIdNotFound
        if is_comment_id_not_exists:
            raise CommentIdNotFound

    def get_reply_details(self, reply_comment_id: str, user_id: str):
        comment_dto = self.storage.get_comment_details_dto(
            comment_id=reply_comment_id)
        comment_dtos = [comment_dto]

        comment_with_editable_status_dtos, user_profile_dtos, \
        comment_id_with_mention_user_id_dtos, comment_id_with_multimedia_dtos = \
            self.get_replies_for_comment(
                reply_dtos=comment_dtos, user_id=user_id)

        return (
            comment_dto, comment_with_editable_status_dtos[0],
            user_profile_dtos, comment_id_with_mention_user_id_dtos,
            comment_id_with_multimedia_dtos
        )

    def get_replies_for_comment(
            self, reply_dtos: List[CommentDTO], user_id: str
    ):
        comment_ids = [comment.comment_id for comment in reply_dtos]
        mention_user_ids = self.storage.get_mention_user_ids(
            comment_ids=comment_ids
        )
        user_ids = list(set(comment_dto.user_id for comment_dto in reply_dtos))
        user_ids = list(set(user_ids + mention_user_ids))
        user_profile_dtos = self._get_user_profile_dtos(user_ids=user_ids)
        comment_id_with_mention_user_id_dtos = \
            self.storage.get_comment_id_with_mention_user_id_dtos(
                comment_ids=comment_ids
            )
        comment_id_with_multimedia_dtos = self.storage.get_multimedia_dtos(
            comment_ids=comment_ids
        )
        comment_with_editable_status_dtos = \
            self._prepare_comment_editable_status_dtos(
                comment_dtos=reply_dtos, user_id=user_id
            )

        return (
            comment_with_editable_status_dtos, user_profile_dtos,
            comment_id_with_mention_user_id_dtos,
            comment_id_with_multimedia_dtos
        )

    @staticmethod
    def _get_user_profile_dtos(user_ids: List[str]) -> List[UserProfileDTO]:
        from ib_discussions.adapters.service_adapter import get_service_adapter
        adapter = get_service_adapter()
        user_profile_dtos = adapter.auth_service.get_user_profile_dtos(
            user_ids=user_ids
        )
        return user_profile_dtos

    @staticmethod
    def _prepare_comment_editable_status_dtos(
            comment_dtos: List[CommentDTO], user_id: str
    ) -> List[CommentIdWithEditableStatusDTO]:
        comment_editable_status_dtos = [
            CreateReplyToCommentInteractor._prepare_comment_editable_status_dto(
                comment_dto=comment_dto, user_id=user_id
            ) for comment_dto in comment_dtos
        ]
        return comment_editable_status_dtos

    @staticmethod
    def _prepare_comment_editable_status_dto(
            comment_dto: CommentDTO, user_id: str
    ) -> CommentIdWithEditableStatusDTO:
        is_editable = False
        is_user_comment_creator = str(user_id) == str(comment_dto.user_id)
        if is_user_comment_creator:
            is_editable = True
        comment_editable_status_dto = CommentIdWithEditableStatusDTO(
            comment_id=comment_dto.comment_id, is_editable=is_editable
        )
        return comment_editable_status_dto
