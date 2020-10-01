from typing import List, Optional

from ib_discussions.adapters.auth_service import UserProfileDTO
from ib_discussions.constants.enum import EntityType
from ib_discussions.exceptions.custom_exceptions import InvalidOffset, \
    InvalidLimit, InvalidUserId, DiscussionSetNotFound
from ib_discussions.interactors.dtos.dtos import GetDiscussionsInputDTO
from ib_discussions.interactors.presenter_interfaces.dtos import \
    DiscussionIdWithEditableStatusDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    GetDiscussionsPresenterInterface
from ib_discussions.interactors.storage_interfaces.dtos import DiscussionDTO
from ib_discussions.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetDiscussionInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_discussions_wrapper(
            self,
            get_discussions_input_dto: GetDiscussionsInputDTO,
            presenter: GetDiscussionsPresenterInterface
    ):
        try:
            response = self._get_discussions_response(
                get_discussions_input_dto=get_discussions_input_dto,
                presenter=presenter,
            )
        except InvalidOffset:
            response = presenter.response_for_invalid_offset()
        except InvalidLimit:
            response = presenter.response_for_invalid_limit()
        except InvalidUserId:
            response = presenter.response_for_invalid_user_id()
        return response

    def _get_discussions_response(
            self, get_discussions_input_dto: GetDiscussionsInputDTO,
            presenter: GetDiscussionsPresenterInterface
    ):
        discussions_with_users_and_discussion_count_dto, \
        discussion_id_with_editable_status_dtos, discussion_id_with_comments_count_dtos = \
            self.get_discussions_details_dto(
                get_discussions_input_dto=get_discussions_input_dto
            )
        return presenter.prepare_response_for_discussions_details_dto(
            discussions_with_users_and_discussion_count_dto=discussions_with_users_and_discussion_count_dto,
            discussion_id_with_editable_status_dtos \
                =discussion_id_with_editable_status_dtos,
            discussion_id_with_comments_count_dtos=discussion_id_with_comments_count_dtos
        )

    def get_discussions_details_dto(
            self, get_discussions_input_dto: GetDiscussionsInputDTO
    ):
        self._validate_limit_and_offset(
            get_discussions_input_dto=get_discussions_input_dto
        )
        discussion_dtos, discussion_set_id, total_discussions_count = \
            self._get_discussion_details(
                get_discussions_input_dto=get_discussions_input_dto
            )
        user_profile_dtos = self._get_user_profile_dtos(
            discussion_dtos=discussion_dtos
        )
        discussion_id_with_comments_count_dtos = \
            self.storage.get_comments_count_for_discussions(
                discussion_set_id=discussion_set_id
            )
        discussion_id_with_editable_status_dtos = \
            self._prepare_discussion_id_with_editable_status_dtos(
                discussion_dtos=discussion_dtos,
                user_id=get_discussions_input_dto.user_id
            )
        from ib_discussions.interactors.presenter_interfaces.dtos import \
            DiscussionsWithUsersAndDiscussionCountDTO
        discussions_with_users_and_discussion_count_dto = DiscussionsWithUsersAndDiscussionCountDTO(
            discussion_dtos=discussion_dtos,
            user_profile_dtos=user_profile_dtos,
            total_count=total_discussions_count
        )
        return discussions_with_users_and_discussion_count_dto, discussion_id_with_editable_status_dtos, \
               discussion_id_with_comments_count_dtos

    def _get_discussion_details(
            self, get_discussions_input_dto: GetDiscussionsInputDTO):
        entity_id_and_entity_type_dto = \
            get_discussions_input_dto.entity_id_and_entity_type_dto
        discussion_set_id = self._get_discussion_set_id(
            entity_id=entity_id_and_entity_type_dto.entity_id,
            entity_type=entity_id_and_entity_type_dto.entity_type
        )
        discussion_dtos = self.storage.get_discussion_dtos(
            discussion_set_id=discussion_set_id,
            get_discussions_input_dto=get_discussions_input_dto
        )
        total_discussions_count = self.storage.get_total_discussion_count(
            discussion_set_id=discussion_set_id,
            filter_by_dto=get_discussions_input_dto.filter_by_dto
        )
        return discussion_dtos, discussion_set_id, total_discussions_count

    def _validate_limit_and_offset(
            self, get_discussions_input_dto: GetDiscussionsInputDTO
    ):
        offset_and_limit_dto = get_discussions_input_dto.offset_and_limit_dto
        self._validate_offset(offset_and_limit_dto.offset)
        self._validate_limit(offset_and_limit_dto.limit)
        return

    @staticmethod
    def _validate_offset(offset: int) -> Optional[InvalidOffset]:
        is_invalid_offset = offset < 0
        if is_invalid_offset:
            raise InvalidOffset
        return

    @staticmethod
    def _validate_limit(limit: int) -> Optional[InvalidLimit]:
        is_invalid_limit = limit < 0
        if is_invalid_limit:
            raise InvalidLimit
        return

    @staticmethod
    def _get_user_profile_dtos(
            discussion_dtos: List[DiscussionDTO]
    ) -> List[UserProfileDTO]:
        user_ids = [
            complete_discussion_dto.user_id
            for complete_discussion_dto in discussion_dtos
        ]

        from ib_discussions.adapters.service_adapter import get_service_adapter
        auth_service = get_service_adapter().auth_service

        user_profile_dtos = auth_service.get_user_profile_dtos(
            user_ids=user_ids
        )
        return user_profile_dtos

    def _get_discussion_set_id(
            self, entity_id: str, entity_type: EntityType
    ) -> str:
        try:
            discussion_set_id = self.storage.get_discussion_set_id_if_exists(
                entity_id=entity_id, entity_type=entity_type
            )
        except DiscussionSetNotFound:
            discussion_set_id = self.storage.create_discussion_set_return_id(
                entity_id=entity_id, entity_type=entity_type
            )
        return discussion_set_id

    def _prepare_discussion_id_with_editable_status_dtos(
            self, discussion_dtos: List[DiscussionDTO], user_id: str
    ) -> List[DiscussionIdWithEditableStatusDTO]:
        discussion_id_with_editable_status_dtos = [
            self._prepare_discussion_id_with_editable_status_dto(
                discussion_dto=discussion_dto, user_id=user_id)
            for discussion_dto in discussion_dtos
        ]
        return discussion_id_with_editable_status_dtos

    @staticmethod
    def _prepare_discussion_id_with_editable_status_dto(
            discussion_dto: DiscussionDTO, user_id: str
    ) -> DiscussionIdWithEditableStatusDTO:
        is_editable = False
        id_discussion_owner_can_edit = discussion_dto.user_id == user_id
        if id_discussion_owner_can_edit:
            is_editable = True

        from ib_discussions.interactors.presenter_interfaces.dtos import \
            DiscussionIdWithEditableStatusDTO
        discussion_id_with_editable_status_dto = \
            DiscussionIdWithEditableStatusDTO(
                discussion_id=discussion_dto.discussion_id,
                is_editable=is_editable
            )
        return discussion_id_with_editable_status_dto
