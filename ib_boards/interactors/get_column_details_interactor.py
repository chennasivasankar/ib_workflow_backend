from typing import List, Tuple

from ib_boards.adapters.service_adapter import get_service_adapter
from ib_boards.exceptions.custom_exceptions import (
    InvalidBoardId, InvalidOffsetValue, InvalidLimitValue, UserDonotHaveAccess)
from ib_boards.interactors.dtos import ColumnParametersDTO, \
    PaginationParametersDTO, ColumnTaskIdsDTO, ColumnTotalTasksDTO, \
    TaskCompleteDetailsDTO, TaskDTO, ActionDTO, ColumnTasksDTO
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.storage_interfaces.dtos import ColumnDetailsDTO, \
    ColumnCompleteDetails
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetColumnDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_column_details_wrapper(self, presenter: PresenterInterface,
                                   columns_parameters: ColumnParametersDTO,
                                   pagination_parameters: PaginationParametersDTO):
        try:
            column_details, task_fields_dtos, task_actions_dtos, column_tasks = \
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
            column_tasks=column_tasks, task_actions_dtos=task_actions_dtos,
            task_fields_dtos=task_fields_dtos, column_details=column_details)

    def get_column_details(self, columns_parameters: ColumnParametersDTO,
                           pagination_parameters: PaginationParametersDTO):
        board_id = columns_parameters.board_id
        offset = pagination_parameters.offset
        limit = pagination_parameters.limit
        user_id = columns_parameters.user_id

        self._validations(board_id, limit, offset)

        column_dtos = self._get_column_details_dto(board_id, user_id)
        column_ids = [column_dto.column_id for column_dto in column_dtos]
        column_stage_dtos = self.storage.get_columns_stage_ids(
            column_ids=column_ids
        )
        task_ids_stages_dtos = self._get_task_ids_for_given_stages(
            column_stage_dtos=column_stage_dtos,
            limit=limit,
            offset=offset
        )
        task_field_dtos, task_action_dtos = self._get_tasks_complete_details(
            task_ids_stages_dtos=task_ids_stages_dtos,
            user_id=user_id
        )
        column_tasks = self._get_column_task_ids_map(
            task_ids_stages_dtos=task_ids_stages_dtos
        )
        column_details = self._get_total_tasks_for_the_columns(
            task_ids_stages_dtos=task_ids_stages_dtos,
            column_dtos=column_dtos
        )
        return column_details, task_field_dtos, task_action_dtos, column_tasks

    @staticmethod
    def _get_tasks_complete_details(
            task_ids_stages_dtos: List[ColumnTaskIdsDTO],
            user_id: int) \
            -> Tuple[List[TaskDTO], List[ActionDTO]]:
        task_details_dtos = []
        for task_ids_stages_dto in task_ids_stages_dtos:
            for stage_id_dto in task_ids_stages_dto.task_stage_ids:
                from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
                task_details_dtos.append(
                    GetTaskDetailsDTO(
                        task_id=stage_id_dto.task_id,
                        stage_id=stage_id_dto.stage_id
                    )
                )
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        return service_adapter.task_service.get_task_complete_details(
            task_details_dtos, user_id=user_id)

    @staticmethod
    def _get_task_ids_for_given_stages(
            column_stage_dtos, limit: int, offset: int) \
            -> List[ColumnTaskIdsDTO]:
        from ib_boards.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO
        task_config_dto = [
            TaskDetailsConfigDTO(
                unique_key=column_stage_dto.column_id,
                stage_ids=column_stage_dto.stage_ids,
                offset=offset,
                limit=limit
            )
            for column_stage_dto in column_stage_dtos
        ]
        task_ids_details = service_adapter.task_service.get_task_ids_for_stage_ids(
            task_config_dtos=task_config_dto
        )
        return task_ids_details

    def _get_column_details_dto(self, board_id, user_id):
        user_service = get_service_adapter().iam_service
        user_roles = user_service.get_user_roles(user_id)
        self._validate_if_user_has_permissions_for_given_board_id(
            board_id=board_id, user_roles=user_roles)

        column_ids = self.storage.get_column_ids_for_board(
            board_id=board_id, user_roles=user_roles)

        column_dtos = self.storage.get_columns_details(column_ids=column_ids)
        return column_dtos

    def _validations(self, board_id: str, limit: int, offset: int):
        self._validate_offset_value(offset=offset)
        self._validate_limit_value(limit=limit)
        self._validate_board_id(board_id=board_id)

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
    def _validate_offset_value(offset: int):
        if offset < 0:
            raise InvalidOffsetValue
        return

    @staticmethod
    def _validate_limit_value(limit: int):
        if limit <= 0:
            raise InvalidLimitValue

    def _validate_board_id(self, board_id: str):
        is_valid = self.storage.validate_board_id(board_id=board_id)
        is_invalid = not is_valid

        if is_invalid:
            raise InvalidBoardId

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
                        task_id=task_stage_dto.task_id
                    )
                )
        return column_tasks
