from ib_boards.adapters.service_adapter import get_service_adapter
from ib_boards.exceptions.custom_exceptions import (
    InvalidBoardId, InvalidOffsetValue, InvalidLimitValue, UserDonotHaveAccess)
from ib_boards.interactors.dtos import ColumnParametersDTO, PaginationParametersDTO, TaskDTO, TaskDetailsDTO, FieldsDTO
from ib_boards.interactors.get_task_details_interactor import GetTaskDetailsInteractor
from ib_boards.interactors.presenter_interfaces.presenter_interface import \
    PresenterInterface
from ib_boards.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class GetColumnDetailsInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_column_details_wrapper(self, presenter: PresenterInterface,
                                   columns_parameters: ColumnParametersDTO,
                                   pagination_parameters: PaginationParametersDTO):
        try:
            task_details, task_actions_dto, task_fields_dto, column_dtos = self. \
                get_column_details(columns_parameters=columns_parameters,
                                   pagination_parameters=pagination_parameters)
            return presenter.get_response_for_column_details(
                task_details=task_details, task_actions_dto=task_actions_dto,
                task_fields_dto=task_fields_dto, column_details=column_dtos)

        except InvalidBoardId:
            presenter.response_for_invalid_board_id()
        except InvalidOffsetValue:
            presenter.response_for_invalid_offset_value()
        except InvalidLimitValue:
            presenter.response_for_invalid_limit_value()
        except UserDonotHaveAccess:
            presenter.response_for_user_donot_have_access_for_board()

    def get_column_details(self, columns_parameters: ColumnParametersDTO,
                           pagination_parameters: PaginationParametersDTO):
        board_id = columns_parameters.board_id
        offset = pagination_parameters.offset
        limit = pagination_parameters.limit
        user_id = columns_parameters.user_id

        self._validations(board_id, limit, offset)

        column_dtos = self._get_column_details_dto(board_id, user_id)

        tasks_dtos = [TaskDetailsDTO(task_id="task_id_1",
                              column_id="column_id_1",
                              stage_id="stage_id_1")]
        fields_dto = [FieldsDTO(
            task_template_id="task_template_id_1",
            field_id="field_id_1"
        )]
        task_interactor = GetTaskDetailsInteractor()
        task_actions_dto, task_fields_dto, task_details = task_interactor. \
            get_task_details(tasks_dtos=tasks_dtos, user_id=user_id,
                             fields_dto=fields_dto)

        return task_details, task_actions_dto, task_fields_dto, column_dtos

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
