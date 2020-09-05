"""
Created on: 05/09/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.exceptions.custom_exceptions import InvalidOffsetValue, \
    InvalidLimitValue, OffsetValueExceedsTotalTasksCount, \
    UserDoNotHaveAccessToColumn, InvalidStageIds
from ib_boards.interactors.dtos import ColumnTasksParametersDTO, FieldDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    GetColumnTasksListViewPresenterInterface
from ib_boards.interactors.storage_interfaces.dtos import AllFieldsDTO
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface, FieldDisplayStatusDTO


class GetColumnTasksInteractorListView:
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
        from ib_boards.interactors.get_column_tasks_interactor import \
            GetColumnTasksInteractor
        column_tasks_interactor = GetColumnTasksInteractor(
            storage=self.storage
        )
        complete_tasks_details_dto = column_tasks_interactor.get_column_tasks(
            column_tasks_parameters=column_tasks_parameters
        )
        field_dtos = complete_tasks_details_dto.task_fields_dtos
        field_ids = [field_dto.field_id for field_dto in field_dtos]
        all_fields = self._get_all_fields_in_the_column(
            column_id=column_tasks_parameters.column_id,
            user_id=column_tasks_parameters.user_id,
            field_ids=field_ids,
            field_dtos=field_dtos
        )
        return complete_tasks_details_dto, all_fields

    def _get_all_fields_in_the_column(
            self, column_id: str, user_id: str,
            field_ids: List[str], field_dtos: List[FieldDTO]) -> List[AllFieldsDTO]:
        present_field_ids = self.storage.get_present_field_ids(
            column_id=column_id,
            user_id=user_id
        )
        extra_field_ids = [
            field_id for field_id in field_ids
            if field_id not in present_field_ids
        ]
        if extra_field_ids:
            self.storage.create_field_ids_order_and_display_status(
                column_id=column_id,
                user_id=user_id,
                field_ids=extra_field_ids
            )
        field_ids_in_order = self.storage.get_field_ids_list_in_order(
            column_id=column_id,
            user_id=user_id,
        )
        field_display_status_dtos = self.storage.get_fields_display_status(
            column_id=column_id,
            user_id=user_id,
        )
        return self._get_all_fields(
            field_ids_in_order=field_ids_in_order,
            field_display_status_dtos=field_display_status_dtos,
            field_dtos=field_dtos,
            field_ids=field_ids
        )

    @staticmethod
    def _get_all_fields(
            field_ids_in_order: List[str],
            field_display_status_dtos: List[FieldDisplayStatusDTO],
            field_dtos: List[FieldDTO], field_ids: List[str]) -> List[AllFieldsDTO]:

        fields_display_status_dict = {}
        for field_display_status_dto in field_display_status_dtos:
            fields_display_status_dict[field_display_status_dto.field_id] =\
                field_display_status_dto.display_status

        field_display_name_dict = {}
        for field_dto in field_dtos:
            field_display_name_dict[field_dto.field_id] = field_dto.key

        return [
            AllFieldsDTO(
                field_id=field_id,
                display_name=field_display_name_dict[field_id],
                display_status=fields_display_status_dict[field_id],
                display_order=field_ids_in_order.index(field_id)
            )
            for field_id in field_ids
        ]


