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
