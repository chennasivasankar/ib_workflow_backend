"""
Created on: 05/09/20
Author: Pavankumar Pamuru

"""
from ib_boards.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue, OffsetValueExceedsTotalTasksCount, \
    UserDoNotHaveAccessToColumn, InvalidStageIds
from ib_boards.interactors.dtos import ColumnTasksParametersDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    GetColumnTasksListViewPresenterInterface
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetColumnTasksInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_column_tasks_wrapper(
            self, column_tasks_parameters: ColumnTasksParametersDTO,
            presenter: GetColumnTasksListViewPresenterInterface):
        from ib_boards.exceptions.custom_exceptions import InvalidColumnId
        try:
            complete_tasks_details_dto, all_fields = self.get_column_tasks(
                column_tasks_parameters=column_tasks_parameters
            )
        except InvalidColumnId:
            return presenter.get_response_for_the_invalid_column_id()
        except InvalidOffsetValue:
            return presenter.get_response_for_invalid_offset()
        except InvalidLimitValue:
            return presenter.get_response_for_invalid_limit()
        except OffsetValueExceedsTotalTasksCount:
            return presenter.get_response_for_offset_exceeds_total_tasks()
        except UserDoNotHaveAccessToColumn:
            return presenter.get_response_for_user_have_no_access_for_column()
        except InvalidStageIds as error:
            return presenter.get_response_for_invalid_stage_ids(error=error)
        return presenter.get_response_for_column_tasks_in_list_view(
            complete_tasks_details_dto=complete_tasks_details_dto,
            all_fields=all_fields
        )

    def get_column_tasks(self,
                         column_tasks_parameters: ColumnTasksParametersDTO):
        column_tasks_interactor = GetColumnTasksInteractor(
            storage=self.storage
        )
        all_fields = []
        complete_tasks_details_dto = column_tasks_interactor.get_column_tasks(
            column_tasks_parameters=column_tasks_parameters
        )
        return complete_tasks_details_dto, all_fields
