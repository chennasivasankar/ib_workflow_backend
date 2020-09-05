import abc
from typing import List

from ib_boards.constants.enum import DisplayStatus
from ib_boards.interactors.dtos import BoardDTO, ColumnDTO, \
    StarOrUnstarParametersDTO, ProjectBoardDTO, ChangeFieldsStatusParameter, \
    ChangeFieldsOrderParameter
from ib_boards.interactors.storage_interfaces.dtos import BoardColumnDTO, \
    ColumnStageIdsDTO, ColumnDetailsDTO, TaskBoardsDetailsDTO


class FieldOrderDTO:
    field_id: str
    order: int


class FieldDisplayStatusDTO:
    field_id: str
    display_status: DisplayStatus


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_project_id_for_board(self, board_id: str) -> str:
        pass

    @abc.abstractmethod
    def get_project_id_for_given_column_id(self, column_id: str) -> str:
        pass

    @abc.abstractmethod
    def add_project_id_for_boards(
            self, project_boards_dtos: List[ProjectBoardDTO]):
        pass

    @abc.abstractmethod
    def validate_board_id(self, board_id) -> bool:
        pass

    @abc.abstractmethod
    def create_boards_and_columns(
            self, board_dtos: List[BoardDTO],
            column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def get_board_ids_for_column_ids(self, column_ids: List[str]) -> List[
        BoardColumnDTO]:
        pass

    @abc.abstractmethod
    def get_boards_column_ids(
            self, board_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def update_columns_for_board(self, column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def create_columns_for_board(self, column_dtos: List[ColumnDTO]) -> None:
        pass

    @abc.abstractmethod
    def delete_columns_which_are_not_in_configuration(
            self, column_ids: List[str]) -> None:
        pass

    @abc.abstractmethod
    def validate_user_role_with_boards_roles(self, user_role: str):
        pass

    @abc.abstractmethod
    def get_board_ids(
            self, user_id: str, project_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def get_board_details(self, board_ids: List[str]) -> List[BoardDTO]:
        pass

    @abc.abstractmethod
    def get_valid_board_ids(self, board_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def validate_column_id(self, column_id: str) -> None:
        pass

    @abc.abstractmethod
    def get_column_display_stage_ids(self, column_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def validate_user_role_with_column_roles(self, user_role: str, column_id: str):
        pass

    @abc.abstractmethod
    def get_columns_details(self, column_ids: List[str]) -> \
            List[ColumnDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_column_ids_for_board(self, board_id: str, user_roles: List[str]) \
            -> List[str]:
        pass

    @abc.abstractmethod
    def get_permitted_user_roles_for_board(self, board_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def get_board_complete_details(self, board_id: str,
                                   stage_ids: List[str]) -> \
            TaskBoardsDetailsDTO:
        pass

    @abc.abstractmethod
    def get_column_details(self, board_id: str, user_roles: List[str]) \
            -> List[BoardColumnDTO]:
        pass

    @abc.abstractmethod
    def get_existing_board_ids(self) -> List[str]:
        pass

    @abc.abstractmethod
    def get_columns_stage_ids(self, column_ids: List[str]) -> List[ColumnStageIdsDTO]:
        pass

    @abc.abstractmethod
    def star_given_board(self,
                         parameters: StarOrUnstarParametersDTO):
        pass

    @abc.abstractmethod
    def unstar_given_board(self,
                           parameters: StarOrUnstarParametersDTO):
        pass

    @abc.abstractmethod
    def validate_field_id_with_column_id(self, column_id: str, field_id: str):
        pass

    @abc.abstractmethod
    def change_display_status_of_field(
            self, field_display_status_parameter: ChangeFieldsStatusParameter):
        pass

    @abc.abstractmethod
    def change_display_order_of_field(self, field_order_parameter: ChangeFieldsOrderParameter):
        pass

    @abc.abstractmethod
    def get_field_display_status_dtos(self, column_id: str, user_id: str) -> List[FieldDisplayStatusDTO]:
        pass

    @abc.abstractmethod
    def get_field_display_order_dtos(self, column_id: str, user_id: str) -> List[FieldOrderDTO]:
        pass
