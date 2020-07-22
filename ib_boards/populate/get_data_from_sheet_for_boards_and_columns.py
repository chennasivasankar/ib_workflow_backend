"""
Created on: 21/07/20
Author: Pavankumar Pamuru

"""
from typing import List, Dict


class GetBoardsAndColumnsDataFromSheet:

    @property
    def data_sheet(self):
        from ib_boards.populate.get_data_from_sheet import GetDataFromSheet
        return GetDataFromSheet()

    def get_data_from_sheet(self):

        from ib_boards.constants.constants import BOARDS_AND_COLUMN_SUB_SHEET
        field_records = self.data_sheet.get_data_from_sub_sheet(
            sub_sheet_name=BOARDS_AND_COLUMN_SUB_SHEET
        )
        self.validate_keys_in_given_dict(
            boards_columns_dicts=field_records[:4]
        )
        boards_columns_dicts = [
            self._get_list_of_dictionary_to_populate_data(field_record)
            for field_record in field_records[:4]
        ]
        return boards_columns_dicts

    def populate_data_from_sheet_to_create_boards_and_columns(self):
        boards_columns_dicts = self.get_data_from_sheet()
        from ib_boards.populate.populate_script_to_create_boards_and_columns \
            import PopulateCreateBoardsAndColumns
        populate_script = PopulateCreateBoardsAndColumns()
        populate_script.populate_create_boards_and_columns(
            boards_columns_dicts=boards_columns_dicts
        )

    def populate_data_from_sheet_to_add_or_delete_columns_for_board(self):
        boards_columns_dicts = self.get_data_from_sheet()
        from ib_boards.populate.populate_script_for_add_or_delete_columns_for_board \
            import PopulateAddOrDeleteColumnsForBoard
        populate_script = PopulateAddOrDeleteColumnsForBoard()
        populate_script.populate_add_or_delete_for_columns_for_board(
            boards_columns_dicts=boards_columns_dicts
        )

    def validate_keys_in_given_dict(self, boards_columns_dicts: List[Dict]):
        from schema import Schema, SchemaError
        schema = Schema(
            [{
                "Board ID*": str,
                "Board Display Name": str,
                "Column Order For Display": int,
                "Column ID*": str,
                "Column Display Name": str,
                "Task Template Stages that are visible in columns": str,
                "Visible to RoleIDs": str,
                "Column Summary": str,
                "Column Actions": str,
                "Card Info_Kanban": str,
                "Card Info_List": str

            }]
        )
        try:
            schema.validate(boards_columns_dicts)
        except SchemaError:
            self._raise_exception_for_invalid_data_format()

    def _raise_exception_for_invalid_data_format(self):
        valid_format = {
            "Board ID*": str,
            "Board Display Name": str,
            "Column Order For Display": int,
            "Column ID*": str,
            "Column Display Name": str,
            "Task Template Stages that are visible in columns": str,
            "Visible to RoleIDs": str,
            "Column Summary": str,
            "Column Actions": str,
            "Card Info_Kanban": str,
            "Card Info_List": str
        }
        self.data_sheet.raise_exception_for_valid_format(valid_format=valid_format)

    @staticmethod
    def _get_list_of_dictionary_to_populate_data(
            field_record: Dict) -> Dict:
        return {
            "board_id": field_record["Board ID*"],
            "board_display_name": field_record["Board Display Name"],
            "column_id": field_record["Column ID*"],
            "column_display_name": field_record["Column Display Name"],
            "display_order": field_record["Column Order For Display"],
            "user_role_ids": field_record["Visible to RoleIDs"],
            "column_summary": field_record["Column Summary"],
            "column_actions": field_record["Column Actions"],
            "task_template_stages": field_record["Task Template Stages that are visible in columns"],
            "kanban_view_fields": field_record["Card Info_Kanban"],
            "list_view_fields": field_record["Card Info_List"],
        }


