from typing import List

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

    @staticmethod
    def _get_filter_ids(filters_dto: List[FilterDTO]):

        return[
            filter_dto.filter_id
            for filter_dto in filters_dto
        ]