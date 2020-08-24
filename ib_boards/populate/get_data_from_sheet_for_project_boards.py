from typing import Dict, List

from ib_boards.populate.populate_script_for_add_project_for_boards import \
    populate_project_for_boards


class GetSheetDataForProjectBoards:

    @property
    def data_sheet(self):
        from ib_boards.populate.get_data_from_sheet import GetDataFromSheet
        return GetDataFromSheet()

    def get_data_from_project_boards_sub_sheet(self, spread_sheet_name: str):
        from ib_boards.constants.constants import PROJECT_BOARDS_SUB_SHEET
        field_records = self.data_sheet.get_data_from_sub_sheet(
            spread_sheet_name=spread_sheet_name,
            sub_sheet_name=PROJECT_BOARDS_SUB_SHEET
        )
        self._validation_for_project_boards_dict(field_records)
        list_of_project_boards_dict = [
            self._convert_project_boards_sheet_data_dict_to_our_format(
                field_record
            )
            for field_record in field_records
        ]

        populate_project_for_boards(list_of_project_boards_dict)

    @staticmethod
    def _convert_project_boards_sheet_data_dict_to_our_format(
            field_record: Dict):
        return {
            "project_id": field_record["Project ID"],
            "board_id": field_record["Board ID"]
        }

    def _validation_for_project_boards_dict(self, project_dict: List[Dict]):
        from schema import Schema, SchemaError
        schema = Schema(
            [{
                "Project ID": str,
                "Board ID": str

            }],
            ignore_extra_keys=True
        )
        schema.validate(project_dict)
        try:
            schema.validate(project_dict)
        except SchemaError:
            self._raise_exception_for_invalid_format()

    def _raise_exception_for_invalid_format(self):
        valid_format = {
            "Project ID": "FIN_MAN",
            "Board ID": "FINB_VENDOR_REGISTRATION"

        }
        self.data_sheet.raise_exception_for_valid_format(valid_format)
