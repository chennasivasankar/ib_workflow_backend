from typing import List

from ib_boards.adapters.service_adapter import get_service_adapter
from ib_boards.exceptions.custom_exceptions import (
    InvalidBoardId, InvalidOffsetValue, InvalidLimitValue, UserDonotHaveAccess)
from ib_boards.interactors.dtos import ColumnParametersDTO, \
    PaginationParametersDTO, ColumnTaskIdsDTO, ColumnTasksDTO
from ib_boards.interactors.get_tasks_details_for_the_column_ids import \
    ColumnsTasksParametersDTO
from ib_boards.interactors.mixins.validation_mixins import ValidationMixin
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.storage_interfaces.dtos import ColumnDetailsDTO, \
    ColumnCompleteDetails
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetColumnDetailsInteractor(ValidationMixin):

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_column_details_wrapper(self, presenter: PresenterInterface,
                                   columns_parameters: ColumnParametersDTO,
                                   pagination_parameters:
                                   PaginationParametersDTO):
        try:
            column_details, column_tasks, tasks_complete_details_dto = \
                self.get_column_details(
                    columns_parameters=columns_parameters,
                    pagination_parameters=pagination_parameters
                )
        except InvalidBoardId:
            return presenter.response_for_invalid_board_id()
        except InvalidOffsetValue:
            return presenter.response_for_invalid_offset_value()
        except InvalidLimitValue:
            return presenter.response_for_invalid_limit_value()
        except UserDonotHaveAccess:
            return presenter.response_for_user_donot_have_access_for_board()
        return presenter.get_response_for_column_details(
            column_tasks=column_tasks, column_details=column_details,
            tasks_complete_details_dto=tasks_complete_details_dto,
        )

    def get_column_details(self, columns_parameters: ColumnParametersDTO,
                           pagination_parameters: PaginationParametersDTO):
        board_id = columns_parameters.board_id
        offset = pagination_parameters.offset
        limit = pagination_parameters.limit
        user_id = columns_parameters.user_id
        view_type = columns_parameters.view_type
        self.validate_board_id(board_id=board_id)

        project_id = self.storage.get_project_id_for_board(board_id)
        column_dtos = self._get_column_details_dto(board_id, user_id, project_id)
        column_ids = [column_dto.column_id for column_dto in column_dtos]
        column_tasks_parameters = ColumnsTasksParametersDTO(
            column_ids=column_ids,
            limit=limit,
            offset=offset,
            user_id=user_id,
            project_id=project_id,
            view_type=view_type,
            search_query=columns_parameters.search_query
        )
        # TODO need to prepare DTO
        tasks_complete_details_dto = \
            self._get_column_tasks_complete_details(column_tasks_parameters)

        column_tasks = self._get_column_task_ids_map(
            task_ids_stages_dtos=tasks_complete_details_dto.column_task_ids
        )
        column_details = self._get_total_tasks_for_the_columns(
            task_ids_stages_dtos=tasks_complete_details_dto.column_task_ids,
            column_dtos=column_dtos
        )
        return column_details, column_tasks, tasks_complete_details_dto

    def _get_column_tasks_complete_details(self,
                                           column_tasks: ColumnsTasksParametersDTO):
        from ib_boards.interactors.get_tasks_details_for_the_column_ids import \
            GetColumnsTasksDetailsInteractor
        interactor = GetColumnsTasksDetailsInteractor(
            storage=self.storage
        )
        return interactor.get_column_tasks_with_column_ids(
            column_tasks_parameters=column_tasks
        )

    def _get_column_details_dto(self, board_id: str, user_id: str,
                                project_id: str):
        user_service = get_service_adapter().iam_service
        user_roles = user_service.get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id)
        self._validate_if_user_has_permissions_for_given_board_id(
            board_id=board_id, user_roles=user_roles)

        column_ids = self.storage.get_column_ids_for_board(
            board_id=board_id, user_roles=user_roles)

        column_dtos = self.storage.get_columns_details(column_ids=column_ids)
        return column_dtos

    def _validate_if_user_has_permissions_for_given_board_id(self,
                                                             board_id: str,
                                                             user_roles: str):
        board_permitted_user_roles = self.storage. \
            get_permitted_user_roles_for_board(board_id=board_id)
        if "ALL ROLES" in board_permitted_user_roles:
            return
        has_permission = False
        for board_permitted_user_role in board_permitted_user_roles:
            if board_permitted_user_role in user_roles:
                has_permission = True
                break

        if not has_permission:
            raise UserDonotHaveAccess
        return

    @staticmethod
    def _get_total_tasks_for_the_columns(
            task_ids_stages_dtos: List[ColumnTaskIdsDTO],
            column_dtos: List[ColumnDetailsDTO]) \
            -> List[ColumnCompleteDetails]:
        columns_dict = {}
        for task_ids_stages_dto in task_ids_stages_dtos:
            columns_dict[task_ids_stages_dto.unique_key] = task_ids_stages_dto
        return [
            ColumnCompleteDetails(
                column_id=column_dto.column_id,
                name=column_dto.name,
                total_tasks=columns_dict[column_dto.column_id].total_tasks
            )
            for column_dto in column_dtos
        ]

    @staticmethod
    def _get_column_task_ids_map(
            task_ids_stages_dtos: List[ColumnTaskIdsDTO]) \
            -> List[ColumnTasksDTO]:
        column_tasks = []
        for task_ids_stages_dto in task_ids_stages_dtos:
            for task_stage_dto in task_ids_stages_dto.task_stage_ids:
                column_tasks.append(
                    ColumnTasksDTO(
                        column_id=task_ids_stages_dto.unique_key,
                        stage_id=task_stage_dto.stage_id,
                        task_id=task_stage_dto.task_id,
                        task_display_id=task_stage_dto.task_display_id
                    )
                )
        return column_tasks
