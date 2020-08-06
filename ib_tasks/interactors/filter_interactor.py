from typing import List

from ib_tasks.constants.enum import Status
from ib_tasks.interactors.filter_dtos import FilterDTO, FilterCompleteDetailsDTO
from ib_tasks.interactors.filter_dtos import CreateConditionDTO, CreateFilterDTO
from ib_tasks.interactors.presenter_interfaces.filter_presenter_interface import \
    FilterPresenterInterface
from ib_tasks.interactors.storage_interfaces.filter_storage_interface \
    import FilterStorageInterface


class FilterInteractor:

    def __init__(
            self, filter_storage: FilterStorageInterface,
            presenter: FilterPresenterInterface):
        self.presenter = presenter
        self.filter_storage = filter_storage

    def create_filter_wrapper(
            self, filter_dto: CreateFilterDTO,
            condition_dtos: CreateConditionDTO):
        pass

    def create_filter(
            self, filter_dto: CreateFilterDTO,
            condition_dtos: CreateConditionDTO):
        pass

    def update_filter_wrapper(
            self, filter_dto: CreateFilterDTO,
            condition_dtos: CreateConditionDTO):
        pass

    def update_filter(
            self, filter_dto: CreateFilterDTO,
            condition_dtos: CreateConditionDTO):
        pass

    def delete_filter_wrapper(self, filter_id: int, user_id: int):
        pass

    def delete_filter(self, filter_id: int, user_id: int):
        pass

    def get_filters_details(self, user_id: str):

        filters_dto = \
            self.filter_storage.get_filters_dto_to_user(user_id=user_id)
        filter_ids = self._get_filter_ids(filters_dto)
        conditions_dto = \
            self.filter_storage.get_conditions_to_filters(filter_ids=filter_ids)
        filter_complete_details_dto = FilterCompleteDetailsDTO(
            filters_dto=filters_dto,
            conditions_dto=conditions_dto
        )
        return self.presenter.get_response_for_get_filters_details(
            filter_complete_details=filter_complete_details_dto
        )

    def update_filter_select_status_wrapper(
            self, user_id: str, filter_id: int, is_selected: Status):
        from ib_tasks.exceptions.filter_exceptions import InvalidFilterId
        from ib_tasks.exceptions.filter_exceptions import UserNotHaveAccessToFilter
        try:
            response = self.update_filter_select_status(
                user_id=user_id, filter_id=filter_id, is_selected=is_selected
            )
        except InvalidFilterId:
            return self.presenter.get_response_for_invalid_filter_id()
        except UserNotHaveAccessToFilter:
            return self.presenter \
                .get_response_for_invalid_user_to_update_filter_status()
        return self.presenter.get_response_for_update_filter_status(
            filter_id=filter_id, is_selected=response
        )

    def update_filter_select_status(
            self, user_id: str, filter_id: int, is_selected: Status):

        self._validate_filter_id(filter_id=filter_id)
        self._validate_user_with_filter_id(
            user_id=user_id, filter_id=filter_id
        )
        is_enabled = is_selected == Status.ENABLED.value
        if is_enabled:
            response = self.filter_storage\
                .enable_filter_status(filter_id=filter_id)
        else:
            response = self.filter_storage\
                .disable_filter_status(filter_id=filter_id)
        return response

    def _validate_user_with_filter_id(self, user_id: str, filter_id: int):
        self.filter_storage.validate_user_with_filter_id(
            user_id=user_id, filter_id=filter_id
        )

    def _validate_filter_id(self, filter_id: int):
        self.filter_storage.validate_filter_id(
            filter_id=filter_id
        )

    @staticmethod
    def _get_filter_ids(filters_dto: List[FilterDTO]):

        return [
            filter_dto.filter_id
            for filter_dto in filters_dto
        ]
