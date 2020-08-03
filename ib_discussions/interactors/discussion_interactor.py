from typing import List

from ib_discussions.interactors.DTOs.common_dtos import DiscussionDTO, \
    EntityIdAndEntityTypeDTO, OffsetAndLimitDTO, FilterByDTO, SortByDTO
from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
    CreateDiscussionPresenterInterface, GetDiscussionsPresenterInterface
from ib_discussions.interactors.storage_interfaces.dtos import \
    CompleteDiscussionDTO
from ib_discussions.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class DiscussionSetNotFound(Exception):
    pass


class InvalidOffset(Exception):
    pass


class InvalidLimit(Exception):
    pass


class InvalidUserId(Exception):
    pass


class DiscussionInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def create_discussion_wrapper(self, discussion_dto: DiscussionDTO,
                                  presenter: CreateDiscussionPresenterInterface
                                  ):
        from ib_discussions.exceptions.custom_exceptions import \
            EntityIdNotFound, InvalidEntityTypeForEntityId
        try:
            response = self._create_discussion_response(
                discussion_dto=discussion_dto, presenter=presenter
            )
        except EntityIdNotFound:
            response = presenter.raise_exception_for_entity_id_not_found()
        except InvalidEntityTypeForEntityId:
            response = presenter. \
                raise_exception_for_invalid_entity_type_for_entity_id()
        return response

    def _create_discussion_response(
            self, discussion_dto: DiscussionDTO,
            presenter: CreateDiscussionPresenterInterface
    ):
        self.create_discussion(discussion_dto=discussion_dto)
        return presenter.prepare_success_response_for_create_discussion()

    def create_discussion(self, discussion_dto):
        # TODO: FIX IT
        # self.storage.validate_entity_id(entity_id=discussion_dto.entity_id)
        # self.storage.validate_entity_type_for_entity_id(
        #     entity_id=discussion_dto.entity_id,
        #     entity_type=discussion_dto.entity_type
        # )
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

    def get_discussions_wrapper(
            self, entity_id_and_entity_type_dto: EntityIdAndEntityTypeDTO,
            offset_and_limit_dto: OffsetAndLimitDTO,
            filter_by_dto: FilterByDTO, sort_by_dto: SortByDTO,
            presenter: GetDiscussionsPresenterInterface
    ):
        from ib_discussions.exceptions.custom_exceptions import \
            EntityIdNotFound, InvalidEntityTypeForEntityId
        try:
            response = self._get_discussions_response(
                entity_id_and_entity_type_dto=entity_id_and_entity_type_dto,
                offset_and_limit_dto=offset_and_limit_dto, presenter=presenter,
                filter_by_dto=filter_by_dto, sort_by_dto=sort_by_dto
            )
        except InvalidOffset:
            response = presenter.raise_exception_for_invalid_offset()
        except InvalidLimit:
            response = presenter.raise_exception_for_invalid_limit()
        except EntityIdNotFound:
            response = presenter.raise_exception_for_entity_id_not_found()
        except InvalidEntityTypeForEntityId:
            response = presenter. \
                raise_exception_for_invalid_entity_type_for_entity_id()
        except InvalidUserId:
            response = presenter.raise_exception_for_invalid_user_id()
        return response

    def _get_discussions_response(
            self, entity_id_and_entity_type_dto: EntityIdAndEntityTypeDTO,
            offset_and_limit_dto: OffsetAndLimitDTO,
            filter_by_dto: FilterByDTO, sort_by_dto: SortByDTO,
            presenter: GetDiscussionsPresenterInterface
    ):
        discussions_details_dto = self.get_discussions_details_dto(
            entity_id_and_entity_type_dto=entity_id_and_entity_type_dto,
            offset_and_limit_dto=offset_and_limit_dto,
            filter_by_dto=filter_by_dto, sort_by_dto=sort_by_dto
        )
        return presenter.prepare_response_for_discussions_details_dto(
            discussions_details_dto=discussions_details_dto
        )

    def get_discussions_details_dto(
            self, entity_id_and_entity_type_dto: EntityIdAndEntityTypeDTO,
            offset_and_limit_dto: OffsetAndLimitDTO,
            filter_by_dto: FilterByDTO, sort_by_dto: SortByDTO,
    ):
        self._validate_limit_offset_entity_id_and_entity_type(
            entity_id_and_entity_type_dto, offset_and_limit_dto)
        discussion_set_id = self._get_discussion_set_id(
            entity_id=entity_id_and_entity_type_dto.entity_id,
            entity_type=entity_id_and_entity_type_dto.entity_type
        )
        complete_discussion_dtos = self.storage.get_complete_discussion_dtos(
            discussion_set_id=discussion_set_id,
            offset_and_limit_dto=offset_and_limit_dto,
            filter_by_dto=filter_by_dto, sort_by_dto=sort_by_dto
        )
        total_discussions_count = self.storage.get_total_discussion_count(
            discussion_set_id=discussion_set_id, filter_by_dto=filter_by_dto
        )
        user_profile_dtos = self._get_user_profile_dtos(
            complete_discussion_dtos=complete_discussion_dtos
        )
        from ib_discussions.interactors.presenter_interfaces.dtos import \
            DiscussionsDetailsDTO
        discussions_details_dto = DiscussionsDetailsDTO(
            complete_discussion_dtos=complete_discussion_dtos,
            user_profile_dtos=user_profile_dtos,
            total_count=total_discussions_count
        )
        return discussions_details_dto

    def _validate_limit_offset_entity_id_and_entity_type(
            self, entity_id_and_entity_type_dto, offset_and_limit_dto
    ):
        self._validate_offset(offset_and_limit_dto.offset)
        self._validate_limit(offset_and_limit_dto.limit)
        # TODO: FIX IT
        # self.storage.validate_entity_id(
        #     entity_id=entity_id_and_entity_type_dto.entity_id
        # )
        # self.storage.validate_entity_type_for_entity_id(
        #     entity_id=entity_id_and_entity_type_dto.entity_id,
        #     entity_type=entity_id_and_entity_type_dto.entity_type
        # )

    @staticmethod
    def _validate_offset(offset):
        is_invalid_offset = offset < 0
        if is_invalid_offset:
            raise InvalidOffset

    @staticmethod
    def _validate_limit(limit):
        is_invalid_limit = limit < 0
        if is_invalid_limit:
            raise InvalidLimit

    @staticmethod
    def _get_user_profile_dtos(
            complete_discussion_dtos: List[CompleteDiscussionDTO]
    ):
        user_ids = [
            complete_discussion_dto.user_id
            for complete_discussion_dto in complete_discussion_dtos
        ]
        from ib_discussions.adapters.service_adapter import get_service_adapter
        auth_service = get_service_adapter().auth_service
        user_profile_dtos = auth_service.get_user_profile_dtos(
            user_ids=user_ids
        )
        return user_profile_dtos

    def _get_discussion_set_id(self, entity_id, entity_type):
        try:
            discussion_set_id = self.storage.get_discussion_set_id_if_exists(
                entity_id=entity_id, entity_type=entity_type
            )
        except DiscussionSetNotFound:
            discussion_set_id = self.storage.create_discussion_set_return_id(
                entity_id=entity_id, entity_type=entity_type
            )
        return discussion_set_id
